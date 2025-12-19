def check_Prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
        
n = int(input("Enter a value: "))
print("Prime factors of ", n," are: ")
for i in range(2,n+1):
    if(n%i==0):
        if check_Prime(i):
            print(i," ")