print("Welcome to my computer quiz!")

play = input("Do you want to play the game? ").lower()
print(play)

if play != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# Question 1
answer = input("What does CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("What does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("What does PSU stands for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 5
answer = input("What does WWW stands for? ").lower()
if answer == "world wide web":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Shows score 
print("You got " + str(score) + " questions correct!")
# Shows Percentage
print("You got " + str((score/5)* 100) + "%")