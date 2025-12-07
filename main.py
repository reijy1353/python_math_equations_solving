from sympy import sympify

def func(x: int, function: str | None = None):
    # If no function is provided, ask the user to enter an expression (will be deprecated soon)
    if function is None:
        equation_str = input("Enter an expression (e.g., x**3 - x**2 + 2): ")
        expr = sympify(equation_str)
    else:
        expr = sympify(function)
    # Substitute the value of x into the expression and return the result
    return expr.subs('x', x)

def get_function():
    equation_str = input("Enter an expression (e.g., x**3 - x**2 + 2): ")
    return equation_str

def bisection(a: int, b: int, epsilon: float = 0.0001):
    """
    This function will solve a math equation using the bisection method.
    """
    function = get_function()
    
    if (func(a, function) * func(b, function) >= 0):
        print("You have not assumed right a and b\n")
        return
    while abs(b-a) >= epsilon:
        c = (a+b)/2
        if func(c, function) == 0.0:
            break
        elif func(c, function)*func(a, function) < 0:
            b = c
        else:
            a = c


print(bisection(0, 1, 0.0001))