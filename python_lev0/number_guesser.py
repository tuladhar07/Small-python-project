import random
top_of_Range= input("type a number: ")

if top_of_Range.isdigit():
    top_of_Range=int(top_of_Range)

    if top_of_Range<=0 :
        print("please enter number larger than 0 next time. ")
        quit()
else:
    print("enter a number next time")
    quit()

random_number= random.randint(0, top_of_Range)
while True:
    user_guess=input("make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time.")
        continue 
    
    if user_guess==random_number:
        print("You got  it! ")
        break
    elif user_guess> random_number:
         print("You were above the number! ")
    else:
            print("you were below the number!")