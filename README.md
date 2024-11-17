# Even or Odd Identifier

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
1. Run the script `minimalistic.py`.
2. Enter a number when prompted.
3. The program will output whether the number is even or odd.

Example:
```bash
$ python minimalistic.py
Enter a number: 4
The number is even.
```

### GUI Version
1. Run the script `WithUI.py`.
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
   git clone https://github.com/dxr3783/Odd-or-Even-Identifier.git
   cd Odd-or-Even-Identifier
   ```
2. Run the desired script:
   - CLI: `python minimalistic.py`
   - GUI: `python WithUI.py`

---

## Screenshots

### CLI Version
```
$ python minimalistic.py
Enter a number: 5
The number is odd.
```

### GUI Version
![GUI Example]![image](https://github.com/user-attachments/assets/15ea0d7f-d2a3-46e2-8522-1b8efe32e11a)


---
