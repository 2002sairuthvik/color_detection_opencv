# Real-Time Yellow Object Detection with OpenCV and PIL

## Overview

This project demonstrates **real-time detection and localization of yellow objects** using a webcam feed. It leverages OpenCV for image processing and Pillow (PIL) for convenient bounding box calculation.

The workflow:
- Captures frames from the webcam.
- Converts each frame to HSV color space for robust color detection.
- Applies a color mask to isolate yellow regions.
- Uses PIL to compute the bounding box of detected yellow areas.
- Draws a rectangle around detected yellow objects in the live video feed.

---

## Features

- **Real-time webcam capture**
- **Color segmentation in HSV space**
- **Automatic bounding box around detected yellow objects**
- **Modular color limit calculation with a utility function**

---

## Installation

First, install the required dependencies:


---

## Usage

1. Ensure your webcam is connected.
2. Place the following code in your `main.py`:

    ```
    import cv2
    from utils import get_limits
    from PIL import Image

    yellow =   # yellow in BGR color space
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lowerLimit, upperLimit = get_limits(color=yellow)
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()
        if bbox is not None:
            x1, y1, x2, y2 = bbox
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    ```

3. Create a `utils.py` file with the following function:

    ```
    import numpy as np
    import cv2

    def get_limits(color):
        c = np.uint8([[color]])
        hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
        lowerLimit = hsvC - 10, 100, 100
        upperLimit = hsvC + 10, 255, 255
        lowerLimit = np.array(lowerLimit, dtype=np.uint8)
        upperLimit = np.array(upperLimit, dtype=np.uint8)
        return lowerLimit, upperLimit
    ```

4. Run the main script:

    ```
    python main.py
    ```

5. Press **Q** to quit the application.

---

## How It Works

- **Color Detection:** The code uses HSV color space, which is better for color segmentation than BGR/RGB.
- **Mask Creation:** A binary mask is generated, highlighting only yellow regions.
- **Bounding Box:** The mask is converted to a PIL Image to use `.getbbox()`, which finds the smallest rectangle containing all detected yellow pixels.
- **Visualization:** A green rectangle is drawn on the original frame to indicate the detected object.

---

## Notes

- The use of PIL is specifically for the `.getbbox()` method, which simplifies bounding box detection in binary images.
- For more advanced object detection or to avoid PIL, consider using OpenCV’s `findContours` and `boundingRect` methods.

---

## License

This project is open-source and free to use.

