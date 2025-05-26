import sys
from hashlib import QApplication
from ui.main_window import MainWindow  # Importing the MainWindow class from the UI module
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QSplashScreen
import time

def main():
    # Initialize the QApplication
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("path/to/icon.png"))  # Set your app icon

    splash = QSplashScreen(QPixmap("path/to/splash.png"))
    splash.show()
    app.processEvents()
    # Simulate loading
    time.sleep(2)
    # Create an instance of the MainWindow class (the GUI)
    window = MainWindow()
    splash.finish(window)
    # Show the main window
    window.show()

    # Execute the application (start the event loop)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()