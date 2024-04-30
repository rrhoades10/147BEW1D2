torch_lit = True

if torch_lit: # if torch_list == True
    print("Venture forth into the cave!")

# else:
#     print("Maybe dont venture forth right now")

# The above is similar to this:
if True:
    print("go to the cave or whatever")

# is vs == 
# checking for equality you should ALWAYS use the double equals sign ==
weather = "sunny"
if weather == "sunny":
    print("Time to go kayaking and hiking and golfing and ultimate frisbeeing and frolicing")

""" Truth Tree
T & T == T
T & F == F
F & F == F
T || F == T
T || T == T
F || F == F
"""

# both statements need to be true when using and
gold_coins = 10
silver_coins = 50
if gold_coins > 5 and silver_coins > 30:
    print("You can afford the lactaid! Enjoy your calcium without the poops!")


# if not the whole statement will be considered false
gold_coins = 4
silver_coins = 50
if gold_coins > 5 and silver_coins > 30:
    print("You can afford the lactaid! Enjoy your calcium without the poops!")
else:
    print("Oh no! Dont drink any milk while youre on the road or things may get messy!")

# not != - it is true that somethign is not equal to something else
enemy = "goblin"

if enemy != "dragon":
    print("Charge forward, you mediocre adventurer")

enemy = "dragon"
if enemy != "dragon":
    print("Charge forward, you mediocre adventurer")
else:
    print("Ope! Theres a dragon, better hide!")


# <= and >= 
player_health = 75
if player_health <= 100:
    print("Drink a health potion for full strength!")
else:
    print("Youre good for now! Dont waste a potion!")


player_health = 150
if player_health >= 100:
    print("You're good to go! Go fight some stuff!")
else:
    print("Maybe you should drink a potion before continuing.")


# =================== RANGES ======================
magic_stones = 12
# gives a range between 10 and 20
# where 10 is less than or equal to our magic stones
# and our magic stones are less than or equal to 20
if 10 <= magic_stones <= 20:
    print("You've unlocked the magic chest!")



magic_stones = 21
if 10 <= magic_stones <= 20:
    print("You have absorbed the stones' power!")
else:
    print("You either have to little or too much power to absorb!")

# Combining Negative Checks
# flip the truth condition
# it is True that this is False

is_daytime = False
dragon_asleep = True
# true that its false     true
if not is_daytime and not dragon_asleep:
    print("Sneak into the dragon's layer and steal his dank lootz!")
else:
    print("Dragon is wake and its daytime!")

#                           same thing as dragon_asleep != True 
if is_daytime == False and not dragon_asleep == True:
    print("Sneak into the dragon's layer and steal his dank lootz!")
else:
    print("dragon is awake its daytime")

nums = []

if not nums:
    print("That list is empty")

if nums == []:
    print("That list is empty")

# ===================== ELIF ===============================
moon_phase = "full moon"
if moon_phase == "full moon":
    print("Beware of Werewolves!")
elif moon_phase == "new moon":
    print("Look out for sexy vampires")

# difference between elif and else
moon_phase = "full moon"
if moon_phase == "full moon":
    print("Beware of Werewolves!")
elif moon_phase == "new moon":
    print("Look out for sexy vampires")
else: #runs any other condition that the first if doesnt hit
    print("That is not how moons work!")


# FizzBuzz
# printing each number from 1 to n
# print FIZZ if the number is divisble by 3
# print BUZZ if the number is divisibly 5
# print FIZZBUZZ if the number is divisible by both 3 and 5

for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FIZZBUZZ")
    elif num % 5 == 0:
        print("BUZZ")
    elif num % 3 == 0:
        print("FIZZ")
    else:
        print(num)

potion_strength = 21
if potion_strength > 20:
    print("Thats a super potent potion")
elif potion_strength > 10:
    print("That is a moderately potent potion")

# checking for more than one specific condition with the elif
weather = "rainy"
if weather == "sunny":
    print("Its a bright sunshiny day!")
elif weather == "rainy":
    print("carry an umbrella")
elif weather == "snowy":
    print("Time to build a snowman!")
elif weather == "tornadoy":
    print("Go to the basement")
elif weather == "windy":
    print("go fly a kite")

