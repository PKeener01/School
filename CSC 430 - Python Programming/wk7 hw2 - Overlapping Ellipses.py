# Written by Patrick Keener on 11/05/2020
# Video Link: https://youtu.be/XnAWEyo24KA
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"
#
# DSC 430: Python Programming
# Assignment 0702: Overlapping Ellipses
#
# Requirements:
#
# ellipse = curve in plane surrounding 2 focal points such that the sum of the 
# distances to the two focal points are constant for every point on the curve
#
#
# 1. [x] Create a 'Point' class that takes in the x & y coordinates of point
#       p1 = Point(2,3)
#       p2 = Point(4,3)
# 2. [x] Create an 'Ellipse' class that takes 2 points & width of long axis
#       el = Ellipse(p1, p2, 4)
# 3. [x] Write function that takes 2 ellipses and returns area of the overlap
# 4. [x] Leverage prng built in A1
# 5. 3 Minute Video:
# 5a.   [x] Run Code
# 5b.   [x] Briefly show code working on simple case (2 circles @ origin)
# 5c.   [x] Briefly show code working on more complicated example I come up with
# 5d.   [x] Show main loop of algorithm

# Initialize Testing
class point():
    """ holds an item of point class """
    def __init__(self, x=0, y=0):
        """ initialize point class """
        self.xCoord = x
        self.yCoord = y
        self.coords = (self.xCoord, self.yCoord)
    
    def getPoint(self):
        """ return coordinates """
        return self.coords

    def updatePoint(self, x=None, y=None):
        """ Updates the point """
        if x != None: self.xCoord = x
        if y != None: self.yCoord = y
        self.coords = (self.xCoord, self.yCoord)
    
    def getX(self):
        """ Returns x """
        return self.xCoord
    
    def getY(self):
        """ Returns Y """
        return self.yCoord


class ellipse():
    """ Holds an item of ellipse class """

    def __init__(self, p1, p2, width = 1):
        """ Initialize class """
        self.p1 = p1
        self.p2 = p2
        self.width = width

        # These are defined so they can be exposed to the user for testing
        self.distX1 = self.distX2 = self.distY1 = self.distY2 = self.distP1 = 0
        self.distP2 = 0
        self.hit = False
    
    def withinEllipse(self, testPoint):
        """ Determine whether the point is within the ellipse """
        # it is within the ellipse if the distance between the test point
        # and both focal points is <= width
        
        # All variables have been defined so they can be exposed to the user 
        # for testing & verification

        # Get distances between x coords
        self.distX1 = (self.p1.xCoord - testPoint.xCoord)**2
        self.distX2 = (self.p2.xCoord - testPoint.xCoord)**2

        # Get distances between Y coords
        self.distY1 = (self.p1.yCoord - testPoint.yCoord)**2
        self.distY2 = (self.p2.yCoord - testPoint.yCoord)**2

        # Final triangulation
        self.distP1 = (self.distY1 + self.distX1)**.5
        self.distP2 = (self.distY2 + self.distX2)**.5

        if self.distP1 + self.distP2 <= self.width:
            self.hit = True
        else:
            self.hit = False
        
        return self.hit
    

class WPprng():
    """ Class containing the war & peace prng """
    
    def __init__(self, seed = 1000, file = 'war-and-peace.txt', step = 100, bits = 32):
        """ Initialize Class """

        
        self.infile  = open(file, 'r')
        # Find file length to know when to roll over for generating many #s
        self.fileLength = int(self.infile.seek(0,2))
        self.step = step
        self.bits = bits
        self.randNum = 0
        self.binArray = []

        if seed == None: ### Note: this was not present at the time the video was recorded
            self.position == 999
        else: 
            self.position = int(seed - 1) 

        self.infile.seek(self.position, 0) # set seed location

        self.currentLetter = self.infile.read(1) # Initialize first value
        self.prevLetter = str()
       
           
    def updateRelPos(self, posChg = 100):
        """ Relatively update the position; negative values allowed """
        self.position += posChg
        
        # if position will be > length of file, roll over to start of file
        if self.position > self.fileLength:
            self.position -= self.fileLength
        
        self.infile.seek(self.position, 0)
        
        # update previous & current letters
        self.prevLetter, self.currentLetter = self.currentLetter, self.infile.read(1)
    

    def random(self):
        """ This will generate a random number using a 32-bit array """
        # initialize variables
        divisor = .5
        self.binArray = [] # reset binArray to empty
        self.randNum = 0 # reset number to 0

        # Move through the text and generate binary array based on relative values
        # of letters
        for i in range(self.bits):
            self.updateRelPos(self.step)
            if self.currentLetter > self.prevLetter:
                self.binArray.append(1)
            else:
                self.binArray.append(0)
        
        # for each num in array determine the value and add it up
        for bin in self.binArray:
            self.randNum += bin*divisor
            divisor /= 2
        
        return self.randNum



# Begin Function

