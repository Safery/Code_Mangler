# Code_Mangler
Code Mangler is an Idea gotten from my CSC professor Dr. Brian at University of Toronto. All credit to him. The principle idea behind the algorithm is, it will shuffle your code. 

# Tutorial
* 1. - Download and save run.py same directory as your code
* 2. - Copy your code and save it to .txt file. Please make SURE your code is PEP-8 compatible and remove any DOCSTRING! but you may keep the comments
* 3. - Run your run.py (you do not have to open it in IDE. Just double click to run.
* 4. - Your shuffled code should appear in a new file call 'Mangled.txt'

# Example

* Please make sure to remove ANY Doctring from the code. Example from my 21 game:
```python
class Computer(object):
    def __init__(self, t):
        # Numer of sticks, chosen mode
        self.stick = 21
        self.t = str(t)
        self._post = [0, 1]

    def normal(self):
        # Given amonut of sticks players can choose.
        self._x = 3
        while True:
            self._i = self.stick / self._x
            if ((self._i % 2) in self._post):
                self.stick -= self._x
                break
            else:
                self._x -= 1
                if (self._x == 0):
                    self._x = 3

    def hard(self):
        pass

    def noob(self):
        pass

    def stick_left(self):
        return self.stick

    def remove_stick(self, s):
        self.stick -= int(s)


def game_of_21(s, t):
    # Initiliaze a new Computer class
    computer = Computer(t)
    # Variable to determine which players has to play next
    x = 0
    while (int(computer.stick_left()) > 0):
        # Determine if var x is an odd or even number.
        if ((x % 2) == 0):
            print('There are currently ' + str(computer.stick_left()) +
                  ' sticks left.')
            get_input = input('How many stick would you like to remove: ')
            # Get user sticks
            computer.remove_stick(get_input)
            # Determine how many sticks are left if its below 0, let player win
            if (int(computer.stick_left()) <= 0):
                print('You Won!')
            x += 1
        else:
            # Chooose computer skill based on the player input.
            if (t == 'hard'):
                # Determine how many sticks are left
                s = computer.stick_left()
                # Initialize/ run the given input Mode.
                computer.hard()
                print('Computer chose ' + str(computer.stick_left() - s)[1] +
                      ' sticks')
            elif (t == 'normal'):
                # Initialize/ run the given input Mode.
                computer.normal()
            else:
                # Initialize/ run the given input Mode.
                computer.noob()
            # Determine how many sticks are left if its below 0, let player win
            if (int(computer.stick_left()) <= 0):
                print('Computer Won!')
            x += 1
```

* The algorithm should produce something like this:

```
def __init__(self, t):

# Determine if var x is an odd or even number.

class Computer(object):
self.stick = 21

self._post = [0, 1]

def normal(self):

self._x = 3

# Determine how many sticks are left if its below 0, let player win

self._i = self.stick / self._x

self.stick -= self._x

x = 0

if (t == 'hard'):

else:

if (self._x == 0):

def hard(self):

s = computer.stick_left()



if (int(computer.stick_left()) <= 0):

def remove_stick(self, s):

def game_of_21(s, t):
print('There are currently ' + str(computer.stick_left()) +

computer = Computer(t)

get_input = input('How many stick would you like to remove: ')

# Initialize/ run the given input Mode.

computer.remove_stick(get_input)

x += 1

computer.hard()

' sticks')
```

# TO DO
*  There are few bugs left to fix. One of the most common being, if the comment is double lined (ie exceeds 80 lines limit), it makes a new line (which don't make sense in the produced mangled).
