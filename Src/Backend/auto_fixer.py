# auto_fixer.py
import re

class AutoFixer:
    def __init__(self, code):
        """Initializes with the given code."""
        self.code = code

    def fix_indentation(self):
        """Fixes common indentation issues in the code."""
        lines = self.code.splitlines()
        fixed_code = ""
        
        for line in lines:
            # Strip leading/trailing spaces
            line = line.strip()
            fixed_code += line + "\n"

        return fixed_code

    def remove_unused_variables(self):
        """Removes unused variables from the code."""
        # This example assumes a simple approach where we remove variables not used in the code.
        # A more advanced approach would use a linter or static analysis.
        defined_vars = re.findall(r'\b\w+\b', self.code)  # Find all variables defined
        used_vars = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', self.code)  # Find variables used in the code

        # Remove variables not used in the code
        for var in defined_vars:
            if var not in used_vars:
                self.code = self.code.replace(f"{var} = ", "")  # Remove variable assignment

        return self.code

    def fix_syntax_errors(self):
        """Attempt to fix some simple syntax errors."""
        # This is a placeholder for real error fixing. In production, you would integrate with tools
        # like autopep8, black, or other code formatters for Python or Prettier for JavaScript.
        self.code = self.code.replace('print (', 'print(')  # Fixing potential spacing issue in print function (Python example)
        return self.code

    def apply_fixes(self):
        """Apply all fixes to the code."""
        self.code = self.fix_indentation()
        self.code = self.remove_unused_variables()
        self.code = self.fix_syntax_errors()
        return self.code

# Example Usage:
if __name__ == "__main__":
    code_sample = """
    def example():
        x = 10
        y = 20
        z = 30
        print (x)
        return x
    """
    fixer = AutoFixer(code_sample)
    fixed_code = fixer.apply_fixes()
    print("Fixed Code:\n", fixed_code)
