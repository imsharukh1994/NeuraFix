def run_code(code: str) -> str:
    """
    Executes the code passed as a string and returns the output or error message.
    This is a basic Python execution. Extend this to handle more languages.
    """
    import io
    import sys

    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()

    try:
        # Execute the code in a restricted namespace
        exec_globals = {}
        exec(code, exec_globals)

        # Get the output from the redirected stdout
        output = redirected_output.getvalue()
        return output if output else "Code executed successfully!"
    except Exception as e:
        # Return error message if code execution fails
        return f"Error: {str(e)}"
    finally:
        # Restore stdout
        sys.stdout = old_stdout