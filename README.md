# Even or Odd Checker

This repository contains two implementations of a simple program to check whether a number is even or odd:
1. A **command-line interface (CLI)** version.
2. A **graphical user interface (GUI)** version using Tkinter.

---

## Features
- CLI Version:
  - Accepts user input from the terminal.
  - Determines if the number is even or odd.
  - Handles invalid inputs gracefully.
  
- GUI Version:
  - User-friendly interface built with Tkinter.
  - Input field and a button to check the result.
  - Displays results in a popup window.
  - Error handling for invalid inputs.

---

## How to Use

### CLI Version
1. Run the script `even_odd_cli.py`.
2. Enter a number when prompted.
3. The program will output whether the number is even or odd.

Example:
```bash
$ python even_odd_cli.py
Enter a number: 4
The number is even.
```

### GUI Version
1. Run the script `even_odd_gui.py`.
2. A window will appear with:
   - An input field.
   - A button labeled "Check".
3. Enter a number in the input field and click the "Check" button.
4. A popup will display whether the number is even or odd.

---

## File Structure
```
├── even_odd_cli.py   # CLI-based implementation
├── even_odd_gui.py   # GUI-based implementation
└── README.md         # Documentation
```

---

## Requirements
- **Python 3.6+**
- No additional dependencies required (Tkinter is included with Python by default).

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/even-odd-checker.git
   cd even-odd-checker
   ```
2. Run the desired script:
   - CLI: `python even_odd_cli.py`
   - GUI: `python even_odd_gui.py`

---

## Screenshots

### CLI Version
```
$ python even_odd_cli.py
Enter a number: 5
The number is odd.
```

### GUI Version
![GUI Example](https://via.placeholder.com/500x300?text=Insert+your+screenshot)

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
