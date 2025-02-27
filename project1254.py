
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
import time
import serial

port = "COM3"  # Replace with your serial port
baud_rate = 9600

 
from tensorflow.keras.layers import DepthwiseConv2D

class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop("groups", None)  # Ignore 'groups' argument
        super().__init__(*args, **kwargs)

# Load the model
model = load_model(
    "C:\\Users\\nsutto2\\OneDrive - IL State University\\254\\keras_Model.h5",
    compile=False,
    custom_objects={"DepthwiseConv2D": CustomDepthwiseConv2D}
)

# Load the labels
class_names = open("C:\\Users\\nsutto2\\OneDrive - IL State University\\254\\labels.txt", "r").readlines()


# CAMERA can be 0 or 1 based on default camera of your computer

try: 
    camera = cv2.VideoCapture(0)
    arduino = serial.Serial(port, baud_rate)
    time.sleep(2) 

    while True:
        # Grab the webcamera's image.
        ret, image = camera.read()

        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Show the image in a window
        cv2.imshow("Webcam Image", image)

        # Make the image a numpy array and reshape it to the model's input shape
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predict using the model
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        class_label = class_name[2:].strip().lower()  # Clean up the class label
        
        print(f"Class Label Detected: '{class_label}'")  # Debugging line

        # Decide what message to send
        message_to_send = ""  # Default to empty
        
        if class_label == 'naia':
            message_to_send = "ON\n"
            print("Detected Naia - Turning ON Green LED")
        elif class_label == 'notnaia':
            message_to_send = "OFF\n"
            print("Detected Not Naia - Turning ON Red LED and Buzzer")
        else:
            print("No matching class label found.")  # Debugging line
        
        # Only send if message_to_send is not empty
        if message_to_send:
            arduino.write(message_to_send.encode('utf-8'))
            arduino.flush()  # Ensure the message is sent
            print(f"Sent: {message_to_send.strip()}") 

        time.sleep(1)  # Small delay between messages
        
        # Listen to the keyboard for presses.
        keyboard_input = cv2.waitKey(1)
        if keyboard_input == 27:  # Exit if 'ESC' is pressed
            break

except serial.SerialException as e:
    print(f"Serial Error: {e}")

finally:
    # Close serial connection once, at the end
    arduino.close()
    print("Serial port closed")

    # Release the camera and close OpenCV windows
    camera.release()
    cv2.destroyAllWindows()

