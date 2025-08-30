import sys
import os
import json

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QTextEdit, QMessageBox
)

from ui_add_dialog import get_resource_path


class BMWCodingGuide(QWidget):
    def __init__(self, language):
        super().__init__()
        icon_path = get_resource_path("data/icon_bmw.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle("BMW Coding Guide")
        self.current_language = language
        self.setFixedSize(600, 750)
        self.setStyleSheet("background-color: hsl(0, 0%, 25%); color: #e4e4e4;")

        # try:
        #     self.json_path = get_resource_path(os.path.join("data", "bmw_codari.json"))
        #     with open(self.json_path, "r", encoding="utf-8") as f:
        #         self.data = json.load(f)
        # except Exception as e:
        #     QMessageBox.critical(self, "Error ", str(e))
        #     QMessageBox.information(self, "Error ", "Eroare cauzata din cauza lipsei de date" if
        #     self.current_language == "ro" else "Error may be caused due to the lack of data")
        #     return

        try:
            self.json_path = get_resource_path("data/bmw_codari.json")
            with open(self.json_path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except Exception as e:
            QMessageBox.critical(self, "Error ", str(e))
            QMessageBox.information(self, "Error ", "Eroare cauzata din cauza lipsei de date" if
            self.current_language == "ro" else "Error may be caused due to the lack of data")
            return

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.model_label = QLabel()
        self.model_label.setStyleSheet("font-size: 12px; font-weight: 20")
        self.model_combo = QComboBox()
        self.model_combo.currentTextChanged.connect(self.update_fabricatie)
        self.model_combo.setStyleSheet("font-size: 12px; font-weight: 15; height: 30px")

        self.fabricatie_label = QLabel()
        self.fabricatie_label.setStyleSheet("font-size: 12px; font-weight: 20")
        self.fabricatie_combo = QComboBox()
        self.fabricatie_combo.currentTextChanged.connect(self.update_module)
        self.fabricatie_combo.setStyleSheet("font-size: 12px; font-weight: 15; height: 30px")

        self.modul_label = QLabel()
        self.modul_label.setStyleSheet("font-size: 12px; font-weight: 20")
        self.modul_combo = QComboBox()
        self.modul_combo.currentTextChanged.connect(self.update_functii)
        self.modul_combo.setStyleSheet("font-size: 12px; font-weight: 15; height: 30px")

        self.functie_label = QLabel()
        self.functie_label.setStyleSheet("font-size: 12px; font-weight: 20")
        self.functie_combo = QComboBox()
        self.functie_combo.setStyleSheet("font-size: 12px; font-weight: 15; height: 30px")

        self.show_button = QPushButton()
        self.show_button.clicked.connect(self.show_instructions)
        self.show_button.setStyleSheet("margin-top: 20px; font-size: 14px; font-weight: 20;"
                                       " height: 30px;background-color: hsl(0, 0%, 22%); border: 1px solid black;")

        self.instructiuni_box = QTextEdit()
        self.instructiuni_box.setReadOnly(True)

        layout.addWidget(self.model_label)
        layout.addWidget(self.model_combo)
        layout.addWidget(self.fabricatie_label)
        layout.addWidget(self.fabricatie_combo)
        layout.addWidget(self.modul_label)
        layout.addWidget(self.modul_combo)
        layout.addWidget(self.functie_label)
        layout.addWidget(self.functie_combo)
        layout.addWidget(self.show_button)
        layout.addWidget(self.instructiuni_box)

        self.setLayout(layout)
        self.update_ui_language()

    def update_ui_language(self):
        if self.current_language == "ro":
            self.model_label.setText("Model BMW:")
            self.fabricatie_label.setText("Fabricație:")
            self.modul_label.setText("Modul:")
            self.functie_label.setText("Funcție:")
            self.show_button.setText("Afișează Instrucțiuni")
            self.model_combo.clear()
            self.model_combo.addItem("Alege model")
        else:
            self.model_label.setText("BMW Model:")
            self.fabricatie_label.setText("Manufacture Year:")
            self.modul_label.setText("Module:")
            self.functie_label.setText("Function:")
            self.show_button.setText("Show Instructions")
            self.model_combo.clear()
            self.model_combo.addItem("Choose model")

        self.model_combo.addItems(self.data.keys())
        self.update_fabricatie(self.model_combo.currentText())

    def update_fabricatie(self, model):
        self.fabricatie_combo.clear()
        if self.current_language == "ro":
            self.fabricatie_combo.addItem("Alege fabricație")
        else:
            self.fabricatie_combo.addItem("Choose manufacture year")

        if model in self.data:
            self.fabricatie_combo.addItems(self.data[model].keys())
        self.update_module()

    def update_module(self, _=None):
        self.modul_combo.clear()
        if self.current_language == "ro":
            self.modul_combo.addItem("Alege modul")
        else:
            self.modul_combo.addItem("Choose module")

        model = self.model_combo.currentText()
        fabricatie = self.fabricatie_combo.currentText()

        if model in self.data and fabricatie in self.data[model]:
            self.modul_combo.addItems(self.data[model][fabricatie].keys())

        self.update_functii()

    def update_functii(self, _=None):
        self.functie_combo.clear()
        if self.current_language == "ro":
            self.functie_combo.addItem("Alege funcție")
        else:
            self.functie_combo.addItem("Choose function")

        model = self.model_combo.currentText()
        fabricatie = self.fabricatie_combo.currentText()
        modul = self.modul_combo.currentText()

        if (
                model in self.data
                and fabricatie in self.data[model]
                and modul in self.data[model][fabricatie]
        ):
            self.functie_combo.addItems(self.data[model][fabricatie][modul].keys())

    def show_instructions(self):
        model = self.model_combo.currentText()
        fabricatie = self.fabricatie_combo.currentText()
        modul = self.modul_combo.currentText()
        functie = self.functie_combo.currentText()

        if any(x.startswith(("Alege", "Choose")) for x in [model, fabricatie, modul, functie]):
            self.instructiuni_box.clear()
            return

        try:
            instructiuni = self.data[model][fabricatie][modul][functie]
        except KeyError:
            self.instructiuni_box.setText("Instrucțiuni indisponibile.")
            return

        tool_data = instructiuni.get("tool", "N/A")
        if isinstance(tool_data, dict):
            tool = tool_data.get(self.current_language, "N/A")
        else:
            tool = tool_data

        pasi = instructiuni.get("pasii", {}).get(self.current_language, [])

        if self.current_language == "ro":
            text = f"Instrument recomandat: {tool}\n\n"
        else:
            text = f"Recommended tool: {tool}\n\n"

        for i, pas in enumerate(pasi, 1):
            text += f"{i}. {pas}\n"

        self.instructiuni_box.setText(text)
