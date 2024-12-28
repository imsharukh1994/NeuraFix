import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main_window import MainWindow  # Importing the MainWindow class from the UI module

def main():
    # Initialize the QApplication
    app = QApplication(sys.argv)

    # Create an instance of the MainWindow class (the GUI)
    window = MainWindow()

    # Show the main window
    window.show()

    # Execute the application (start the event loop)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()