from cx_Freeze import setup, Executable

base = None


executables = [Executable("duplicates.py", base=base)]

packages = ["tkinter"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "abc",
    options = options,
    version = "1",
    description = 'first',
    executables = executables
)

