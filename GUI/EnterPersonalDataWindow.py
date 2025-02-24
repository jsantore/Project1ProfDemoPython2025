import sqlite3

from PySide6.QtCore import QRect
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QComboBox, QTextEdit, QPushButton, QHBoxLayout


class PersonalDataWindow(QWidget):
    def __init__(self, cursor: sqlite3.Cursor):
        super().__init__()
        self.cursor = cursor
        self.user_name = None
        self.user_email = None
        self.phone = None
        self.name = None
        self.github = None
        self.other_link = None
        self.projects = None
        self.classes = None
        self.other_info = None
        self.setupWindow()

    def setupWindow(self):
        self.setWindowTitle("Enter Information about yourself")
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Enter profile ID:"))
        self.user_name = QLineEdit()
        main_layout.addWidget(self.user_name)
        main_layout.addWidget(QLabel("Email Address:"))
        self.user_email = QLineEdit()
        main_layout.addWidget(self.user_email)
        main_layout.addWidget(QLabel("Phone Number:"))
        self.phone = QLineEdit()
        main_layout.addWidget(self.phone)
        main_layout.addWidget(QLabel("Full Name:"))
        self.name = QLineEdit()
        main_layout.addWidget(self.name)
        main_layout.addWidget(QLabel("Github/Gitlab/bitbucket Link:"))
        self.github = QLineEdit()
        main_layout.addWidget(self.github)
        main_layout.addWidget(QLabel("Other Link:"))
        self.other_link = QLineEdit()
        main_layout.addWidget(self.other_link)
        main_layout.addWidget(QLabel("Projects:"))
        self.projects = QTextEdit()
        main_layout.addWidget(self.projects)
        main_layout.addWidget(QLabel("Classes:"))
        self.classes = QTextEdit()
        main_layout.addWidget(self.classes)
        main_layout.addWidget(QLabel("Other Info:"))
        self.other_info = QTextEdit()
        main_layout.addWidget(self.other_info)
        bottom_row = QHBoxLayout()
        save_button = QPushButton("Save")
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.back)
        bottom_row.addWidget(save_button)
        bottom_row.addWidget(back_button)
        main_layout.addLayout(bottom_row)
        self.set_size()
        self.setLayout(main_layout)



    def back(self):
        self.close()

    # this function was originally generated by Gemini but that version only
    # made the window full height but half width, so I modified it to do 2/3 height
    def set_size(self):
        screen = QGuiApplication.primaryScreen()
        available_geometry = screen.availableGeometry()
        width = available_geometry.width()
        height = available_geometry.height()
        self.setGeometry(
            QRect(width // 10, height // 10, width // 4, (height // 3) * 2)
        )  # Set size to quarter width, 2/3 height, positioned just off top-left

