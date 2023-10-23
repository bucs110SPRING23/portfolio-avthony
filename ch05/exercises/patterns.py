

def star_pyramid():
    for i in range(amount):
        print("*"*(amount - i))
        
        
def star_pyramidr():
    for i in range(amount+1):
        print("*"*(i))

amount = int(input("pleases enter the amount of stars you want to print "))

star_pyramidr()
star_pyramid()