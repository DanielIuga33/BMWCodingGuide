import json
import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton, QTextEdit, QComboBox
from PyQt5.QtWidgets import QMessageBox
from sqlalchemy.orm.sync import update

from data_validator import DataValidator
from utils import bmw_models, get_bmw_years_intervals, get_modules_by_model_and_year, \
    bmw_modules_db, get_resource_path, get_writable_json_path


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
        self.fabricatie_combo = QComboBox()
        self.module_combo = QComboBox()
        self.function_input = QLineEdit()
        self.tool_input = QLineEdit()
        self.pasi_ro_input = QTextEdit()
        self.pasi_en_input = QTextEdit()

        self.model_combo.setStyleSheet("font-size: 14px; font-weight: 20; height: 22px")
        self.fabricatie_combo.setStyleSheet("font-size: 14px; font-weight: 20; height: 22px")
        self.module_combo.setStyleSheet("font-size: 14px; font-weight: 20; height: 22px")
        self.function_input.setStyleSheet("font-size: 14px; font-weight: 20; height: 22px")
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
        self.model_combo.currentTextChanged.connect(self.update_fabricatie)
        self.fabricatie_combo.currentTextChanged.connect(self.update_module)

        layout.addWidget(QLabel(labels["fabricatie"]))
        layout.addWidget(self.fabricatie_combo)
        if self.language == "ro":
            self.fabricatie_combo.addItem("Alege fabricație")
        else:
            self.fabricatie_combo.addItem("Choose manufacture year")

        layout.addWidget(QLabel(labels["module"]))
        layout.addWidget(self.module_combo)
        if self.language == "ro":
            self.module_combo.addItem("Alege modulul")
        else:
            self.module_combo.addItem("Choose module")
        # self.fabricatie_combo.currentTextChanged.connect(self.update_module)

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

    def update_fabricatie(self, model):
        try:
            self.fabricatie_combo.clear()
            if self.language == "ro":
                self.fabricatie_combo.addItem("Alege fabricație")
            else:
                self.fabricatie_combo.addItem("Choose manufacture year")
            if model in bmw_models:
                self.fabricatie_combo.addItems(get_bmw_years_intervals(model))
            else:
                self.reset_module()
        except Exception as e:
            print(e)
            return

    def reset_module(self):
        self.module_combo.clear()
        if self.language == "ro":
            self.module_combo.addItem("Alege modulul")
        else:
            self.module_combo.addItem("Choose module")

    def update_module(self):
        try:
            self.module_combo.clear()
            if self.language == "ro":
                self.module_combo.addItem("Alege modulul")
            else:
                self.module_combo.addItem("Choose module")
            if self.model_combo.currentText() in bmw_models:
                if self.fabricatie_combo.currentText() in bmw_modules_db[self.model_combo.currentText()]:
                    self.module_combo.addItems(get_modules_by_model_and_year
                                               (self.model_combo.currentText(), self.fabricatie_combo.currentText()))
        except Exception as e:
            print(e)

    def get_data(self):
        return {
            "model": self.model_combo.currentText(),
            "modul": self.module_combo.currentText(),
            "functie": self.function_input.text().strip(),
            "fabricatie": self.fabricatie_combo.currentText(),
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

        # Calea către fișierul JSON
        if getattr(sys, 'frozen', False):
            # Rulat ca EXE
            base_path = os.path.dirname(sys.executable)
        else:
            # Rulat din PyCharm / sursă
            base_path = os.path.dirname(os.path.abspath(__file__))

        data_dir = os.path.join(base_path, "data")
        filepath = os.path.join(data_dir, "bmw_codari.json")

        model = data["model"]
        fabricatie = data["fabricatie"]
        modul = data["modul"]
        functie = data["functie"]

        os.makedirs(data_dir, exist_ok=True)

        # Încarcă fișierul existent sau creează structura nouă
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    json_data = json.load(f)
                except json.JSONDecodeError:
                    json_data = {}
        else:
            json_data = {}

        # Creează structura: model > fabricatie > modul
        json_data.setdefault(model, {}).setdefault(fabricatie, {}).setdefault(modul, {})

        json_data[model][fabricatie][modul][functie] = {
            "tool": data["tool"],
            "pasii": {
                "ro": data["pasi_ro"],
                "en": data["pasi_en"]
            }
        }

        errors = 0
        # FOR THE SCRIPT
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)

            msg_text = "Codarea a fost salvată cu succes!" if self.language == "ro" else "Coding was saved successfully!"
            QMessageBox.information(self, "Succes" if self.language == "ro" else "Success", msg_text)
            self.accept()
        except Exception as e:
            errors += 1
            QMessageBox.critical(self, "Eroare salvare", str(e))

        # FOR THE .EXE
        try:
            location = get_resource_path("../_internal/data/bmw_codari.json")
            with open(location, "w", encoding="utf-8") as f:
                json.dump(json_data, f, ensure_ascii=False, indent=4)

                msg_text = "Codarea a fost salvată cu succes!" if self.language == "ro" else "Coding was saved successfully!"
                QMessageBox.information(self, "Succes" if self.language == "ro" else "Success", msg_text)
                self.accept()

        except Exception as e:
            errors += 1
            if errors == 2:
                QMessageBox.critical(self, "Eroare salvare", str(e))
