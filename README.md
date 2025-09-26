# Autopilot – Macro Recorder & Replayer
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

A desktop application for recording and replaying keyboard and mouse macros.
Designed to automate repetitive tasks by capturing user input and replaying it accurately, with support for organizing, editing, and managing saved macros.

Built as a personal project to gain hands-on experience with desktop GUI design, input recording, and modular software architecture in Python.

## ✨ Features

* Record keyboard & mouse input as macros
* Replay saved macros from a GUI
* Macro management – rename, delete, edit
* Automatic timestamping for recorded macros
* JSON-based macro storage for portability and editing
* Qt-based GUI with context menus and single-row selection tables
* Infrastructure for future logic (conditions, loops, variables)

## 🛠️ Tech Stack

* Language: Python 3.11+
* GUI Framework: PySide6 (Qt for Python)
* Dependencies:
  * keyboard, mouse, pynput – input capture 
  * PySide6 – GUI framework 
  * pyautogui, pygetwindow, pillow, screeninfo – window & screen handling 
  * json, datetime – storage & timestamps 
* Storage: Local JSON files

Full list of dependencies is provided in **requirements.txt**

## 🚀 Getting Started

### Prerequisites

* Python 3.11 or later installed
* pip for managing dependencies

### Installation

Clone this repository:
```
git clone https://github.com/CanoeH01/KeyboardMouseMacroApp.git
cd KeyboardMouseMacroApp
```

Install dependencies:
``pip install -r requirements.txt``

Run the App:
``python main.py``

## 📸 Demo

### Record Macros
![](readme-gifs/Record_Macro.gif)

### Then replay endlessly
![](readme-gifs/Replay_Macro.gif)

## 🔮 Roadmap / Future Improvements

* Assign hotkeys for quick macro execution
 
* Macro scheduling (run at specific times)
 
* Advanced macro scripting with conditions, loops, and variables

## 👤 About the Project

This was a solo project, created over summer of second year as part of my preparation for a software development work placement.

Some of the biggest challenges I overcame during development have been normalising mouse input across multi-monitor setups, learning about threading to keep the GUI responsive while recording or replaying macros, and creating a modular design that supports future expansion.

What I’m most proud of is being able to take my own abstract idea and turning to a fully working desktop app for the first time. With a usable GUI, a solid file system, and room to grow.

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.
