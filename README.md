# Arduino-Python-Facial-Recognition-Project

# DataSet
This project uses a teachable model to recognize a face and control an LED light depending on if the face is recognizable(due to the teachable machine) or not.

This project used two trained models using Teachable Machine.
1. Facial Recognition Model- Checks if it is my face, if yes, the LED turns green, if not the LED turns red and activates a buzzer until my face is in frame again.
2. 2 classes where one consist of my face, and the other consists of a background or anything that isn't my face.
3. "Exit"'s model if CTRL C is activated in the pyserial on Python.

These models work together to control the LED lights in the project.

## References
- [Teachable Machine](https://teachablemachine.withgoogle.com/)
- [PySerial Documentation](https://pyserial.readthedocs.io/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Arduino Documentation](https://docs.arduino.cc/)

  # Steps To Take:
  1. Go to [Teachable Machine](https://teachablemachine.withgoogle.com/).
   - Create a new image model with two classes:
   - Class 1: Your face (upload multiple pictures, be sure to make differnet expressions and change your hair or hat so the machine recongizes you regardless).
   - Class 2: Other faces/no face (or background images).
   - Export the model in TensorFlow/Keras format.

  2. **Upload Arduino Code:**
- Open the Arduino IDE and upload the basic code that listens for commands from Python to control the LED light.
- The code should:
  -Turn on the green LED when your face is detected.
  -Turn on the red LED when no face is detected.

 3.  **Set Up Python-Arduino Communication:**
- Install the required Python libraries using: pip install pyserial tensorflow opencv-python
   - Use Python to send serial signals to the Arduino:
   - When the model detects your face, Python sends a signal to turn on the green LED.
   - When no face is detected, Python sends a signal to turn on the red LED.

4. **Test the System:**
- Train and test the model (facial recognition).
- Test the communication between Python and Arduino to ensure the LED control works based on:
  - Facial recognition (green for your face, red for no face).
 
5. ## Refine the project as needed
   - Check if the code runs smoothly as well as the program itself.
   - Check if the machine recognizes your face and runs smoothly during runtime.
   - Adjust the machine as needed and/or the code


























## Versions Used:
- **Python:** 3
- **TensorFlow:** 2.18
- **Keras:** Latest
- **OpenCV:** 4.10
- **PySerial:** 3.5
- **Arduino IDE:** Latest
- **Hardware:** Arduino Mega 2560
