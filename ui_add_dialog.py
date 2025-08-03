import json
import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton, QTextEdit, QComboBox
from PyQt5.QtWidgets import QMessageBox
from setuptools.config.pyprojecttoml import validate

from data_validator import DataValidator
from utils import bmw_models


def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class AddCodingDialog(QDialog):
    def __init__(self, language, parent=None):
        super().__init__(parent)
        self.language = language
        icon_path = get_resource_path("data/icon_bmw.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle("Adaugă Codare Nouă" if language == "ro" else "Add New Coding")
        self.setStyleSheet("background-color: hsl(0, 0%, 25%); color: #e4e4e4;")
        self.setFixedSize(500, 700)

        layout = QVBoxLayout()

        self.model_combo = QComboBox()
        self.fabricatie_input = QLineEdit()
        self.module_input = QLineEdit()
        self.function_input = QLineEdit()
        self.tool_input = QLineEdit()
        self.pasi_ro_input = QTextEdit()
        self.pasi_en_input = QTextEdit()

        self.model_combo.setStyleSheet("font-size: 14px; font-weight: 20; height: 22px")
        self.module_input.setStyleSheet("font-size: 14px; font-weight: 20; height: 22px")
        self.function_input.setStyleSheet("font-size: 14px; font-weight: 20; height: 22px")
        self.fabricatie_input.setStyleSheet("font-size: 14px; font-weight: 20; height: 22px")
        self.tool_input.setStyleSheet("font-size: 14px; font-weight: 20; height: 22px")
        self.pasi_en_input.setStyleSheet("font-size: 12px; font-weight: 20")
        self.pasi_ro_input.setStyleSheet("font-size: 12px; font-weight: 20")

        # Labels text in both languages
        labels_ro = {
            "model": "Model",
            "module": "Modul",
            "function": "Funcție",
            "fabricatie": "Perioadă fabricație",
            "tool": "Tool",
            "pasi_ro": "Pași RO (fiecare pe linie nouă)",
            "pasi_en": "Pași EN (fiecare pe linie nouă)",
            "save": "Salvează"
        }
        labels_en = {
            "model": "Model",
            "module": "Module",
            "function": "Function",
            "fabricatie": "Manufacturing Period",
            "tool": "Tool",
            "pasi_ro": "Steps RO (one per line)",
            "pasi_en": "Steps EN (one per line)",
            "save": "Save"
        }

        labels = labels_ro if self.language == "ro" else labels_en
        layout.addWidget(QLabel(labels["model"]))
        layout.addWidget(self.model_combo)
        if self.language == "ro":
            self.model_combo.addItem("Alege modelul")
        else:
            self.model_combo.addItem("Choose model")
        self.model_combo.addItems(sorted(bmw_models))
        self.model_combo.setCurrentIndex(0)
        layout.addWidget(QLabel(labels["fabricatie"]))
        layout.addWidget(self.fabricatie_input)
        layout.addWidget(QLabel(labels["module"]))
        layout.addWidget(self.module_input)
        layout.addWidget(QLabel(labels["function"]))
        layout.addWidget(self.function_input)
        layout.addWidget(QLabel(labels["tool"]))
        layout.addWidget(self.tool_input)
        layout.addWidget(QLabel(labels["pasi_ro"]))
        layout.addWidget(self.pasi_ro_input)
        layout.addWidget(QLabel(labels["pasi_en"]))
        layout.addWidget(self.pasi_en_input)

        QLabel.setStyleSheet(self, "background-color: hsl(0, 0%, 25%); color: #e4e4e4;"
                                   " font-size: 14px; font-weight: 20")

        btn_save = QPushButton(labels["save"])
        btn_save.clicked.connect(self.save_data_to_file)
        layout.addWidget(btn_save)

        self.setLayout(layout)

    def get_data(self):
        return {
            "model": self.model_combo.currentText(),
            "modul": self.module_input.text().strip(),
            "functie": self.function_input.text().strip(),
            "fabricatie": self.fabricatie_input.text().strip(),
            "tool": self.tool_input.text().strip(),
            "pasi_ro": [line.strip() for line in self.pasi_ro_input.toPlainText().splitlines() if line.strip()],
            "pasi_en": [line.strip() for line in self.pasi_en_input.toPlainText().splitlines() if line.strip()]
        }

    def save_data_to_file(self):
        data = self.get_data()

        try:
            DataValidator.validate(self.language, data["functie"], data["tool"], data["pasi_ro"], data["pasi_en"])
        except Exception as e:
            QMessageBox.information(self, "Eroare: " if self.language == "ro" else "Error:", str(e))
            return
        filepath = os.path.join("data", "bmw_codari.json")

        model = data["model"]
        fabricatie = data["fabricatie"]
        modul = data["modul"]
        functie = data["functie"]

        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Încarcă fișierul existent (sau creează structura nouă)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    json_data = json.load(f)
                except json.JSONDecodeError:
                    json_data = {}
        else:
            json_data = {}

        # Asigură existența structurii: model > fabricatie > modul
        if model not in json_data:
            json_data[model] = {}
        if fabricatie not in json_data[model]:
            json_data[model][fabricatie] = {}
        if modul not in json_data[model][fabricatie]:
            json_data[model][fabricatie][modul] = {}

        # Adaugă funcția
        json_data[model][fabricatie][modul][functie] = {
            "tool": data["tool"],
            "pasii": {
                "ro": data["pasi_ro"],
                "en": data["pasi_en"]
            }
        }

        # Scrie înapoi în fișier
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

        msg_text = "Codarea a fost salvată cu succes!" if self.language == "ro" else "Coding was saved successfully!"
        QMessageBox.information(self, "Succes" if self.language == "ro" else "Success", msg_text)
        self.accept()
