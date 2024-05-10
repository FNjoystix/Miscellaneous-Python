#To do:
# - Make the fish reproduce 1 for every 2
# - Make fish die occasionally to put some weight on round 1

for i in range(50):
    print("\n")

fish_amount = 10
money = 0
rnd1 = 0 #These vars are called so that the variable is defined just in case the IF statement below is run improperly.
rnd2 = 0
print("Each fish is worth 1$ in the first round and 3$ in the second. There are two rounds per year.")
print("8$ at the end of each year will be extracted for living expenses. If you cannot pay that, you lose.")

while money > -1:
    print("\n")
    print("You have " + str(money) + "$ and there are " + str(fish_amount) + " fish in your lake.")
    take = input("How many fish would you like to take in the first round? ")
    if int(take) > fish_amount:
        print("You do not have that many fish.")
    else:
        print("   You take " + str(take) + " fish in round 1.")
        rnd1 = take
        fish_amount = int(fish_amount) - int(rnd1)
    take = input("How many fish would you like to take in the second round? ")
    if int(take) > fish_amount:
        print("You do not have that many fish.")
    else:
        print("   You take " + str(take) + " fish in round 2.")
        rnd2 = take
        fish_amount = int(fish_amount) - int(rnd2)
    profit = (int(rnd1) + 3*int(rnd2))
    money = (int(money) + int(profit))
    bought = input("How many fish would you like to buy? (1$ each) ")
    money = (int(money) - int(bought))
    fish_amount = int(fish_amount) + int(bought)
    money = int(money) - 8
print("YOU HAVE RUN OUT OF MONEY. YOU LOSE!")