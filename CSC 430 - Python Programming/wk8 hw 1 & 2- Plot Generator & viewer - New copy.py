# Written by Patrick Keener on 11/11/2020
# Video Link:  https://youtu.be/OlEex3HZK1s
# Honor Statement:  "I have not given or received any unauthorized assistence 
#                    on this assignment"
#
# DSC 430: Python Programming
# Assignment 0801 & 0802: Plot Generator and Plot Viewer

import random

class SimplePlotGenerator():
    

    """ A simple plot generator """
    def __init__(self):
        """ Creates initial variables """
        # create a list with random words selected from file to be read into
        # the perscribed format
        self.storyWords = list()
        self.plot = str()
    
    def registerPlotViewer(self, pv):
        """register the plot viewer"""
        self.pv = pv
        
    def generate(self):
        """ generates simple plot """
        self.plot = str("Something happens")
        return None
    
    def display(self):
        """ Displays results 
        
        Pattern: [Name], a [adjective] [profession], must [verb] the 
        [adjective_evil] [villain job], [villain]
        
        """

        # Select 'a' or 'an' as appropriate
        if self.storyWords[1][0] in 'aeiou': 
            self.storyWords.insert(1, 'an')
        else:
            self.storyWords.insert(1, 'a')
        
        # ============== Change =====================
        # Adjusted after video to move output from model to viewer
        self.plot = str('{}, {} {} {}, must {} the {} {}, {}.'
        .format(*self.storyWords))

        return None

    def readWords(self):
        """ Read each file into a list of strings """
            
        words = open("plot_adjectives.txt", "r")
        self.plot_adjectives = words.read().splitlines()
                
        words = open("plot_adjectives_evil.txt", "r")
        self.plot_adjectives_evil = words.read().splitlines()

        words = open("plot_names.txt", "r")
        self.plot_names = words.read().splitlines()

        words = open("plot_profesions.txt", "r")
        self.plot_professions = words.read().splitlines()

        words = open("plot_verbs.txt", "r")
        self.plot_verbs = words.read().splitlines()

        words = open("plot_villains.txt", "r")
        self.plot_villains = words.read().splitlines()

        words = open("plot_villian_job.txt", "r")
        self.plot_villain_job = words.read().splitlines()
        
        return None


class RandomPlotGenerator(SimplePlotGenerator):
    
    """ Generates a random plot produced from 7 files found on d2l"""

    def __init__(self):
        """ initialize class """
        self.storyWords = list()
        self.readWords() # import the words
        return None

    def generate(self):
        """ Writes a random story to a list which will be displayed using 
        another function
        """        
        
        # Select the story words
        self.storyWords.append(random.choice(self.plot_names).strip())
        self.storyWords.append(random.choice(self.plot_adjectives).strip())
        self.storyWords.append(random.choice(self.plot_professions).strip())
        self.storyWords.append(random.choice(self.plot_verbs).strip())
        self.storyWords.append(random.choice(self.plot_adjectives_evil).strip())
        self.storyWords.append(random.choice(self.plot_villain_job).strip())
        self.storyWords.append(random.choice(self.plot_villains).strip())

        # Display output
        self.display()
        return None
    

