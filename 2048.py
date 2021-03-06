import random

"""Generating initial conditions"""
def initials():
    """generating initial numbers"""
    a=2**random.randint(1,2)
    matrix[random.randint(0,order-1)][random.randint(0,order-1)]=2
    while (True):
        x=random.randint(0,order-1)
        y=random.randint(0,order-1)
        if matrix[x][y]==0:
            matrix[x][y]=a
            break

def printing():
    """Printing the matrix"""
    for i in range(order):
        print matrix[i]


"""for generating a number at each step"""
def generate():
    while(True):
        if matrix[random.randint(0,order-1)][random.randint(0,order-1)]==0:
            matrix[random.randint(0,order-1)][random.randint(0,order-1)]=2**random.randint(1,2)
            break



"""Taking keyboard input from user"""
def swipe(score):
    print "\n\nEnter....\n'w' to swipe up\n's' to swipe down\n'a' to swipe left\n'd' to swipe right\n"
    swipe_value=raw_input()
    if swipe_value =='W' or swipe_value=='w':
        up_swipe(score)
    elif swipe_value =='S' or swipe_value=='s':
        down_swipe(score)
    elif swipe_value =='A' or swipe_value=='a':
        left_swipe(score)
    elif swipe_value =='D' or swipe_value=='d':
        right_swipe(score)
    else:
        print "\nPlease enter a valid choice!\n\n"



"""Up swipe function"""
def up_swipe(score):
    for c in range(order):
        for traverse in range(order-1):
            for r in range(order-traverse-1):
                if matrix[c][r]==0 and matrix[c][r+1]!=0:
                    matrix[c][r+1],matrix[c][r]=matrix[c][r],matrix[c][r+1]
    for c in range(order):
        for r in range(order-1):
            if matrix[c][r]==matrix[c][r+1] and matrix[c][r+1]!=0:
                matrix[c][r]=matrix[c][r]+matrix[c][r+1]
                matrix[c][r+1]=0
                score=score+matrix[c][r]
    print "\n"+score
            
    generate()
    printing()


"""Down swipe function"""
def down_swipe(score):
    for c in range(order):
        for traverse in range(order,1,-1):
            for r in range(order-traverse-1,1,-1):
                if matrix[c][r]==0 and matrix[c][r-1]!=0:
                    matrix[c][r-1],matrix[c][r]=matrix[c][r],matrix[c][r-1]
    for c in range(order):
        for r in range(order,1,-1):
            if matrix[c][r]==matrix[c][r-1] and matrix[c][r-1]!=0:
                matrix[c][r]=matrix[c][r]+matrix[c][r-1]
                matrix[c][r-1]=0
                score=score+matrix[c][r]
    print "\n"+score

    generate()
    printing()


"""Left swipe function"""   
def left_swipe(score):
    for r in range(order):
        for traverse in range(order-1):
            for c in range(order-traverse-1):
                if matrix[c][r]==0 and matrix[c+1][r]!=0:
                    matrix[c+1][r],matrix[c][r]=matrix[c][r],matrix[c+1][r]
    for r in range(order):
        for c in range(order-1):
            if matrix[c][r]==matrix[c+1][r] and matrix[c+1][r]!=0:
                matrix[c][r]=matrix[c][r]+matrix[c+1][r]
                matrix[c+1][r]=0
                score=score+matrix[c][r]
    print "\n"+score

    generate()
    printing()


"""Right swipe function"""
def right_swipe(score):
    for r in range(order):
        for traverse in range(order,1,-1):
            for c in range(order-traverse-1,1,-1):
                if matrix[c][r]==0 and matrix[c-1][r]!=0:
                    matrix[c-1][r],matrix[c][r]=matrix[c][r],matrix[c-1][r]
    for r in range(order):
        for c in range(order,1,-1):
            if matrix[c][r]==matrix[c-1][r] and matrix[c-1][r]!=0:
                matrix[c][r]=matrix[c][r]+matrix[c-1][r]
                matrix[c-1][r]=0
                score=score+matrix[c][r]
    print "\n"+score

    generate()
    printing()
    





"""_____________main_______________"""


    
score=0

"""Creating the matrix"""
order=int(input("Enter the matrix size from 3 to 8: "))

while not(order>=3 and order<=8):
    order=int(input("\nWrong Input!!\n\nEnter the matrix size from 3 to 8: "))
matrix=[[0 for column in range(order)] for row in range(order)]
    
while True:
    initials()
    print "\n\n"
    printing()
    swipe(score)
