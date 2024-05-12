# My first Python program!

for i in range(50):
    print("\n")     

import random
r = random.randint(1,100)
g = 0
while r != g:
    g = input("Guess: ")
    if (int(g) > int(r)):
        print("   Lower!")
    elif(int(g) < int(r)):
        print("   Higher!")
    else:
        print("Good job! That was the number!")
        break
