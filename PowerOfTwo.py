N = int(input("Enter the value of N: "))

if N < 0 or N >= 31:
    print("Enter a value: ")
else:
    i = 0
    power = 1 
    
    while i <= N:
        print("2^", i, "=", power)
        power = power * 2
        i = i + 1