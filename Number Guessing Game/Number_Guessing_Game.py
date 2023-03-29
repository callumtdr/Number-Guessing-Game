import random


num = random.randint(1,100) #Generates a random number between 1 and 100.
correct = False #sets the intial guess as incorrect so the while loop can initiate.

count = 0 #sets the initial count of guesses to 0.

while correct == False:
    guess = input("Enter a number between 1 and 100: ")

    guess = int(guess) #converts the users input into an integer from string.

    if guess == num: #if the users guess is the same as the generated number, the count is increases by 1 and changes the "correct" variable to True ending the while loop and finishing the game.
        count+=1
        print("Thats it, good job!")
        correct = True
        if count == 1:
            print("First guess, you must be psychic")
        else:
            print("you made",count,"guesses" )
            
    elif guess < num: #if the guess is too high or too low the count is increased by one and the "correct" variable is still false.
        print("Your guess too low")
        count+=1
        correct =False
    elif guess > num:
        print("Your guess is too high")
        count+=1
        correct = False
    
