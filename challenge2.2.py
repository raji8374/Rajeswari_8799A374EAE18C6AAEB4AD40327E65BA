#-Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes. Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling, respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.
#define the player class
class player:
  def play(self):
    print("The player is playing cricket.")
#define the batsman class, derived from player
class batsman(player):
  def play(self):
    print("The batsman is batting.")
#define the bowler class,derived from player
class bowler(player):
  def play(self):
    print("The bowler is bowling.")
#create objects of batsman and bowler classes
batsman=batsman()
bowler=bowler()
#call the play() method for each object
batsman.play()
bowler.play()