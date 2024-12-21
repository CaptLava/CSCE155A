import random
T = 'T'
array_of_amphibians = [T] * 15
F = 'F'

for n in range (0,11):
    j = random.randint(0,14)
    array_of_amphibians[j] = (F)
    for amphibians in array_of_amphibians:
        if amphibians == T:
            print("\033[0;32m" + amphibians, end =" ")
        else:
            print("\033[0;31m" + amphibians, end =" ")

    print("\033[0;0m" + "The",j,"th toad turned into a frog!")
