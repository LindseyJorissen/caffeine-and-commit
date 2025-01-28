def draw_Lbottom_triangle(height):
    for i in range(height+1):
        print(i * "#\t")
        
def draw_Rbottom_triangle(height):
    for i in range(height):
        for j in range(i,height-1):
            print(" ",end="\t")
        for k in range (i+1):
            print("#",end="\t")
        print()

def draw_Ltop_triangle(height):
    for i in range(height):
        for j in range(i,height):
            print("#", end="\t")
        print()
        
def draw_Rtop_triangle(height):
    for i in range(height):
        for j in range(i):
            print(" ",end="\t")
        for k in range(i,height):
            print("#",end="\t")
        print()       

def draw_square(height):
    for i in range(height):
        for j in range(height):
            print("#",end="  ")
        print()

def draw_rectangle(height,width):
    for i in range(height):
        for j in range(width):
            print("#",end="  ")
        print()
        
def draw_pyramid(height):       
    for i in range(height):
        for j in range(i,height-1):
            print(" ",end=" ")
        for j in range(i):
            print("#",end=" ")
        for j in range(i+1):
            print("#",end=" ")
        print()

def draw_circle(diameter):
    radius = int(diameter/2)
    for y in range(-radius, radius +1):
        for x in range(-radius, radius+1):
            if (x**2 + y**2)**0.5 < radius + 0.5:
                print("# ", end="")
            else:
                print("  ", end="")
        print() 
