import sys
import os
import main
base = None

if sys.platform == 'win64':
    base = "Win64GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Adones\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Adones\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [main.Executable("notepad.py", base=base, icon="notepad.ICO")]


main.layout(
    name = " Notepad ",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["notepad.ICO",'tcl86t.dll','tk86t.dll', 'resources']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )