from os import system
import random

iterations = 1000

def withSwitching():
    car = 0

    for i in range(iterations):
        doors = ['car', 'goat', 'goat']

        doors.remove(random.choice(doors))  # choose a random door and switch
        doors.remove('goat')

        if doors[0] == 'car':
            car += 1

    print(f"When switched: {(car/iterations)*100}%")

def withoutSwitching():
    car = 0

    for i in range(iterations):
        doors = ['car', 'goat', 'goat']

        doors.remove('goat')

        if random.choice(doors) == 'car':
            car += 1
    
    print(f"When not switched: {(car/iterations)*100}%")

if __name__=='__main__':
    withSwitching()
    withoutSwitching()
    system("pause")
