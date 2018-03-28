import sys
import os

from cx_Freeze import setup, Executable
try:
    approot = os.path.dirname(os.path.abspath(__file__))
except NameError:
    import sys
    approot = os.path.dirname(os.path.abspath(sys.argv[0]))
finally:
    os.chdir(approot)
	
base = None
if sys.platform == "win32":
    base = "Win32GUI"

    include_files = [r"C:\Program Files (x86)\Python36-32\DLLs\tcl86t.dll",
                     r"C:\Program Files (x86)\Python36-32\DLLs\tk86t.dll"]
				 
	
    os.environ['TCL_LIBRARY'] = r'C:\Program Files (x86)\Python36-32\tcl\tcl8.6'
    os.environ['TK_LIBRARY'] = r'C:\Program Files (x86)\Python36-32\tcl\tk8.6'
else:
    include_files = []

build_exe_options = {"packages": ["os", "tkinter", 'idna', "requests", "bs4", "subprocess"],"includes":["os", "tkinter", "requests", "bs4", "subprocess"], "include_files": include_files}
setup(
        name = "ytRSSfinder",
        version = "1.0",
        description = "A simple as F*** program to find RSS stream from any Youtube URL",
		options = {"build_exe": build_exe_options},
        executables = [Executable("ytRSSfinder.py", base = base)])