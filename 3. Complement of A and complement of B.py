# 3. Complement of A and complement of B

## Formula :

# complement_of_A = 1 - A

# complement_of_B = 1 - B

# where A and B are fuzzy sets

A = dict()
B = dict()
X = dict()
Y = dict()

A = {"a": 1, "b": 0.3, "c": 0.5, "d": 0.2 }
B = {"a": 0.5, "b": 0.4, "c": 0.1, "d": 1 }

print('The Fuzzy Set is :', A)
print('The Fuzzy Set is :', B)

for i,j in zip(A,B):
     X[i] = 1 - A[i]
     Y[j] = 1 - B[j]
 
print('Fuzzy Set Complement A is :', X)
print('Fuzzy Set Complement B is :', Y)
