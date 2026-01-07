# ProdigyInfoTech-CyberSecurity-Internship-Task-04
Task 04: Ethical Keylogger

This project is created as part of the **Prodigy InfoTech Cyber Security Internship Program**.  
The task demonstrates a simple and ethical implementation of a keylogger using Python.

---

## 🎯 Task Objective
To build a basic Python program that:
- Listens to keyboard events  
- Records all keystrokes pressed by the user  
- Saves them securely into a text file  
- Stops execution when the ESC key is pressed  

---

## 🛠️ Technologies Used
- Python 3
- pynput library for keyboard event handling

---

## ⚙️ Features
- Captures real-time keyboard inputs  
- Logs keystrokes into `keystrokes.txt`  
- Supports background listener mode  
- Safe handling of alphabets, numbers, and special keys  
- ESC key to exit the program  
- Lightweight and easy to use CLI-based tool  

---

## ▶️ How to Run the Program

1. Install the required dependency:
```bash
pip install pynput
Navigate to the project directory:
cd ProdigyInfoTech-CyberSecurity-Internship-Task-04

Run the keylogger program:
python keylogger.py
Type any keys on your keyboard.
Press ESC to stop the program.
Open keystrokes.txt to view the logged output.

🧪 Example Behavior
User types: rohit test 123 !@#
Output stored in file: keystrokes.txt
Program exits on ESC key press

📂 Project Structure
arduino
Copy code
ProdigyInfoTech-CyberSecurity-Internship-Task-04/
│
├── keylogger.py
├── README.md
├── keystrokes.txt
