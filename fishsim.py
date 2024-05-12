#To do:
# Make the words "are" and "is" change depending on plurality
# Fix reproduction

import random
import math

for i in range(50):
    print("\n")

fish_amount = 10
money = 0
rnd1 = 0 #These vars are called so that the variable is defined just in case the IF statement below is run improperly.
rnd2 = 0

print("Hello, and welcome to Fish Simulator v1.2!")
print("- Each fish is worth 1$ in the first round and 3$ in the second. There are two rounds per year.")
print("- 8$ at the end of each year will be extracted for living expenses. If you go below 0$, you lose!")
print("- In between rounds 1 and 2 there is a chance that some of your fish will die.")
print("- If you try to take more fish than you have, the round will be skipped. Don't do it!")

while money > -1:
    print("\n")
    print("You have " + str(money) + "$ and there are " + str(fish_amount) + " fish in your lake.")
# Round 1
    take = input("How many fish would you like to take in the first round? ")
    if int(take) > fish_amount:
        print("You do not have that many fish.")
    else:
        print("   You take " + str(take) + " fish in round 1.")
        rnd1 = take
    fish_amount = int(fish_amount) - int(rnd1)

# Kill Phase
    prekill_amount = fish_amount
    num_killed = 0
    for i in range(prekill_amount):
        if random.randint(1,4) == 1:
            num_killed = num_killed + 1
            fish_amount = fish_amount - 1
    print("   " + str(num_killed) + " fish died. You have " + str(prekill_amount - num_killed) + " fish left.")
        
# Round 2
    take = input("How many fish would you like to take in the second round? ")
    if int(take) > fish_amount:
        print("You do not have that many fish.")
    else:
        print("   You take " + str(take) + " fish in round 2.")
        rnd2 = take
        fish_amount = int(fish_amount) - int(rnd2)
    profit = (int(rnd1) + 3*int(rnd2))
    money = (int(money) + int(profit))

# Reproduction Phase
    # num_born = math.floor(fish_amount / 2)
    # fish_amount = fish_amount + num_born
    # print("   " + str(num_born) + " fish were born.")

# Buy Phase
    print("You have " + str(money) + "$ and there are " + str(fish_amount) + " fish in your lake.")
    bought = input("How many fish would you like to buy? (1$ each) ")
    money = (int(money) - int(bought))
    fish_amount = int(fish_amount) + int(bought)
    money = int(money) - 8

print("YOU HAVE RUN OUT OF MONEY. YOU LOSE!")
