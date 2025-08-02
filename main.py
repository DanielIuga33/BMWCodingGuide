import sys
import os
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QTextEdit, QHBoxLayout
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class BMWCodingGuide(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMW Coding Guide")
        self.current_language = "ro"
        self.setFixedSize(600, 450)

        # Încarcă datele JSON
        json_path = get_resource_path(os.path.join("data", "bmw_codari.json"))
        with open(json_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # Layout pentru limbi (buton cu steaguri în dreapta sus)
        lang_layout = QHBoxLayout()
        lang_layout.addStretch()  # împinge butoanele spre dreapta

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
        self.btn_ro.setIcon(QIcon(get_resource_path("data/flag_ro.png")))
        self.btn_en.setIcon(QIcon(get_resource_path("data/flag_en.png")))

        main_layout.addLayout(lang_layout)

        # Restul UI-ului
        self.model_label = QLabel("Model BMW:")
        self.model_combo = QComboBox()
        self.model_combo.addItem("Alege model")
        self.model_combo.addItems(self.data.keys())
        self.model_combo.setCurrentIndex(0)
        self.model_combo.currentTextChanged.connect(self.update_module)

        self.modul_label = QLabel("Modul:")
        self.modul_combo = QComboBox()
        self.modul_combo.currentTextChanged.connect(self.update_functii)

        self.functie_label = QLabel("Funcție:")
        self.functie_combo = QComboBox()

        self.show_button = QPushButton("Afișează Instrucțiuni")
        self.show_button.clicked.connect(self.show_instructions)

        self.instructiuni_box = QTextEdit()
        self.instructiuni_box.setReadOnly(True)

        main_layout.addWidget(self.model_label)
        main_layout.addWidget(self.model_combo)
        main_layout.addWidget(self.modul_label)
        main_layout.addWidget(self.modul_combo)
        main_layout.addWidget(self.functie_label)
        main_layout.addWidget(self.functie_combo)
        main_layout.addWidget(self.show_button)
        main_layout.addWidget(self.instructiuni_box)

        self.setLayout(main_layout)

        # Inițializare selecție
        self.update_module(self.model_combo.currentText())

    def update_model_language_ui(self):
        self.model_combo.clear()
        if self.current_language == "ro":
            self.model_combo.addItem("Alege model")
        else:
            self.model_combo.addItem("Choose model")
        self.model_combo.addItems(self.data.keys())
        self.model_combo.setCurrentIndex(0)

    def set_ro_language(self):
        self.current_language = "ro"
        self.update_ui_language()

    def set_en_language(self):
        self.current_language = "en"
        self.update_ui_language()

    def update_ui_language(self):
        self.instructiuni_box.clear()
        self.update_model_language_ui()
        if self.current_language == "ro":
            self.model_label.setText("Model BMW:")
            self.modul_label.setText("Modul:")
            self.functie_label.setText("Funcție:")
            self.show_button.setText("Afișează Instrucțiuni")
        else:
            self.model_label.setText("BMW Model:")
            self.modul_label.setText("Module:")
            self.functie_label.setText("Function:")
            self.show_button.setText("Show Instructions")
        return
        self.update_module(self.model_combo.currentText())

        self.show_instructions()  # Reafișează instrucțiunile în limba nouă

    def update_module(self, model):
        self.modul_combo.clear()
        if self.current_language == "ro":
            self.modul_combo.addItem("Alege modul")
        else:
            self.modul_combo.addItem("Choose module")
        if model in self.data:
            self.modul_combo.addItems(self.data[model].keys())
        self.modul_combo.setCurrentIndex(0)
        self.update_functii(self.modul_combo.currentText())

    def update_functii(self, modul):
        self.functie_combo.clear()
        if self.current_language == "ro":
            self.functie_combo.addItem("Alege funcție")
        else:
            self.functie_combo.addItem("Choose function")
        model = self.model_combo.currentText()
        if model in self.data and modul in self.data[model]:
            self.functie_combo.addItems(self.data[model][modul].keys())
        self.functie_combo.setCurrentIndex(0)

    def show_instructions(self):
        model = self.model_combo.currentText()
        modul = self.modul_combo.currentText()
        functie = self.functie_combo.currentText()

        if model == "Alege model" or modul == "Alege modul" or functie == "Alege funcție":
            self.instructiuni_box.clear()
            return

        instructiuni = self.data[model][modul][functie]
        tool = instructiuni.get("tool", {}).get(self.current_language, "N/A")
        pasi = instructiuni.get("pasii", {}).get(self.current_language, [])

        text = f"Instrument recomandat: {tool}\n\n"
        for i, pas in enumerate(pasi, 1):
            text += f"{i}. {pas}\n"

        self.instructiuni_box.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMWCodingGuide()
    window.show()
    sys.exit(app.exec_())
