#   HW2 Assignment 
#   Author: Ryan Ferrin 
#   Save this file as RYAN-FERRIN-HW1.py

# 1) -1 print 2 n x m rectangles with "*"
#    -2 print a crntered triangle of height n with "*"

# function for printing "*" row of length n
def row(n):
    #base case number of columns
    if n<1:
        return
    # print '*" leave cursor on line
    print('*', end= "")
    row(n-1)  
    
#function to print 2 ea. m rows of column n
def rectangle(n, m):
    # base case number of rows
    if m<1:
        return

    row(n)
    print(end=" ")
    row(n)
    print()
    rectangle(n, m-1)

rectangle(4, 6)

# print a cented triangle of hieght n with "*"
def triangle(n):
    # in case non-positive integer is given
    if n<1:
        return
    i=0 # iteration counter
    j=1 # starting row
    k=n-1 #number of spaces
    
    
    #loop to get number of rows
    for i in range(n):
        # loop for leading spaces
        for h in range(k):
            print(end=' ')
        # print row
        row(j)
        print()
        #increment counters
        k -= 1 
        j += 2
        i += 1 
    
triangle(6)

# 2) create a function that removes repeated values from a list.
#    original list is to remain unchanged and a new list is created

def clean1(alist):

    # define temporary empty list, tmp
    tmp = []
    
    #add unique value from alist to tmp
    for i in range(len(alist)):
        if alist[i] not in tmp:
            tmp.append(alist[i])
    return tmp

a1 = [1,2,3,4,4,4,5,1,2,1,5]
newlist = clean1(a1)
print(a1)
print(newlist)

# 3) create a funtion that modifies a list to remove repeated values.
#    original list is modified

def clean2(alist):

    i=0
    match = True
    while match:
        if alist[i] in alist[i+1:len(alist)]:
            del alist[i]
            match = True
        else:
            i += 1
            if i == len(alist):
                match = False
        
print(a1)
clean2(a1)
print(a1)

# 4) write a function that takes a list and returns
#    a string of elements that are a power of 2

def fct(alist):

    even=[]
    
    for i in range(len(alist)):
        if alist[i] % 2 == 0 and alist[i] != 0:
            even.append(alist[i])
       
    print('These element of the given list are a power of 2 ' + str(even))

a2 = [1, 2, 3, 4, 5, 16, 255, 256, -1, -2, 84]
fct(a2)
