<p align="center">
  <img alt="Playwright" src="https://ewig5qf9cgn.exactdn.com/wp-content/uploads/2022/08/Playwright_logo_long-768x155.png">
</p>

[![Playwright](https://img.shields.io/badge/Playwright-1.34.0-blue.svg)](https://github.com/microsoft/playwright)
[![Python](https://img.shields.io/badge/Python-3.11.2-blue.svg)](https://www.python.org/)
[![pip](https://img.shields.io/badge/pip-23.1.2-blue.svg)](https://pypi.org/project/pip/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


# 🎭 Playwright-Python
Welcome to the Playwright-Python repository! This repository provides a Python library for automating browser actions using Playwright.

## 🤔 What is Playwright?
Playwright is an open-source automation framework that allows developers to automate browser actions across multiple browsers, including Chromium, Firefox, and WebKit. With Playwright, you can write reliable and efficient browser automation scripts using Python.

Playwright provides a high-level API that enables you to interact with web pages, perform actions such as clicking buttons, filling forms, and capturing screenshots, and extract data from websites.

## 📋 Installation
To use Playwright-Python, first you need to create a virtual environment and activate it:
```sh
python -m venv mv_students
```

```sh
source mv_students/bin/activate
```

Then you need to have Python 3.7 or above installed on your system. You can install Playwright-Python using pip. The package is include the requirements file:

```sh
python -m pip install --upgrade pip
```

```sh
pip install -r Students/requirements.txt
```

## ⚙️ Usage
To execute a test you can use this command:

```sh
pytest Students/Examples/codegen.py -s -v --template=html1/index.html --report=Students/Examples/Reports report.html
```

## 👥 Contributing
We welcome contributions to the Playwright-Python project! If you find any issues or have suggestions for improvements, please open an issue on the GitHub repository.

If you'd like to contribute code, please fork the repository, make your changes, and submit a pull request. We appreciate your contributions!

## 📄 License
This repository is licensed under the Apache License 2.0. Feel free to use, modify, and distribute the code in this repository according to the terms of the license.

## 👏 Acknowledgements
Playwright-Python is built on top of the Playwright project, which is maintained by Microsoft. We would like to express our gratitude to the Playwright team for providing such a powerful and versatile automation framework.

## ✉️ Contact
If you have any questions or need assistance with Playwright-Python, you can reach out to us by opening an issue on the GitHub repository. We'll be happy to help!

Happy browsing automation with Playwright-Python!
