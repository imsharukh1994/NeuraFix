# issue_detector.py
import os
import re

class IssueDetector:
    def __init__(self, code):
        self.code = code

    def detect_syntax_errors(self):
        """Detects syntax errors in the given code."""
        try:
            compile(self.code, "<string>", "exec")
            return []
        except SyntaxError as e:
            return [{"error": str(e), "line": e.lineno, "column": e.offset}]
    
    def detect_unused_variables(self):
        """Detects unused variables in the code."""
        # This can be improved using static analysis libraries like PyLint
        unused_vars = []
        defined_vars = re.findall(r'\b\w+\b', self.code)
        used_vars = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', self.code)
        
        for var in defined_vars:
            if var not in used_vars:
                unused_vars.append(var)

        return unused_vars

    def run_all_checks(self):
        """Runs all checks to find issues in the code."""
        syntax_errors = self.detect_syntax_errors()
        unused_vars = self.detect_unused_variables()

        issues = {
            "syntax_errors": syntax_errors,
            "unused_variables": unused_vars
        }
        return issues

# Example Usage:
if __name__ == "__main__":
    code_sample = """
    def example():
        x = 10
        return x
    """
    detector = IssueDetector(code_sample)
    issues = detector.run_all_checks()
    print(issues)
