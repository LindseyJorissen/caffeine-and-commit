def bottomleft_triangle():
    height = int(input("Height: \n"))
    for i in range(height+1):
        print(i * "#\t")
        
def bottomright_triangle():
    height = int(input("Height: \n"))
    for i in range(height):
        for j in range(i,height-1):
            print(" ",end="\t")
        for k in range (i+1):
            print("#",end="\t")
        print()

def topleft_triangle():
    height = int(input("Height: \n"))
    for i in range(height):
        for j in range(i,height):
            print("#", end="\t")
        print()
        
def topright_triangle():
    height = int(input("Height: \n"))
    for i in range(height):
        for j in range(i):
            print(" ",end="\t")
        for k in range(i,height):
            print("#",end="\t")
        print()