# what happens if we just use ifs
# potion_strength = 21
# if potion_strength > 20:
#     print("Thats a super potent potion")
# if potion_strength > 10:
#     print("That is a moderately potent potion")
# if potion_strength > 5:
#     print("Thats a not potent potion")

# ^^ for the most part, 95% of the time, dont do that

sword_material = "gold"

if sword_material == "gold":
    print("The sword shines brightly!")
elif sword_material == "silver":
    print("The sword has a mystical glimmer")
elif sword_material == "bronze":
    print("The sword looks ancient and valuable!")
elif sword_material == "iron":
    print("That sword looks rusted and gross :(")

# trying to access a dungeon
player_level = 12

if player_level < 5:
    print("Access the beginner dungeon!")
elif player_level < 10:
    print("Enter the intermediate dungeon")
elif player_level > 10:
    print("Challenge the advanced dungeon!")

# try to golf
round_score = 99 # pretty good

print("Hello welcome to my golf course, dont be bad!")
if round_score > 150:
    print("Maybe go back to minigolf....")
elif round_score > 100:
    print("Ok you can come in but you have to do your best!")
elif round_score > 85:
    print("Youre ready for a pretty tough course maybe")
elif round_score < 85:
    print("You're pretty good, come on in!")

# combining conditions with and inside of elifs
is_dragon_present = False
has_treasure = False
#  is_dragon_present == True and has_treasure == False
if is_dragon_present and not has_treasure:
    print("Enter with caution! There be Dragons but no treasure :(")

#     is_dragon_present == False and has_treasure == True
elif not is_dragon_present and has_treasure:
    print("Theres no dragon! Come get some lootz")

#    is_dragon_present == True and has_treasure == True
elif is_dragon_present and has_treasure:
    print("A mighty dragon guards the treasure. Tread carefully!")

# is_dragon_present == False and has_treasure == False
else:
    print("The lair is empty, but theres also no treasure.")

# mixing potions
red_potion = False
blue_potion = False
#  if red_potion and not blue_potion
if red_potion == True and blue_potion == False:
    print("You got a potion of strength!")
#  if not red_potion and blue_potion
elif red_potion == False and blue_potion == True:
    print("You get a potion of speed!")
#  if red_potion and blue_potion
elif red_potion == True and blue_potion == True:
    print("OH NO! Mixing the potions made the explode!")
else: # if red_potion == False and blue_potion == False
    print("No potions were mixed!")



# combining conditions with and inside of elifs
# is_dragon_present = False
# has_treasure = False
# #  is_dragon_present == True and has_treasure == False
# if is_dragon_present and not has_treasure:
#     print("Enter with caution! There be Dragons but no treasure :(")

# #     is_dragon_present == False and has_treasure == True
# elif not is_dragon_present:
#     if has_treasure:
#         print("Theres no dragon! Come get some lootz")

# #    is_dragon_present == True and has_treasure == True
# elif is_dragon_present and has_treasure:
#     print("A mighty dragon guards the treasure. Tread carefully!")

# # is_dragon_present == False and has_treasure == False
# else:
#     print("The lair is empty, but theres also no treasure.")

# Using the else to account for anything else!
is_daytime = False
is_raining = False
if is_daytime: 
    print("Take the sunny path through the meadow")
elif is_raining:
    print("Take the rainy path through the swamp! wot r u doin in me swamp")
else:
    print("Neither path is suitable right now. Use your compass to head back home!")

weather = "hailing"
if weather == "sunny":
    print("Its a bright sunshiny day!")
elif weather == "rainy":
    print("carry an umbrella")
elif weather == "snowy":
    print("Time to build a snowman!")
elif weather == "tornadoy":
    print("Go to the basement")
elif weather == "windy":
    print("go fly a kite")
    # accounts for any possiblity that isnt listed above
else:
    print("Cant do anything in this weather, better stay inside!")

# using else with user input
# game = input("Would you like to play a game?")
# if game == "yes":
#     print("Cool, lets play monopoly!")
# elif game == "no":
#     print("Ok fine, ill play by myself")
# else: 
#     print("not a valid response....please answer with yes or no")

