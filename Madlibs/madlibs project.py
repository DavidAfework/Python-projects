# Init variables

thematrix = ""
system = ""
Neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""

profession = ["","","",""]
adj = ["",""]

# Get input from user

print("welcome user!")
print("Let's play a game")
neo = input("please share with me your name?: ")

#Getting the matrix variable from user

print(f"Hello {neo}! Are you ready?")
thematrix = input("what is something you want to know more about?: ")

#Getting system variable from user

print(f"Oohh! I know, you want to learn more about {thematrix} right?")
print(f"So...what have you heard about {thematrix} on your travels?")
print(f"Would you like to know more?")
system = input(f"what noun would you categorize {thematrix} as: ")


#Getting enemy variable from user
enemy = input(f"Give me an opposing noun to {system}")
#Getting inside variable from user
inside = input(f"Now give me any relaxing noun(present tense): ")
#Getting all profession variables from user
print(f"Okay, now I need 4 professions relating to {system}")

for i in range(len(profession)):
    profession[i] = input(f"profession (plural) {i+1} / {len(profession)}")

#Getting the save variable from user
save = input(f"Give me a rescue related verb (present tense): ")

#Getting the unplugged variable
unplugged = input(f"And a verb that makes you think about relief (past tense): ")

#Getting the adjectives
print(f"lastly I need 2 dystopian describing words")

for i in range(len(adj)):
    adj[i] = input(f"Adjective {i+1} / {len(adj)}: ")

#Getting the fight variable
fight = input(f"& a verb: ")


# Init Story  
story = (f"{thematrix} is a {system}, {Neo}. That {system} is our {enemy}." ,\
 f"But when you're {inside}, you look around, what do you see? {profession[0]}, {profession[1]}, {profession[2]}, {profession[3]}. " ,\
      f"The very minds of the people we are trying to {save}."  ,\
          f"But until we do, these people are still a part of that {system} and that makes them our enemy. " ,\
              f"You have to understand, most of these people are not ready to be {unplugged}. " ,\
                   f"And many of them are so {adj[0]}, so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.")
# Print Story

print(story)
input()