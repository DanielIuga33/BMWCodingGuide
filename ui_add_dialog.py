from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton, QTextEdit


class AddCodingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Adaugă Codare Nouă")
        self.setFixedSize(400, 500)

        layout = QVBoxLayout()

        self.model_input = QLineEdit()
        self.module_input = QLineEdit()
        self.function_input = QLineEdit()
        self.fabricatie_input = QLineEdit()
        self.tool_ro_input = QLineEdit()
        self.tool_en_input = QLineEdit()
        self.pasi_ro_input = QTextEdit()
        self.pasi_en_input = QTextEdit()

        layout.addWidget(QLabel("Model"))
        layout.addWidget(self.model_input)
        layout.addWidget(QLabel("Modul"))
        layout.addWidget(self.module_input)
        layout.addWidget(QLabel("Funcție"))
        layout.addWidget(self.function_input)
        layout.addWidget(QLabel("Perioadă fabricație"))
        layout.addWidget(self.fabricatie_input)
        layout.addWidget(QLabel("Tool RO"))
        layout.addWidget(self.tool_ro_input)
        layout.addWidget(QLabel("Tool EN"))
        layout.addWidget(self.tool_en_input)
        layout.addWidget(QLabel("Pași RO (fiecare pe linie nouă)"))
        layout.addWidget(self.pasi_ro_input)
        layout.addWidget(QLabel("Pași EN (fiecare pe linie nouă)"))
        layout.addWidget(self.pasi_en_input)

        btn_save = QPushButton("Salvează")
        btn_save.clicked.connect(self.accept)
        layout.addWidget(btn_save)

        self.setLayout(layout)

    def get_data(self):
        return {
            "model": self.model_input.text().strip(),
            "modul": self.module_input.text().strip(),
            "functie": self.function_input.text().strip(),
            "fabricatie": self.fabricatie_input.text().strip(),
            "tool_ro": self.tool_ro_input.text().strip(),
            "tool_en": self.tool_en_input.text().strip(),
            "pasi_ro": [line.strip() for line in self.pasi_ro_input.toPlainText().splitlines() if line.strip()],
            "pasi_en": [line.strip() for line in self.pasi_en_input.toPlainText().splitlines() if line.strip()]
        }
