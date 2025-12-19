N = int(input("Enter the value of N: "))

if N == 0:
    print("N should be greater than zero")
else:
    harmonic = 0.0

    for i in range(1, N + 1):
        harmonic = harmonic + (1 / i)

    print("Nth Harmonic Value:", harmonic)