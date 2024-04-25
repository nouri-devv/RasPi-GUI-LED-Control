from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import gpiod

# Create the chip object once
chip = gpiod.Chip('gpiochip4')

green_LED_PIN = 17
green_LED_line = chip.get_line(green_LED_PIN)
green_LED_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

red_LED_PIN = 27
red_LED_line = chip.get_line(red_LED_PIN)
red_LED_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

blue_LED_PIN = 22
blue_LED_line = chip.get_line(blue_LED_PIN)
blue_LED_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)


# Initialize LED states
green_LED_state = False
red_LED_state = False
blue_LED_state = False


def green_clicked():
    global green_LED_state

    if green_LED_state:
        green_LED_line.set_value(0)
        green_LED_state = False
        print("OFF")
    else:
        green_LED_line.set_value(1)
        green_LED_state = True
        print("On")

def red_clicked():
    global red_LED_state

    if red_LED_state:
        red_LED_line.set_value(0)
        red_LED_state = False
        print("OFF")
    else:
        red_LED_line.set_value(1)
        red_LED_state = True
        print("On")

def blue_clicked():
    global blue_LED_state

    if blue_LED_state:
        blue_LED_line.set_value(0)
        blue_LED_state = False
        print("OFF")
    else:
        blue_LED_line.set_value(1)
        blue_LED_state = True
        print("On")


def window():
    # setting up the window properties
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("SIT210 - Task 5.1P")

    # main label or heading
    label = QtWidgets.QLabel(win)
    label.setText("SIT210 - Task 5.1P")

    # Green LED button
    green_LED = QtWidgets.QPushButton(win)
    green_LED.setText("GREEN")
    green_LED.move(100, 50)
    green_LED.clicked.connect(green_clicked)

    # Red LED button
    red_LED = QtWidgets.QPushButton(win)
    red_LED.setText("RED")
    red_LED.move(100, 100)
    red_LED.clicked.connect(red_clicked)

    # Blue LED button
    blue_LED = QtWidgets.QPushButton(win)
    blue_LED.setText("BLUE")
    blue_LED.move(100, 150)
    blue_LED.clicked.connect(blue_clicked)

    # show the window at the end of function
    win.show()
    sys.exit(app.exec_())

window()