def multiplication_table(x):
    """prints out a multiplication table for the numbers 1 through x"""
    for i in range(1,x+1):
        for j in range(1,x+1):
            print(i*j,end="\t")
        print()
multiplication_table(10)