def boundaries(e1, e2):
    """ Determine the boundaries for the square """
    minX = min(e1.p1.xCoord, e1.p2.xCoord, e2.p1.xCoord, e2.p2.xCoord) - max(e1.width, e2.width)
    maxX = max(e1.p1.xCoord, e1.p2.xCoord, e2.p1.xCoord, e2.p2.xCoord) + max(e1.width, e2.width)

    minY = min(e1.p1.yCoord, e1.p2.yCoord, e2.p1.yCoord, e2.p2.yCoord) - max(e1.width, e2.width)
    maxY = max(e1.p1.yCoord, e1.p2.yCoord, e2.p1.yCoord, e2.p2.yCoord) + max(e1.width, e2.width)
    return minX, minY, maxX, maxY

def getXY(prn, xRange, yRange, minX, minY):
    """ determine the random x y values """
    x = prn.random()
    y = prn.random()

    # Scale the random number to the range of numbers
    x = x * xRange + minX 
    y = y * yRange + minY

    return x, y


def OverlappingEllipses(ellipse1, ellipse2, seed = None):
    """ Determines area overlap of ellipses """
    e1HitCount = 0
    e2HitCount = 0
    totalHitCount = 0


    minX, minY, maxX, maxY = boundaries(ellipse1, ellipse2)

    xRange = maxX - minX # get the range of potential x values
    yRange = maxY - minY # get the range of potential y values

    prn = WPprng(seed) # initialize random object; ##### Added ability to use Seed after video

    for sim in range(1000):
        xRand, yRand = getXY(prn, xRange, yRange, minX, minY)
        testPoint = point(xRand, yRand)

        # Check that points are in the ellipses
        e1 = ellipse1.withinEllipse(testPoint)
        if e1: e1HitCount += 1
        e2 = ellipse2.withinEllipse(testPoint)
        if e2: e2HitCount += 1
        if e1 and e2 == True: totalHitCount += 1
    
    print('E1 Hits: {}\nE2 Hits: {}\nTotal Hits: {}'
        .format(e1HitCount, e2HitCount,totalHitCount))
    e1Overlap = totalHitCount/e1HitCount * 100
    e2Overlap = totalHitCount/e2HitCount * 100

    print('Area of Overlapping Circumference:'
    'Ellipse 1 has approximately %{:.2f} of its area overlapping Ellipse 2, '
    'whereas Ellipse 2 has approximates %{:.2f} of its area overlapping Ellipse 1.'
    .format(e1Overlap, e2Overlap) 
    )





## Test Ellipses

p1 = point(0,0)
p2 = point(0,0)
e1 = ellipse(p1,p2,2)

p3 = point(0,0)
p4 = point(0,0)
e2 = ellipse(p3,p4,2)

OverlappingEllipses(e1, e2)


p1 = point(5,1)
p2 = point(8,3)
e1 = ellipse(p1,p2,20)

p3 = point(5,3)
p4 = point(15,7)
e2 = ellipse(p3,p4,25)

OverlappingEllipses(e1, e2)








# ==========  Testing ============

def A1test():
    """ A function used for testing the code """
    a = WPprng()
    print('Starting Position: {}'.format(a.infile.tell()))
    print('File Length: {}\nStep Size: {}'.format(a.fileLength, a.step))
    print('Current Letter: {}\nPrevious Letter (should be empty): {}'
        .format(a.currentLetter, a.prevLetter))
    
    print('\nUpdating Relative Position by 100')
    a.updateRelPos(100)
    print('New Cursor Position: {}'.format(a.infile.tell()))
    print('New Current Letter: {}\nNew Previous Letter: {}'
        .format(a.currentLetter, a.prevLetter))
    
    print('\nGenerating Random Number')
    a.random()
    print('Ending Cursor Position: {}\nRandom Number: {}\nArray Used: {}'
        .format(a.infile.tell(), a.randNum, a.binArray))
    
    
    numlist = []
    iterations = 1000
    print('\nGenerating {} random numbers...'.format(iterations))
    for n in range(iterations):
        numlist.append(a.random())
    
    print('Population Average (should be .459251): {}'
        '\npopulation Min (should be .0169193): {}'
        '\nPopulation Max (should be .976971): {}'
        .format(sum(numlist)/iterations, min(numlist), max(numlist)))
    print('\n\nExecution Complete.')

def pointTest():
    """ test point class """
    a = point()
    
    print('Initial Point; Should be 0, 0: {}'.format(a.getPoint()))
    a.updatePoint(2,3)
    print('Update point to 2,3: {}'.format(a.getPoint()))

    a.updatePoint(1)
    print('Update x to 1: {}'.format(a.getPoint()))
    
    a.updatePoint(None,5)
    print('Update y to 5: {}'.format(a.getPoint()))


def ellipseTest():
    """ test ellipse class """
    p1 = point(1,1)
    p2 = point(2,2)
    e = ellipse(p1, p2, 3)

    print('\nShould be a miss:')
    testPt = point(1.5,8)
    e.withinEllipse(testPt)
    print(e.distP1)
    print(e.distP2)
    print(e.width)
    print(e.hit)
    
    print('\nShould be a hit:')
    testPt = point(1.5,2)
    e.withinEllipse(testPt)
    print(e.distP1)
    print(e.distP2)
    print(e.width)
    print(e.hit)


def testing():
    """ execute tests """
    pointTest()
    ellipseTest()
    A1test()