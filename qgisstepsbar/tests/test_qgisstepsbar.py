from qgisstepsbar import QgisStepsBar
from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QPushButton


def test_dialog():
    class BackButton(QPushButton):
        def __init__(self, stepsbar):
            super().__init__("Back")
            self.clicked.connect(stepsbar.decrement)

    class NextButton(QPushButton):
        def __init__(self, stepsbar):
            super().__init__("Next")
            self.clicked.connect(stepsbar.increment)

    class MainDialog(QDialog):
        def __init__(self):
            super().__init__()
            self.layout = QVBoxLayout()
            self.setLayout(self.layout)

            self.stepsbar = QgisStepsBar(["Step 1", "Step 2", "Step 3", "Step 4"])
            self.layout.addWidget(self.stepsbar)

            self.back_button = BackButton(self.stepsbar)
            self.layout.addWidget(self.back_button)

            self.next_button = NextButton(self.stepsbar)
            self.layout.addWidget(self.next_button)

    main_dialog = MainDialog()
    main_dialog.show()
