import random

n = int(input("Enter number of times to flip the coin: "))
if n <= 0:
    print("Enter a number")
else:
    heads = 0
    tails = 0

    for i in range(n):
        if random.random() < 0.5:
            heads += 1
        else:
            tails += 1

    head_percentage = (heads / n) * 100
    tail_percentage = (tails / n) * 100

    print("Heads percentage:", head_percentage)
    print("Tails percentage:",tail_percentage)