class InteractivePlotGenerator(SimplePlotGenerator):
    """ A class to tell a story of the user's choosing """
    

    def __init__(self):
        """ initialize class, read data, generate lists"""
        self.storyWords = list()
        self.wordList = list()
        self.readWords() # import the words
        self.generateUILists() # generate the words for the UI
        return None
    
    def generateUILists(self):
        """ Generate the list of names to be displayed to the user """

        # Select 5 random words, striping leading/trailing spaces as we go
        # Append into list of lists
        self.wordList += [[x.strip() for x in random.choices(self.plot_names,k = 5)]]
        self.wordList += [[x.strip() for x in random.choices(self.plot_adjectives, k = 5)]]
        self.wordList += [[x.strip() for x in random.choices(self.plot_professions, k = 5)]]
        self.wordList += [[x.strip() for x in random.choices(self.plot_verbs, k = 5)]]
        self.wordList += [[x.strip() for x in random.choices(self.plot_adjectives_evil, k = 5)]]
        self.wordList += [[x.strip() for x in random.choices(self.plot_villain_job, k = 5)]]
        self.wordList += [[x.strip() for x in random.choices(self.plot_villains, k = 5)]]

    def generate(self):
        """ Interactively generate a plot """
        
        # Cycle through each part of speech
        for wordType in self.wordList:

            # Initialize variables 
            questionString = 'Please enter the number corresponding to your selection:'
            self.counter = 0

            # Cycle through each word type and add it to a string to create a
            # formatted list of words with corresponding numbers
            for word in wordType:
                self.counter += 1
                questionString += str('\n{}. {}').format(self.counter, word)
            
            questionString += '\nSelection: '
            
            # Query the user then add the corresponding index to the plot
            self.storyWords.append(
                wordType[self.pv.queryUser(questionString) -1])
        
        self.display() # display the final plot


class PlotViewer:
    
    """ Acts as viewer and controller of plot production methods """

    def registerPlotGenerator(self, pg):
        """ register the plot generator """
        self.pg = pg
        self.pg.registerPlotViewer(self)
    
    def generate(self):
        """ Generates the plot """
        self.pg.generate()
        self.display()  # Added after video
    
    def display(self): # added after video
        print(self.pg.plot)

    def queryUser(self, str):
        """ queries user to build plot """
        return self.userInput(str)
    
    def userInput(self, qString, intCheck = True, posCheck = True, maxNumCheck = True):
        """ Utility function to get user input and check for common errors, allows
        checking to be turned on or off.

        Errors Checked:
        1. Is an integer
        2. Is positive 
        """

        while True:
            userResponse = input(qString)
        
            try:
                userResponse = eval(userResponse)
            except:
                print('Please enter an number\n')
                continue
            
            if maxNumCheck == True:
                if userResponse > self.pg.counter:
                    print('The number is too high.  Please try again. \n')
                    continue

            if intCheck == True:
                if userResponse != userResponse//1: # Check if integer
                    print('The number must be an integer. Please try again.\n')
                    continue
            
            if posCheck == True:
                if userResponse < 0: # ensure it is positive
                    print('The number must be positive\n')
                    continue
            
            return userResponse



# ====================== Testing Scripts =====================

def viewerTest():
    """ test the viewer: """
    print("\n\nTest the viewer")
    a = PlotViewer()
    print('\nSimple plot generator test:')
    a.registerPlotGenerator(SimplePlotGenerator())
    a.generate()

    print('\nRandom plot generator test:')
    a.registerPlotGenerator(RandomPlotGenerator())
    a.generate()

    print('\nInteractive plot generator test:')
    a.registerPlotGenerator(InteractivePlotGenerator())
    a.generate()
    
    print('\n')
    # print(a.namesList)


def randomTest():
    pg = RandomPlotGenerator()
    
    print("Check for correct read-in:\n"
    "Adjective: {}\nEvil Adjective: {}\nName: {}\nProfession: {}\n"
    "Verb: {}\nVillain: {}\nVillain Job: {}\n".format(
        pg.plot_adjectives[0], pg.plot_adjectives_evil[0], pg.plot_names[0],
        pg.plot_professions[0], pg.plot_verbs[0], pg.plot_villains[0],
        pg.plot_villain_job[0]
    )) 
    
    print("Test Random Plot:")
    pg.generate()


def simpleTest():
    """ Testing for simple plot """
    print("Test simple plot:")
    pg = SimplePlotGenerator()
    pg.generate()
    print('\n')


def testing():
    """ Automated Testing Suite """
    simpleTest()
    randomTest()
    viewerTest()



testing()