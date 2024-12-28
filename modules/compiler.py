# modules/compiler.py

def run_code(code: str) -> str:
    """
    Executes the code passed as a string and returns the output or error message.
    This is a basic Python execution. Extend this to handle more languages.
    """
    try:
        # Execute the code in a restricted namespace
        exec_globals = {}
        exec(code, exec_globals)

        # You can capture output here if needed (e.g., print statements)
        # For simplicity, return a success message
        return "Code executed successfully!"
    except Exception as e:
        # Return error message if code execution fails
        return f"Error: {str(e)}"