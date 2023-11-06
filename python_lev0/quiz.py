print("Welcooe to my quiz game")

playing = input ("Do you want to play? ")
if playing.lower()!= "yes":
    quit()

print("Okay lets play!")
score=0
answer = input ("What does CPU stands for?  ")
if answer.lower() =="central processing unit":
    print("correct! ")
    score+=1
else:
    print("Incorrect!")

answer = input ("What does GPU stands for? ")
if answer.lower() =="graphics processing unit":
    print("correct! ")
    score+=1
else:
    print("Incorrect!")

answer = input ("What does RAM stands for? ")
if answer.lower() =="Random Access Memory":
    print("correct! ")
    score+=1
else:
    print("Incorrect!")

print ("you got "+str(score) + " questions correct!")
print ("you got "+str((score/3)*100 )+ " questions correct")