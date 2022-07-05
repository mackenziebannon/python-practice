# test file to try using functions

def myFunc(x):
    return x*x

print(myFunc(5))

# github copilot testing 

def cube(x):
    return x*x*x

def volume(x,y,z):
    return x*y*z
  
def circumference(x):
    return 2*x*3.14
  
def area(x):
    return x*x*3.14

def average(x,y):
    return (x+y)/2
  
def average(x,y,z):
    return (x+y+z)/3
  
def avg(x, *y):
    return (x+sum(y))/len(y)

def grades(*y):
    return sum(y)/len(y)

def gradeletter(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    elif x >= 60:
        return "D"
    else:
        return "F"
      

def gradegpa(x):
    if x >= 90:
        return 4.0
    elif x >= 80:
        return 3.0
    elif x >= 70:
        return 2.0
    elif x >= 60:
        return 1.0
    else:
        return 0.0
      
def roots(x,y):
    return x**0.5, y**0.5
  
def quadratic(x,y,z):
    return x**2+y**2+z**2

def absolute(x):
    if x < 0:
        return -x
    else:
        return x

def regex(x):
    return x.replace("a","b")

def random(x):
    return x*random.random()

def dictionary(x):
    return x.upper()

