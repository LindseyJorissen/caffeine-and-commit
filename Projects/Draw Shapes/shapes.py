def draw_bottomleft_triangle(height):
    for i in range(height+1):
        print(i * "#\t")
        
def draw_bottomright_triangle(height):
    for i in range(height):
        for j in range(i,height-1):
            print(" ",end="\t")
        for k in range (i+1):
            print("#",end="\t")
        print()

def draw_topleft_triangle(height):
    for i in range(height):
        for j in range(i,height):
            print("#", end="\t")
        print()
        
def draw_topright_triangle(height):
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
