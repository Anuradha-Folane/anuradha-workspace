# anuradha-workspace
# Playwright Pytest Automation Framework

This repository contains a **basic but scalable UI automation framework**
built using **Python, Pytest, and Playwright**.

###
Purpose of This Project
Learn Playwright with Pytest
Understand Page Object Model
Practice pytest fixtures (conftest.py)
Build a reusable automation foundation
Maintain a reference project on GitHub
### 

🛠️ Tech Stack

- Python 3
- Pytest
- Playwright (sync API)
- Page Object Model (POM)


## 📁 Project Structure & Explanation
anuradha-workspace/
├── pages/
│   ├── __init__.py
│   └── login_page.py
│
├── tests/
│   ├── test_example.py
│   └── test_login.py
│
├── conftest.py
├── pytest.ini
├── .gitignore
└── README.md

1} pages/
Contains Page Object classes.
Each page class holds:
>locators
>actions
>page-specific methods
***Keeps test logic clean and readable***

Eg: login_page.py
>Contains locators for login page
>Methods to open page and perform login

2} tests/
Contains all test cases.
Eg: test_login.py
>UI test for login functionality
>Uses Playwright page fixture
>Uses LoginPage from pages folder
***Tests should only contain assertions and test flow.***

3) Conftest.py
This is the heart of the framework.
Responsibilities:
>Manages Playwright browser lifecycle
>Creates reusable pytest fixtures
>Provides page fixture to all tests
***Avoids duplicate setup code in tests.***

4} pytest.ini
Pytest configuration file.
Used to:
>Control test discovery
>Set default pytest options
>Simplify command-line execution

5} .gitignore
Prevents unnecessary files from being committed:
>virtual environment (venv)
>cache files
>Playwright reports
>IDE config files
