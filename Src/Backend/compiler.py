# compiler.py
import subprocess

class Compiler:
    def __init__(self, code, language="python"):
        """Initializes the compiler with the given code and language."""
        self.code = code
        self.language = language

    def compile_code(self):
        """Compiles or runs the given code."""
        if self.language == "python":
            return self.run_python_code()
        elif self.language == "javascript":
            return self.run_javascript_code()
        else:
            return {"success": False, "error": f"Unsupported language: {self.language}"}

    def run_python_code(self):
        """Executes Python code using subprocess."""
        try:
            # Using subprocess to execute the Python code in a new process
            result = subprocess.run(
                ["python3", "-c", self.code],  # Executes the Python code
                capture_output=True,            # Captures the output
                text=True                       # Returns output as a string (not bytes)
            )

            # Returns the result (stdout and stderr)
            if result.returncode == 0:
                return {"success": True, "output": result.stdout.strip()}
            else:
                return {"success": False, "error": result.stderr.strip()}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def run_javascript_code(self):
        """Executes JavaScript code using Node.js and subprocess."""
        try:
            # Using subprocess to execute JavaScript code via Node.js
            result = subprocess.run(
                ["node", "-e", self.code],  # Executes JavaScript code with Node.js
                capture_output=True,         # Captures the output
                text=True                    # Returns output as a string
            )

            # Returns the result (stdout and stderr)
            if result.returncode == 0:
                return {"success": True, "output": result.stdout.strip()}
            else:
                return {"success": False, "error": result.stderr.strip()}
        except Exception as e:
            return {"success": False, "error": str(e)}

# Example Usage:
if __name__ == "__main__":
    code_sample_python = "print('Hello, world!')"
    compiler_python = Compiler(code_sample_python, language="python")
    result_python = compiler_python.compile_code()
    print("Python Compilation Result:", result_python)

    code_sample_js = "console.log('Hello from JavaScript!')"
    compiler_js = Compiler(code_sample_js, language="javascript")
    result_js = compiler_js.compile_code()
    print("JavaScript Compilation Result:", result_js)
