
# LEGO Steering Wheel for PC

![LEGO Steering Wheel](images/image.png)

🧩 Build a functional PC steering wheel using LEGO.

A fully functional PC steering wheel built from LEGO SPIKE Prime & Mindstorms 51515.
It works as a virtual game controller and supports analog steering and pedals.

## ✨ Features

- Analog steering
- Python software
- Easy to build


## 📋 Requirements

### Hardware

- LEGO SPIKE Prime Hub
- LEGO MINDSTORMS Robot Inventor (51515)
- PC
- USB cable

### Software

- Python 3.12+
- Pybricks
- vgamepad
## 🎥 Demo

 [Watch the demo on YouTube](https://youtu.be/A2cssbsgGk0)



## 📦 Download

📦 [Latest Release](https://github.com/alemannko/Lego-steering-wheel/releases/latest)
## 🛠️ Building Guide

```text
1. Download instructions
2. Assemble steering wheel and pedals
3. Install Pybricks firmware on both hubs.
4. Download the scripts
5. Run the main script
```
## 💻 Software

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

Then follow this sequence:

    1. Turn on the pedals hub.
    2. Wait for it to connect.
    3. Turn on the steering wheel hub.
    4. Wait for it to connect.

> **Note:** The hubs must be connected in this order.
## 🎮 Controls

| LEGO Control   | Virtual Controller |
| -------------- | ------------------ |
| Steering Wheel | Left Stick X       |
| Gas Pedal      | Right Stick Y      |
| Brake Pedal    | Right Stick X      |
| Button         | Cross (X)          |


## 📁 Project Structure

```text
LEGO-Steering-Wheel/
├── Instructions/
│   ├── Steering-wheel.pdf
|   └── Pedals.pdf
├── Studio/
|   ├── Pedals.io
│   └── Steering Wheel.io
├── Software/
│   ├── main.py
│   ├── steering.py
│   ├── pedals.py
│   └── requirements.txt
├── LICENSE
└── README.md
```
## 🚀 Roadmap

- Force feedback
- Paddle shifters
- Support for more games
- Support for additional platforms

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

[MIT](https://choosealicense.com/licenses/mit/)


## ❤️ Credits

- Pybricks
- vgamepad
## 🐞 Found a bug?

Please open an issue if you find a bug or have a suggestion.
