import sys
import os
import json
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QTextEdit, QHBoxLayout, QMessageBox
)

from ui_add_dialog import AddCodingDialog


def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class BMWCodingGuide(QWidget):
    def __init__(self, language):
        super().__init__()
        self.setWindowTitle("BMW Coding Guide")
        self.current_language = language
        self.setFixedSize(600, 500)

        # Încarcă datele JSON
        self.json_path = get_resource_path(os.path.join("data", "bmw_codari.json"))
        with open(self.json_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()



        # UI principale
        self.model_label = QLabel("Model BMW:")
        self.model_combo = QComboBox()
        self.model_combo.addItem("Alege model")
        self.model_combo.addItems(self.data.keys())
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

        self.add_button = QPushButton("Adaugă codare nouă")
        self.add_button.clicked.connect(self.open_add_dialog)

        main_layout.addWidget(self.model_label)
        main_layout.addWidget(self.model_combo)
        main_layout.addWidget(self.modul_label)
        main_layout.addWidget(self.modul_combo)
        main_layout.addWidget(self.functie_label)
        main_layout.addWidget(self.functie_combo)
        main_layout.addWidget(self.show_button)
        main_layout.addWidget(self.instructiuni_box)
        main_layout.addWidget(self.add_button)

        self.setLayout(main_layout)

        # Inițializare
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
            self.add_button.setText("Adaugă codare nouă")
        else:
            self.model_label.setText("BMW Model:")
            self.modul_label.setText("Module:")
            self.functie_label.setText("Function:")
            self.show_button.setText("Show Instructions")
            self.add_button.setText("Add New Coding")
        # reîmprospătare module și funcții
        self.update_module(self.model_combo.currentText())

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

        if model in ["Alege model", "Choose model"] or modul in ["Alege modul", "Choose module"] or functie in ["Alege funcție", "Choose function"]:
            self.instructiuni_box.clear()
            return

        instructiuni = self.data[model][modul][functie]
        tool = instructiuni.get("tool", {}).get(self.current_language, "N/A")
        pasi = instructiuni.get("pasii", {}).get(self.current_language, [])

        text = f"Instrument recomandat: {tool}\n\n"
        for i, pas in enumerate(pasi, 1):
            text += f"{i}. {pas}\n"

        self.instructiuni_box.setText(text)

    def open_add_dialog(self):
        dialog = AddCodingDialog(self)
        if dialog.exec_():
            new_data = dialog.get_data()
            self.adauga_codare(**new_data)

    def adauga_codare(self, model, modul, functie, fabricatie, tool_ro, tool_en, pasi_ro, pasi_en):
        # Creează structura în self.data dacă nu există
        if model not in self.data:
            self.data[model] = {}
        if modul not in self.data[model]:
            self.data[model][modul] = {}
        # Include perioada fabricației dacă e nevoie
        # Poți adapta după cum vrei, aici punem ca sub-cheie "fabricatie"
        codare_info = {
            "fabricatie": fabricatie,
            "tool": {
                "ro": tool_ro,
                "en": tool_en
            },
            "pasii": {
                "ro": pasi_ro,
                "en": pasi_en
            }
        }
        self.data[model][modul][functie] = codare_info

        # Salvează în fișier JSON
        try:
            with open(self.json_path, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False)
            QMessageBox.information(self, "Succes", "Codarea a fost adăugată și salvată cu succes!")
        except Exception as e:
            QMessageBox.critical(self, "Eroare", f"Nu s-a putut salva codarea: {e}")

        # Actualizează UI (combo-uri)
        self.update_model_language_ui()
