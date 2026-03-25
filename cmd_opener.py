import subprocess
import sys
import os

def open_cmd():
    """
    Open Command Prompt (cmd.exe) in the current working directory.

    This function spawns a new Command Prompt process using the subprocess module.
    The CMD window will open with the current working directory as its starting location.

    Raises:
        SystemExit: Exits with code 1 if an exception occurs during CMD initialization.

    Returns:
        None

    Examples:
        >>> open_cmd()
        CMD opened successfully!
    """
    try:
        # Open cmd.exe in the current directory
        subprocess.Popen('cmd.exe', cwd=os.getcwd(), shell=True)
        subprocess.Popen('cmd.exe', cwd=os.getcwd())
    except Exception as e:
        print(f"Error opening CMD: {e}")
        sys.exit(1)

if __name__ == "__main__":
    open_cmd()