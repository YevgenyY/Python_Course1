import sys 

a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])

# Find discriminant
D = b**2 - (4 * a * c)

#print(D)

x1 = (-b + D**(1/2) ) / (2 * a)
x2 = (-b - D**(1/2) ) / (2 * a)

print( int (x1) )
print( int (x2) )
