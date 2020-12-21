#this is a guess the number game.

print("hello! What is your name?")
myName=input()
number = 5

print("Well", myName + ", i am thinking of a number between 1 and 20")
print("take a guess")
guess = int(input())
if guess == number:
    print("Good job " + myName + "! you guessed my number! ")
if guess != number:
    print("fail")