is_raining = False
is_cold = False
if is_raining and is_cold:
    print("Wear a waterproof jacket and scarf!")
elif is_raining:
    print("Dont forget your umbrella!")
else:
    print("Weather looks pretty good! Lets go outside!")

# going to the movies, can we get in?
# age = int(input("Enter your age: "))
# rating = input("Enter a movie rating (G, PG, PG-13, R)")

# if rating == "G":
#     print("You can watch the movie!")
# elif rating == "PG" and age >= 7:
#     print("You can watch the movie!")
# elif rating == "PG-13" and age >= 13:
#     print("You can watch the movie!")
# elif rating == "R" and age >= 17:
#     print("You can watch the movie!")
# else:
#     print("You are not allowed to watch that movie :(")


# A grading system
# take a user input for a grade
# write a conditional statement to check that grade and assign a letter grade
# based on the value
# A -> 90 or higher
# B -> 80-89
# C -> 70-79
# D -> 60- 69
# F -> 59 and lower

# score = int(input("What did you score on the test?"))
# if score >= 90:
#     print("You got an A!")
# elif score >= 80:
#     print("You got a B!")
# elif score >= 70:
#     print("You got a C.")
# elif score >= 60:
#     print("You got a D!")
# else:
#     print("Thats an F :(")


# Making some coffee
# take two user inputs asking if the user likes milk and sugar in their coffee
# One input for milk, one input for sugar

# if they like milk and sugar, make a coffee recomendation 
# if they dont like sweet coffee but they like milk then make a relevant coffee recommendation 
# if they like sugar but no milk then make a recommendation
# give them black coffee if they like neither


# sugar = input("Do you like to add sugar?") or ""
# milk = input("Do you like to add milk?") or ""
# if milk and sugar:
#   print('You can take fapoccino')
# elif sugar and not milk:
#   print('You can take sweet coffee with no milk')
# elif not sugar and milk:
#   print('You can take latte')  
# else:
#   print('You can take black coffee')



# sugar = input ("Do you want sugar? Please enter yes or no ")
# milk = input ("Do you want Milk? Please enter yes or no ")
# if sugar == "yes" and milk == "yes":
#     print("You should try out a caramel latte!")
# elif sugar == "no" and milk == "yes":
#     print("You should try a cafe au lait!")
# elif sugar == "yes" and milk == "no":
#     print("You should try a Cuban espresso!")
# else:
#     print("A black coffee is the best recommendation for you!")



# ===================== NESTING CONDITIONALS ============================
# a condition will run only if the "parent" condition is true
temperature = 14
if temperature < 25:
    print("Its quite chilly!")
    if temperature < 15:
        print("Actually, its super chilly. Grab that big ole coat!")

# nested conditional with else
temperature = 15
if temperature < 25:
    print("Its quite chilly!")
    if temperature <= 15:
        print("Actually, its super chilly. Grab that big ole coat!")
    else:
        print("Yeeeppp still pretty chilly")

age = 21
if age >= 18:
    if age >= 21:
        print("You can drive, vote, and also drink! and depending on your state smoke a little doob!")
    else:
        print("You can drive and vote!")
else:
    print("You're too young to drive or vote")

day = "Friday"
time = "afternoon"

if day == "Saturday":
    if time == "Morning":
        print("Exercise and Golf")
    elif time == "Evening":
        print("Drinks and drive some golf carts....responsibly")
    else:
        print("Take a nap")
elif day == "Friday":
    if time == "Morning":
        print("Bootcamp and hang out with Ryan...yayyy")
    elif time == "Evening":
        print("Drinkin")
    else:
        print("Hoping to finish class early so we can go partake in extra curricular activities ayy lmao")

names = ["Farzin", "Caleb", "Kayla", "Victor", "Pheona", "Ryan", "Bob", "Linda"]

for name in names:
    if name == "Farzin":
        print("Find cool facts about python pointers using is that Ryan doesnt know about")
    elif name == "Caleb":
        print("Shrugging off the question and chillin")
    elif name == "Kayla":
        print("Drinkin and playin golf")
    elif name == "Victor":
        print("Reading scary articles about google layoffs")
    elif name == "Pheona":
        print("Shopping for anything, clothing and stuff")
    else:
        print("Just hangin out")

