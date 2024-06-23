# Hand Gesture Controlled Virtual Mouse and Gamepad

## Overview

This repository contains two Python scripts that utilize hand gestures detected via a webcam to control a virtual mouse and gamepad. The scripts use OpenCV, MediaPipe, and PyAutoGUI to achieve this functionality.

### Features

- **Virtual Mouse**: Control the mouse pointer and perform click actions using hand gestures.
- **Virtual Gamepad**: Control arrow keys based on hand gestures to simulate gamepad movements.

## Setup and Installation

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/hand-gesture-control.git
    cd hand-gesture-control
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Scripts

#### Virtual Mouse

- To start the virtual mouse control script, run:
    ```bash
    python hand_detector.py
    ```

#### Virtual Gamepad

- To start the virtual gamepad control script, run:
    ```bash
    python move_car.py
    ```

## Scripts

### `hand_detector.py`

This script uses the webcam to detect hand gestures and control the mouse pointer. It tracks the index finger and thumb to move the cursor and perform click actions.

#### How it works:
- Uses MediaPipe to detect hand landmarks.
- Calculates the distance between the index finger (landmark 8) and thumb (landmark 4).
- Moves the mouse pointer based on the index finger's position.
- Clicks the mouse when the distance between the index finger and thumb is below a certain threshold.

### `move_car.py`

This script uses the webcam to detect hand gestures and control the arrow keys, simulating a gamepad. It detects the movement of the index finger to press and release the 'up' and 'left' or 'right' arrow keys.

#### How it works:
- Uses MediaPipe to detect hand landmarks.
- Tracks the horizontal movement of the index finger (landmark 8).
- Presses 'up' and 'right' keys when the index finger moves to the right.
- Presses 'up' and 'left' keys when the index finger moves to the left.
- Releases the keys when the finger is not moving or the script stops detecting hands.

## File Structure

- **hand_detector.py**: Script for virtual mouse control.
- **move_car.py**: Script for virtual gamepad control.
- **requirements.txt**: List of required Python packages.
- **README.md**: This readme file.

## Dependencies

The following Python packages are required for this project:
- opencv-python
- mediapipe
- pyautogui

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Contributing

If you wish to contribute to this project, please create a fork and submit a pull request.

## Contact

For any issues or questions, please contact:
- **Email**: your.email@example.com

---

Feel free to modify and enhance this project as needed. Contributions are welcome!

---
