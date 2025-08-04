import os
import subprocess

UI_DIR = os.path.join(os.path.dirname(__file__), "gui")
UI_FILE = os.path.join(UI_DIR, "main_window.ui")
OUTPUT_PY = os.path.join(UI_DIR, "ui_main_window.py")

def convert_ui():
    cmd = ["pyside6-uic", UI_FILE, "-o", OUTPUT_PY]
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Converted: {UI_FILE} → {OUTPUT_PY}")
    except subprocess.CalledProcessError:
        print("❌ Failed to convert UI file.")

if __name__ == "__main__":
    convert_ui()
