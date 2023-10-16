

def star_pyramid():
    star = "*"
    for i in range(amount):
        print(star*(amount - i))
        
        
def star_pyramidr():
    star = "*"
    for i in range(amount+1):
        print(star*(i))

amount = int(input("pleases enter the amount of stars you want to print "))

star_pyramid()
star_pyramidr()