# Written by Patrick Keener on 11/05/2020
# Video Link: https://youtu.be/on8tSUqWg5M
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"
#
# DSC 430: Python Programming
# Assignment 0702: War and Random Numbers
#
# Requirements:
# 
# 1. [x] Create pnrg as an object (prng = WarandPeacePsuedoaRndomNumberGenerator())
# 2. [x]     Should be able to pass a seed
# 3. [x] Genereate prn's [0,1) by using prng.random()
# 4. 3-minute video:
# 4a.   [x]  Run code
# 4b.   [x]  Explain how prn's are produced
# 4c.   [x]  Generate 10k #s.  What's min, max, min? Does it make sense? 



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

def test():
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
    iterations = 10000
    print('\nGenerating {} random numbers...'.format(iterations))
    for n in range(iterations):
        numlist.append(a.random())
    
    
    print('Population Average: {}\npopulation Min: {}\nPopulation Max: {}'
        .format(sum(numlist)/iterations, min(numlist), max(numlist)))
    print('\n\nExecution Complete.')
    

test()