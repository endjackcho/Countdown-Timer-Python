# Countdown Timer ⏳

A simple interactive countdown timer built with Python.

This program allows users to set a custom countdown duration using the HH:MM:SS format. It continuously updates the remaining time until the countdown reaches zero.

### Features
- **Custom Time Input:** Accepts hours, minutes, and seconds.
- **Real-Time Countdown:** Updates the displayed time every second.
- **Automatic Time Conversion:** Handles transitions between seconds, minutes, and hours.
- **Input Validation:** Handles invalid time formats and values.
- **Interactive CLI:** Allows users to run multiple countdowns.
- **Exit Option:** Press Enter without entering a value to quit.

### Input Format
```text
HH:MM:SS
```

### Example
**Input:**
```text
Enter your time: 01:02:05
```

**Output:**
```text
1:2:5
1:2:4
1:2:3
...
>> Timer finished !
```

### Technologies Used
- Python
- Time Module (`sleep`)
- OS Module
- Functions
- Exception Handling
- While Loops
- Conditional Statements
- String Manipulation

### How to Run
```bash
python main.py
```

**A beginner-friendly Python project focused on time management, loops, conditional logic, and working with built-in Python modules.**
