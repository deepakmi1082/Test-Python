# Test-Python Project

## Overview
The Test-Python project provides a simple utility to open the Command Prompt (cmd.exe) in the current working directory. This functionality is encapsulated in the `cmd_opener.py` file, which utilizes Python's `subprocess` module to spawn a new CMD process.

## Files

- **cmd_opener.py**: Contains the `open_cmd` function that opens a Command Prompt in the current working directory.
- **README.md**: Documentation for the project, including usage instructions.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **requirements.txt**: Lists the dependencies required for the project.

## Usage
To use the `open_cmd` function, simply run the `cmd_opener.py` script. This will open a new Command Prompt window in the directory where the script is executed.

```bash
python cmd_opener.py
```

## Requirements
Make sure to have Python installed on your system. You can install any required dependencies listed in `requirements.txt` using pip:

```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.