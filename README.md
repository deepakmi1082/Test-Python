# Test-Python Project

## Overview
The Test-Python project is a collection of simple Python utilities and examples, including a basic calculator and a command prompt opener. It demonstrates fundamental Python programming concepts, unit testing, and basic CLI interactions.

## Features
- **Calculator Module**: Performs basic arithmetic operations (addition, subtraction, multiplication, division).
- **Command Prompt Opener**: Opens a new Command Prompt window in the current working directory.
- **Unit Tests**: Comprehensive test suites for both modules using Python's unittest framework.

## Files
- **calculator.py**: Implements basic arithmetic functions and a CLI interface for calculations.
- **cmd_opener.py**: Contains the `open_cmd` function to open Command Prompt.
- **test_calculator.py**: Unit tests for the calculator module.
- **test_cmd_opener.py**: Unit tests for the command opener module.
- **requirements.txt**: Lists project dependencies.
- **README.md**: This documentation file.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/deepakmi1082/Test-Python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Test-Python
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Calculator
Run the calculator script for interactive arithmetic operations:
```bash
python calculator.py
```
Follow the prompts to select an operation and enter numbers.

You can also import and use the functions programmatically:
```python
from calculator import add, subtract, multiply, divide

result = add(2, 3)  # Returns 5
```

### Command Prompt Opener
Run the script to open a new Command Prompt:
```bash
python cmd_opener.py
```

## Testing
Run the unit tests to verify functionality:
```bash
python -m unittest test_calculator.py
python -m unittest test_cmd_opener.py
```

Or run all tests:
```bash
python -m unittest
```

## Requirements
- Python 3.x
- Dependencies listed in `requirements.txt` (currently subprocess32 for compatibility)

## Contributing
1. Fork the repository.
2. Create a feature branch.
3. Make your changes and add tests.
4. Run tests to ensure everything works.
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.