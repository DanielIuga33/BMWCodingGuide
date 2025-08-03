import os
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from ui_main_window import BMWCodingGuide
from ui_add_dialog import AddCodingDialog


def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        icon_path = get_resource_path("data/icon_bmw.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle("BMW Coding Guide - Welcome")
        self.setFixedSize(600, 300)
        self.setStyleSheet("background-color: hsl(0, 0%, 25%); color: #e4e4e4;")

        self.current_language = "ro"  # implicit

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 🔹 Steaguri sus-dreapta
        flag_layout = QHBoxLayout()
        flag_layout.addStretch()

        self.btn_ro = QPushButton()
        self.btn_ro.setIcon(QIcon(get_resource_path("data/flag_ro.png")))
        self.btn_ro.setIconSize(QSize(29, 29))
        self.btn_ro.setFixedSize(30, 23)
        self.btn_ro.setToolTip("Română")
        self.btn_ro.clicked.connect(lambda: self.set_language("ro"))

        self.btn_en = QPushButton()
        self.btn_en.setIcon(QIcon(get_resource_path("data/flag_en.png")))
        self.btn_en.setIconSize(QSize(29, 29))
        self.btn_en.setFixedSize(30, 23)
        self.btn_en.setToolTip("English")
        self.btn_en.clicked.connect(lambda: self.set_language("en"))

        flag_layout.addWidget(self.btn_ro)
        flag_layout.addWidget(self.btn_en)

        layout.addLayout(flag_layout)

        # 🔹 Mesaj de bun venit
        # self.label_welcome = QLabel()
        # self.label_welcome.setAlignment(Qt.AlignCenter)
        # layout.addWidget(self.label_welcome)

        welcome_layout = QHBoxLayout()
        welcome_layout.setAlignment(Qt.AlignLeft)

        self.icon_label = QLabel()
        icon_path = get_resource_path("data/BMW_welcome3.png")  # imaginea ta
        self.icon_label.setPixmap(QIcon(icon_path).pixmap(128, 128))  # dimensiune ajustabilă
        self.icon_label.setContentsMargins(50, 0, 60, 0)  # margine stânga/sus/dreapta/jos

        self.label_welcome = QLabel()
        self.label_welcome.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.label_welcome.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        welcome_layout.addWidget(self.icon_label)
        welcome_layout.addWidget(self.label_welcome)

        layout.addLayout(welcome_layout)

        # 🔹 Butoane principale
        self.btn_start = QPushButton()
        self.btn_add = QPushButton()


        self.btn_start.clicked.connect(self.open_coding_guide)
        self.btn_add.clicked.connect(self.open_add_function)

        layout.addWidget(self.btn_start)
        layout.addWidget(self.btn_add)

        self.setLayout(layout)
        self.update_texts()

        self.btn_start.setStyleSheet("font-size: 14px; font-weight: 20; height: 35px")
        self.btn_add.setStyleSheet("font-size: 14px; font-weight: 20; height: 35px")

    def set_language(self, lang_code):
        self.current_language = lang_code
        self.update_texts()

    def update_texts(self):
        if self.current_language == "ro":
            self.label_welcome.setText("Bine ai venit!")
            self.btn_start.setText("Începe codare")
            self.btn_add.setText("Adaugă o funcție nouă")
        else:
            self.label_welcome.setText("Welcome!")
            self.btn_start.setText("Start Coding")
            self.btn_add.setText("Add New Function")

    def open_coding_guide(self):
        self.coding_guide_window = BMWCodingGuide(self.current_language)
        self.coding_guide_window.current_language = self.current_language
        self.coding_guide_window.update_ui_language()
        self.coding_guide_window.show()

    def open_add_function(self):
        self.add_dialog = AddCodingDialog(self.current_language)
        self.add_dialog.setWindowTitle("Adaugă Codare Nouă" if self.current_language == "ro" else "Add New Coding")
        self.add_dialog.exec_()
