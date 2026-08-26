# Python Virtual Environments & pip

## 📘 Description

This repository contains beginner-friendly Python examples that demonstrate **Virtual Environments and Package Management with pip**. It covers creating and activating virtual environments, installing Python packages, managing dependencies with `pip`, creating `requirements.txt`, installing dependencies from a requirements file, and using `.gitignore` to exclude virtual environments from GitHub.

## 📚 Topics Covered

* Introduction to Virtual Environments
* Why Virtual Environments Are Needed
* Creating a Virtual Environment
* `venv` Module
* Activating a Virtual Environment
* Deactivating a Virtual Environment
* Checking the Active Python Environment
* `where.exe python`
* Introduction to `pip`
* Installing Packages with `pip`
* `pip install`
* Checking Installed Packages
* `pip list`
* Package Dependencies
* Upgrading `pip`
* `python -m pip`
* `pip freeze`
* Creating `requirements.txt`
* Package Version Pinning
* Installing from `requirements.txt`
* `pip install -r requirements.txt`
* Creating Multiple Virtual Environments
* Switching Between Virtual Environments
* `.gitignore`
* Ignoring Virtual Environments in Git
* Python Dependency Management
* Virtual Environments for Real-World Projects
* Virtual Environments for Agentic AI Projects

## 🛠️ Technologies Used

* Python 3
* PyCharm
* PowerShell
* `venv` — Python Standard Library
* `pip` — Python Package Installer
* `requests` — Python HTTP Library
* Git & GitHub

## ▶️ How to Run

1. Clone this repository.
2. Open the project in PyCharm or Visual Studio Code.
3. Navigate to the `26_Virtual_Environments_Pip` folder.
4. Create a virtual environment:

```powershell
py -m venv venv
```

5. Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

6. Install the project dependencies:

```powershell
pip install -r requirements.txt
```

7. Run the Python program:

```powershell
python main.py
```

## 📦 Package Management

This project demonstrates how to install and manage Python packages using `pip`.

The `requests` package was installed using:

```powershell
pip install requests
```

Installed dependencies were saved using:

```powershell
pip freeze > requirements.txt
```

The dependencies can later be recreated using:

```powershell
pip install -r requirements.txt
```

## 🔒 Virtual Environment & Git

Virtual environments are not uploaded to GitHub because they contain environment-specific files and installed packages.

The `.gitignore` file prevents virtual environments from being tracked:

```text
venv/
test_env/
__pycache__/
```

Instead of uploading the environment itself, the project uploads `requirements.txt`, which allows the environment to be recreated when needed.

## 🎯 Learning Outcome

After completing this section, I can:

* Create Python virtual environments.
* Activate and deactivate virtual environments.
* Understand why virtual environments are important.
* Install Python packages using `pip`.
* Check installed packages using `pip list`.
* Upgrade `pip`.
* Understand package dependencies.
* Create and use `requirements.txt`.
* Reinstall project dependencies from `requirements.txt`.
* Manage multiple virtual environments.
* Use `.gitignore` to exclude virtual environments from GitHub.
* Understand how dependency management is used in real-world Python and Agentic AI projects.

## 👩‍💻 Author

**Sadia Hadayat-Ullah**

GitHub: https://github.com/sadiahadayat-ullah

