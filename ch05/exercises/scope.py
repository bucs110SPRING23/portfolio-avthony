
def multiplication(x):
    multiplier = int(input("what would you like to multiply your number by: "))
    accum = x
    for _ in range(multiplier):
        x = x + accum
    return(x)

def exponent():
    x = 0
    
def square():
    x = 0

 
main_Num = int(input("Please enter the number you would like to use: "))

mult = multiplication(main_Num)
print(mult)