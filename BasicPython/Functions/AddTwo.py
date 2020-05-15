
#in this case we create a functin which will accept two inputs
def addtwo(a, b):

    added = a + b
    return added

#We ask the user to introduce two values
x = input("Introduce el valor a:")
y = input ("Introduce el valor b:")

#we define the values as floats
fx = float(x)
fy = float(y)

#we call the function print and inside this one our function which will
#add the two values that the user has introduced
print ("a + b = ", addtwo(fx, fy))
