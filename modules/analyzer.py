# modules/analyzer.py

import ast

def analyze_code(code: str) -> str:
    """
    Analyzes the code for syntax errors. Returns a message indicating if the code is valid or contains errors.
    """
    try:
        # Parse the code into an abstract syntax tree (AST) to check for syntax errors
        ast.parse(code)
        return "Code is syntactically correct."
    except SyntaxError as e:
        return f"Syntax error: {e.msg} at line {e.lineno}"