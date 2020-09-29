# QGIS Steps Bar
## Usage
### Installation
```bash
pip install qgisstepsbar
```

### Sample Code 1 (Add to layout)
```python
from qgisstepsbar import QgisStepsBar
from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.stepsbar = QgisStepsBar(["Step1", "Step 2", "Step 3", "Step 4"])
        self.layout.addWidget(self.stepsbar)

dialog = Dialog()
dialog.show()
```

![QGIS Step Bar](https://raw.githubusercontent.com/linz/qgis-steps-bar/master/media//qgisstepsbar.png)

### Sample Code 2 (Add controls)
```python
from qgisstepsbar import QgisStepsBar
from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QPushButton

class BackButton(QPushButton):
    def __init__(self, stepsbar):
        super().__init__("Back")
        self.clicked.connect(stepsbar.decrement)

class NextButton(QPushButton):
    def __init__(self, stepsbar):
        super().__init__("Next")
        self.clicked.connect(stepsbar.increment)

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.stepsbar = QgisStepsBar(["Step1", "Step 2", "Step 3", "Step 4"])
        self.layout.addWidget(self.stepsbar)

        self.back_button = BackButton(self.stepsbar)
        self.layout.addWidget(self.back_button)

        self.next_button = NextButton(self.stepsbar)
        self.layout.addWidget(self.next_button)

dialog = Dialog()
dialog.show()
```

![QGIS Step Bar](https://raw.githubusercontent.com/linz/qgis-steps-bar/master/media//control.png)

## Development
### Dependencies Requirements
You are going to need 
- Python 3.8+
- QGIS 3.10+

### Setup
Create and activate a virtual environment.

```bash
python3 -m venv .venv
. .venv/bin/activate
```

Upgrade pip and install the required dependencies.

```bash
pip install --upgrade pip
pip install -r requirements-dev.txt
```

Install commit-msg git hook. It runs on every local commit to check if the commit message conforms to the convention specified in `.gitlint`

```bash
pre-commit install --hook-type commit-msg
```

Install Poetry. Peotry is a Python project management tool. QGIS Steps Bar uses Peotry to deploy packages to PyPI.
To install:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
poetry env use .venv/bin/python3
```

### Deployment
The following command builds the source and wheels archives:

```bash
poetry build
```

This command publishes the package, previously built with the build command, to PyPI

```bash
poetry publish
```

### Versioning
Different verisons can be found at PyPI: https://pypi.org/project/qgisstepsbar/
