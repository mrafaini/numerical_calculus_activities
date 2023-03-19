from newton import newton

def calculate_integral_trapezium_method(f, m, a, b):
    h = (b-a)/m
    
    sum = (1/2)*f(a) + (1/2)*f(b) 
    x_i = a
    for i in range(1, m):
        x_i = x_i + h
        sum += f(x_i)
    return sum*h

def f(x):
    return 105*x**2*(1-x)**4

def F(tau):
    m = 10E4
    return calculate_integral_trapezium_method(f, m, 0, 1) - 0.5
    
    