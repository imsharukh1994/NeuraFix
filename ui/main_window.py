from PyQt5.QtWidgets import QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel
from modules.compiler import run_code  # Import the run_code function from compiler
from modules.analyzer import analyze_code  # Import the analyze_code function from analyzer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("NeuraFix")
        self.setGeometry(100, 100, 800, 600)  # Position and size of the window
        
        # Create widgets (components)
        self.editor = QPlainTextEdit(self)
        self.editor.setPlaceholderText("Write your code here...")  # Placeholder text in the editor
        
        self.run_button = QPushButton("Run Code", self)
        self.debug_button = QPushButton("Analyze Code", self)
        self.status_label = QLabel("Status: Ready", self)
        
        # Connect buttons to actions (functions)
        self.run_button.clicked.connect(self.run_code)
        self.debug_button.clicked.connect(self.debug_code)
        
        # Layout setup
        layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.debug_button)

        layout.addWidget(self.editor)
        layout.addLayout(button_layout)
        layout.addWidget(self.status_label)

        # Central widget and layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_code(self):
        code = self.editor.toPlainText()  # Get code from the editor
        self.status_label.setText("Status: Running code...")
        
        # Call the compiler's run_code function
        result = run_code(code)
        
        # Update the status with the result
        self.status_label.setText(f"Status: {result}")

    def debug_code(self):
        code = self.editor.toPlainText()  # Get code from the editor
        self.status_label.setText("Status: Analyzing code...")
        
        # Call the analyzer's analyze_code function
        result = analyze_code(code)
        
        # Update the status with the result
        self.status_label.setText(f"Status: {result}")