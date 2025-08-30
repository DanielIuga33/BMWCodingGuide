import json

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QTextEdit, QMessageBox
)

from ui_add_dialog import get_resource_path


class BMWCodingGuide(QWidget):
    def __init__(self, language):
        super().__init__()

        self.model_label = QLabel()
        self.model_combo = QComboBox()
        self.fabrication_label = QLabel()
        self.fabrication_combo = QComboBox()
        self.modul_label = QLabel()
        self.modul_combo = QComboBox()
        self.function_label = QLabel()
        self.function_combo = QComboBox()
        self.show_button = QPushButton()
        self.instructions_box = QTextEdit()

        self.style_label = "font-size: 14px; font-weight: 25"
        self.style_combo = "font-size: 16px; font-weight: 15; height: 32px"
        icon_path = get_resource_path("data/icon_bmw.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle("BMW Coding Guide")
        self.current_language = language
        self.setFixedSize(600, 750)
        self.setStyleSheet("background-color: hsl(0, 0%, 25%); color: #e4e4e4;")

        self.json_path = get_resource_path("data/codes.json")
        with open(self.json_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.model_label.setStyleSheet(self.style_label)
        self.model_combo.currentTextChanged.connect(self.update_fabric)
        self.model_combo.setStyleSheet(self.style_combo)

        self.fabrication_label.setStyleSheet(self.style_label)
        self.fabrication_combo.currentTextChanged.connect(self.update_module)
        self.fabrication_combo.setStyleSheet(self.style_combo)

        self.modul_label.setStyleSheet(self.style_label)
        self.modul_combo.currentTextChanged.connect(self.update_function)
        self.modul_combo.setStyleSheet(self.style_combo)

        self.function_label.setStyleSheet(self.style_label)
        self.function_combo.setStyleSheet(self.style_combo)

        self.show_button.clicked.connect(self.show_instructions)
        self.show_button.setStyleSheet("margin-top: 20px; font-size: 18px; font-weight: 20;"
                                       " height: 30px;background-color: hsl(0, 0%, 22%); border: 1px solid black;")

        self.instructions_box.setReadOnly(True)

        layout.addWidget(self.model_label)
        layout.addWidget(self.model_combo)
        layout.addWidget(self.fabrication_label)
        layout.addWidget(self.fabrication_combo)
        layout.addWidget(self.modul_label)
        layout.addWidget(self.modul_combo)
        layout.addWidget(self.function_label)
        layout.addWidget(self.function_combo)
        layout.addWidget(self.show_button)
        layout.addWidget(self.instructions_box)

        self.setLayout(layout)
        self.update_ui_language()

    def update_ui_language(self):
        if self.current_language == "ro":
            self.model_label.setText("Model BMW:")
            self.fabrication_label.setText("Fabricație:")
            self.modul_label.setText("Modul:")
            self.function_label.setText("Funcție:")
            self.show_button.setText("Afișează Instrucțiuni")
            self.model_combo.clear()
            self.model_combo.addItem("Alege model")
        else:
            self.model_label.setText("BMW Model:")
            self.fabrication_label.setText("Manufacture Year:")
            self.modul_label.setText("Module:")
            self.function_label.setText("Function:")
            self.show_button.setText("Show Instructions")
            self.model_combo.clear()
            self.model_combo.addItem("Choose model")

        self.model_combo.addItems(self.data.keys())
        self.update_fabric(self.model_combo.currentText())

    def update_fabric(self, model):
        self.fabrication_combo.clear()
        if self.current_language == "ro":
            self.fabrication_combo.addItem("Alege fabricație")
        else:
            self.fabrication_combo.addItem("Choose manufacture year")

        if model in self.data:
            self.fabrication_combo.addItems(self.data[model].keys())
        self.update_module()

    def update_module(self, _=None):
        self.modul_combo.clear()
        if self.current_language == "ro":
            self.modul_combo.addItem("Alege modul")
        else:
            self.modul_combo.addItem("Choose module")

        model = self.model_combo.currentText()
        fabric = self.fabrication_combo.currentText()

        if model in self.data and fabric in self.data[model]:
            self.modul_combo.addItems(self.data[model][fabric].keys())

        self.update_function()

    def update_function(self, _=None):
        self.function_combo.clear()
        if self.current_language == "ro":
            self.function_combo.addItem("Alege funcție")
        else:
            self.function_combo.addItem("Choose function")

        model = self.model_combo.currentText()
        fabric = self.fabrication_combo.currentText()
        modul = self.modul_combo.currentText()

        if (
                model in self.data
                and fabric in self.data[model]
                and modul in self.data[model][fabric]
        ):
            self.function_combo.addItems(self.data[model][fabric][modul].keys())

    def show_instructions(self):
        model = self.model_combo.currentText()
        fabric = self.fabrication_combo.currentText()
        modul = self.modul_combo.currentText()
        function = self.function_combo.currentText()

        if any(x.startswith(("Alege", "Choose")) for x in [model, fabric, modul, function]):
            self.instructions_box.clear()
            return

        try:
            instruction = self.data[model][fabric][modul][function]
        except KeyError:
            self.instructions_box.setText("Instrucțiuni indisponibile.")
            return

        tool_data = instruction.get("tool", "N/A")
        if isinstance(tool_data, dict):
            tool = tool_data.get(self.current_language, "N/A")
        else:
            tool = tool_data

        pasi = instruction.get("pasii", {}).get(self.current_language, [])

        if self.current_language == "ro":
            text = f"Instrument recomandat: {tool}\n\n"
        else:
            text = f"Recommended tool: {tool}\n\n"

        for i, pas in enumerate(pasi, 1):
            text += f"{i}. {pas}\n"

        self.instructions_box.setText(text)
