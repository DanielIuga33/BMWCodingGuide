import os
import sys

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt5.QtCore import Qt
from ui_main_window import BMWCodingGuide, get_resource_path
from ui_add_dialog import AddCodingDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMW Coding Guide - Welcome")
        self.setFixedSize(400, 200)

        self.current_language = "ro"  # default

        self.initUI()

    def get_resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def initUI(self):
        layout = QVBoxLayout()

        # Label de welcome
        self.label_welcome = QLabel("Bine ai venit! / Welcome!")
        self.label_welcome.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_welcome)

        # Layout limbi (steaguri)
        lang_layout = QHBoxLayout()
        lang_layout.addStretch()

        self.btn_ro = QPushButton()
        self.btn_ro.setIcon(QIcon(get_resource_path("data/flag_ro.png")))
        self.btn_ro.setIconSize(QSize(29, 29))
        self.btn_ro.setFixedSize(30, 23)
        self.btn_ro.setToolTip("Română")
        self.btn_ro.clicked.connect(self.set_ro_language)

        self.btn_en = QPushButton()
        self.btn_en.setIcon(QIcon(get_resource_path("data/flag_en.png")))
        self.btn_en.setIconSize(QSize(29, 29))
        self.btn_en.setFixedSize(30, 23)
        self.btn_en.setToolTip("English")
        self.btn_en.clicked.connect(self.set_en_language)

        lang_layout.addWidget(self.btn_ro)
        lang_layout.addWidget(self.btn_en)

        # Selectare limbă
        lang_layout = QHBoxLayout()
        lang_layout.addWidget(QLabel("Selectează limba / Choose language:"))

        self.lang_combo = QComboBox()
        self.lang_combo.addItem("Română", "ro")
        self.lang_combo.addItem("English", "en")
        self.lang_combo.currentIndexChanged.connect(self.change_language)

        lang_layout.addWidget(self.lang_combo)
        layout.addLayout(lang_layout)

        # Butoane principale
        self.btn_start = QPushButton("Începe codare")
        self.btn_add = QPushButton("Adaugă o funcție nouă")

        self.btn_start.clicked.connect(self.open_coding_guide)
        self.btn_add.clicked.connect(self.open_add_function)

        layout.addWidget(self.btn_start)
        layout.addWidget(self.btn_add)

        self.setLayout(layout)
        self.update_texts()

    def set_ro_language(self):
        self.current_language = "ro"

    def set_en_language(self):
        self.current_language = "en"

    def change_language(self, index):
        self.current_language = self.lang_combo.currentData()
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
        self.close()

    def open_add_function(self):
        self.add_dialog = AddCodingDialog()
        self.add_dialog.setWindowTitle("Adaugă Codare Nouă" if self.current_language == "ro" else "Add New Coding")
        self.add_dialog.exec_()
