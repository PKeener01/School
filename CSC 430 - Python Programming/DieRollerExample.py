import random

#I roll dice.  I don't care if it is for the console
#or for a fancy smancy GUI.
#I only roll a six sided die.
class DiceRoller:

  def registerDiceViewer(self, dv):
    self.dv = dv

  def roll(self):
    return random.randrange(6)+1

#I too roll dice.  I too don't care if it is for
#the console or for a fancy smancy GUI..
#But, I need input from the DiceViewer.
class FlexibleDiceRoller(DiceRoller):

  def roll(self):
    n = self.dv.queryUser("What size die should I role? : ")
    n = int(n)
    result = random.randrange(n)+1
    return result

#I present dice rolls.  I don't care how the die are rolled.
#I am just responsible for displaying the results...
#...and I might need to ask the user for some info if the
#dr needs me to.
#I print to the console, but another viewer could 'extend' me
#into a fancy smany GUI.
class DiceViewer:

  def registerDiceRoller(self, dr):
    self.dr = dr
    self.dr.registerDiceViewer(self)
  
  def queryUser(self, str):
    return input(str)

  def roll(self):
    print ( self.dr.roll() )

#I present dice rolls.  I don't care how the die are rolled.
#I am just responsible for displaying the results...
#...and I might need to ask the user for some info if the
#dr needs me to.
#I use some other means other than the console
#to interact with the user
class FancyDiceViewer(DiceViewer):

  #I will inhereit registerDiceRoller 

  def queryUser(self, str):
    #Here I might pop up a GUI window.
    pass

  def roll(self):
    #Here I present the roll in my GUI.
    pass


# ----- ----- ----- ----- ---- ----


dv = DiceViewer()

print ("Attempting: DiceRoller")
dv.registerDiceRoller( DiceRoller() )
dv.roll()

print ("Attempting: FlexibleDiceRoller")
dv.registerDiceRoller( FlexibleDiceRoller() )
dv.roll()