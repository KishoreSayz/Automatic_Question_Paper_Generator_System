from cx_Freeze import setup, Executable

# Specify the list of files to include and their locations
includefiles = ['Template\Template.docx', 'qp.db']  # Adjust paths as necessary

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    'packages': ['os', 'tkinter', 'sqlite3', 'datetime', 'docx'],  # Add necessary packages
    'include_files': includefiles,
}

# Executable
executables = [
    Executable('generate_questions.py', base=None)  # Replace with your main Python script
]

setup(
    name='MyApplication',
    version='0.1',
    description='My GUI Application',
    options={'build_exe': build_exe_options},
    executables=executables
)
