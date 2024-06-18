# Smart-Trash
Educational project in the Internet of Things.

# Stack:
Database: ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)

Framework: ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

Regressions: ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

# Navigation:

```mermaid
flowchart TB
src --> smart_can
smart_can --> static
static --> .js_Files
static --> images
images --> .png_Files
smart_can --> template
template --> .html_Files
smart_can --> .py_Files
src --> tests
tests --> tests.py
```

## src - main folder with project

### smart_can - production version
-- __init__.py - initialize abstract class Unit and class of geo
-- __main__.py - start our Flask-project and logger + get blueprint
-- logger.py - connection to database
-- ManageUnits.py - initialize 2 classes: sensors and MainControlUnit
-- route.py - our blueprints for render html code

### tests
-- tests.py - testing enviroment

