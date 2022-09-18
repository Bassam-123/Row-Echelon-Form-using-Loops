# Python code that reduces a Matrix into its Row Echelon Form and finds the rank of the matrix.

import numpy as np

r = int(input('Enter the number of rows: '))
c = int(input('Enter the number of columns: '))
print('Enter',r,'x',c,'Matrix:')
elements = list(map(int, input().split()))  
  
A = np.array(elements).reshape(r,c)  # Printing the matrix given by the user
print(A) 

B = np.array(A,dtype=np.float_)      # Taking B as a copy of A, because we are going to alter it's values.

# If all the elements in a column is 0, we perform REF on next column 
def row_echelon(B):
    for m in range(c-1):
        for n in range(m+1,r):
            if B[m,m+1] != 0:
                B[n] =- (B[n,m+1]/B[m,m+1]) * B[m,:] + B[n,:]
                
    return B

# Function to rearrange the Matrix by performing row interchange operation.
def rearr(A):
    for m in range(i,c):
        for n in range(m+1,r):
            flag = False
            if A[n,m] != 0:
                A[[n,i]] = A[[i,n]] 
                flag = True
                break
        if flag == True:
            break
    return A

# Function to find the rank of the Matrix.
def rankfind (B): 
    rank = 0
    for r in range(len(B)):
        for c in range(len(B[0])):
            if B[r,c] != 0:
                rank += 1
                break
                
    return rank

# Perform REF on Input Matrix
for i in range(c-1):
    for j in range(i+1,r):
        if B[i,i] != 0:
            B[j,:] =-(B[j,i]/B[i,i]) * B[i,:] + B[j,:]
            
        else :
            rearr(B)                 # Function is called when pivot element is 0 
            if (B[i,i] == 0):
                row_echelon(B)       # Function is called if pivot element is still 0 after row interchange
            else:
                break

print("\nThe Row Echelon Form is:")
print(B)   
rank = rankfind(B)
print('The Rank is: ',rank)                
