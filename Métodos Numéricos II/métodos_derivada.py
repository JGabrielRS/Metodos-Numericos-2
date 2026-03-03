def f(x):
    return x**2 + 3*x + 5

def derivada_foward(x, delta):
    return (f(x + delta) - f(x))/delta

def derivada_backward(x, delta):
    return (f(x) - f(x - delta))/delta

def derivada_central(x, delta):
    return (f(x + delta) - f(x - delta))/(2*delta)

x = 50
delta = 0.01
print(derivada_foward(x,delta)) 
print(derivada_backward(x,delta))
print(derivada_central(x, delta))