# create a genre variable for a book
# check if that genre is equal to Fantasy, Adventure, Mystery etc..
# create a nested conditional to check who the author is

genre = "Fantasy"
author = "JRR Tolkien"
if genre == "Fantasy":
    if author == "JRR Tolkien":
        print("Theyre taking the hobbits to isengard")
    elif author == "CS Lewis":
        print("somethign about narnia")


genre = "Drama"
author = "tiger woods"
if genre == "Fantasy":
    if author == "JRR Tolkien":
        print("Theyre taking the hobbits to isengard")
    elif author == "CS Lewis":
        print("somethign about narnia")
elif genre == "Drama":
    if author== "tiger woods":
        print("golf am i right")
elif genre == "romance":
    if author=="ron swanson":
        print("ceder wood mmmmm")
elif genre == "action":
    if author=="batman":
        print("justice")


genre = "Fantasy"
author = "JRR Tolkien"
if genre == "Fantasy":
    if author == "JRR Tolkien":
        print("Theyre taking the hobbits to isengard")
    elif author == "CS Lewis":
        print("somethign about narnia")
elif genre == "Sci_fi":
    if author == "Arthur C Clarke":
        print("Did you enjoy 2001 Space Odyssey")
elif genre == "Historical fiction":
    if author == "Kent Follett":
        print("Does the end justify the means?")
    else:
        print("The titanic!")


genre = "Fantasy"
author = "J.K. Rowling"
if genre == "Fantasy":
    if author == "J.K. Rowling":
        print("Voldermolt is back")
    elif author == "Stephen King":
        print("The clowns back")
elif genre == "Anime":
    if author == "Koyoharu Gotouge":
        print("Nezuko is badass")
    elif author == "Eiichiro Oda":
        print("Luffy is cool")
else:
    print("I can't give you any information on that genre")


genre = "Action"
author = "Susie Joe"
if genre == "Action":
    if author == "Susie Joe":
        print("Saving the world")
    elif author == "John Doe":
        print("Killing the bad guy")
elif genre == "Rom Com":
    if author == "Harry":
        print("They love each other")
    elif author == "Larry":
        print("fairytale")
    else:
        print("They don't love each other")
else:
    print("These people have bad taste")


# genre = str(input("Enter your genre (Fiction, Fantasy or Romance): "))
# author = str(input("Enter your author (J.K. Rowling, Stephen King, Your option): "))
# if genre == "Fiction":
#     if author == "J.K. Rowling":
#         print("I'm going to read Harry Potter")
#     elif author == "Stephen King":
#         print("I'm going to read The Shining")
#     else:
#         print("I'm going to watch a movie")
# else:
#     question = input("Are you sure you want to read this book? (yes or no)" )
#     if question:
#         print("Awesome")
#     if not question:
#         print("That's alright!")



# ==================== SHORTHAND CONDITIONAL - TERNARY =======================
x = 5
y = 10
if x > y:
    print("x is greater")
else:
    print("y is greater")
# do this              if this  else    do this
print("x is greater") if x > y else print("y is greater")

# lets go to the beach....maybe
weather = "sunny"
# sets activity to "beach" if weather equals sunny otherwise activity is set to video games
activity = "beach" if weather == "sunny" else "video games"
print(activity)
# long hand version
if weather == "sunny":
    activity = "beach"
else:
    activity = "video games"
print(activity)

# what kind of exercise are we doing?

energy_level = 4.5
time_available = 60
# set short_on_time variable to a boolean based on if the right side of the equal sign is true
short_on_time = time_available < 45.0
print(short_on_time)

workout = "intense cardio" if energy_level > 4.0 and not short_on_time else "light yoga"
print(workout)

# =================== PASS ========================
# the pass lets skip over blocks of code until we get our lives together

weather = "blizzardy"

if weather == "sunny":
    print("Go to the beach...wear sunscreen!")
elif weather == "blizzard":
    pass
elif weather == "rainy":
    print("stomp some puddles")


name = "Victor"
if name == "Victor":
    # do something
    pass

def sign_in():
    pass


def sign_up():
    pass

bad_decision = "taco bell"
for letter in bad_decision:
    pass
