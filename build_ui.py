import os
import subprocess

UI_DIR = os.path.join(os.path.dirname(__file__), "gui")
UI_FILES = [os.path.join(UI_DIR, "main_window.ui"), os.path.join(UI_DIR, "record_macro.ui")]
OUTPUT_PY = [os.path.join(UI_DIR, "ui_main_window.py"), os.path.join(UI_DIR, "ui_record_macro.py")]

def convert_ui():
    for ui_file, output_py in zip(UI_FILES, OUTPUT_PY):
        cmd = ["pyside6-uic", ui_file, "-o", output_py]
        try:
            subprocess.run(cmd, check=True)
            print(f"✅ Converted: {ui_file} → {output_py}")
        except subprocess.CalledProcessError:
            print("❌ Failed to convert UI file.")

if __name__ == "__main__":
    convert_ui()
