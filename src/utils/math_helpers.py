from sympy import sympify

def evaluate_expression(expression):
    """
    Evaluates a mathematical expression.
    :param expression: A string containing the mathematical expression.
    :return: The evaluated result.
    """
    result = sympify(expression)
    return result
