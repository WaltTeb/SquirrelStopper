# SquirrelStopper
Basic motion detection algorithm made during Hack UMass 2022.
Utilizes openCV library for python. The main function of the program is a loop that periodically takes a photo with the webcam, and converts it to a greyscale.
The darkest average row of pixels is then compared to the previous darkest row of pixels, if the two differ too drastically, motion is detected, and the Arduino
triggers the alarm to go off. 
