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

Install the required dependencies.

```bash
poetry install
```

### Deployment
You will have to add your own pypi token in this repo as a secret called `PYPI_TOKEN`

Run the following command and push the new branch to publish this package to pypi:

```bash
sh version.bump.sh
```


### Versioning
Different verisons can be found at PyPI: https://pypi.org/project/qgisstepsbar/
