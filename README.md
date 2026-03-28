# ⚛️ Physics Formula Calculator

A simple command-line Python program that calculates five common physics formulas based on user input.

---

## 📋 Description

This program presents the user with a menu of five physics formulas. The user selects a formula, enters the required values, and the program calculates and displays the result with the correct unit.

---

## 🚀 How to Run

Make sure you have Python installed (Python 3 recommended), then run:

```bash
python physics_calculator.py
```

---

## 🎮 How to Use

1. Run the program — a menu of 5 formulas is displayed.
2. Type the letter (`a`, `b`, `c`, `d`, or `e`) matching your chosen formula.
3. Enter the required values when prompted.
4. The calculated result is printed with its unit.

---

## 📐 Formulas Covered

| Option | Formula | Equation | Unit |
|--------|---------|----------|------|
| a | Momentum | M = m × v | kg·m/s |
| b | Potential Energy | PE = m × g × h | J (Joules) |
| c | Ohm's Law | V = I × R | V (Volts) |
| d | Kinetic Energy | KE = 0.5 × m × v² | J (Joules) |
| e | Work Done | W = F × d | J (Joules) |

---

## 📊 Sample Output

```
Choose a formula:
a = Momentum         (M = m * v)
b = Potential Energy (PE = m * g * h)
c = Ohm's Law        (V = I * R)
d = Kinetic Energy   (KE = 0.5 * m * v²)
e = Work Done        (W = F * d)

Enter a, b, c, d or e: b
Mass (kg): 10
Gravity (m/s²) [9.8 on Earth]: 9.8
Height (m): 5
Potential Energy = 490.0 J
```

---

## 🔢 Variable Reference

| Variable | Meaning | Unit |
|----------|---------|------|
| m | Mass | kg |
| v | Velocity | m/s |
| g | Gravitational acceleration | m/s² |
| h | Height | m |
| I | Current | A (Amperes) |
| R | Resistance | Ω (Ohms) |
| F | Force | N (Newtons) |
| d | Distance | m |

---

## 🛠️ Requirements

- Python 3.x
- No external libraries required

---

## 📁 File Structure

```
physics_calculator.py    # Main program
README.md                # Project documentation
```




- Allow the user to run multiple calculations without restarting
- Display a history of previous calculations
- Build a GUI version using Tkinter or a web version using Streamlit
