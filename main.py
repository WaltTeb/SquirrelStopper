import cv2
import numpy as np
import serial
import time

def main():
    
    
    monitorMovement()
    
    activateAlarm()


def monitorMovement():
    startTime = time.time()
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0 

    darkestRow = 0 #initial darkest row

    thresh = 18 #number of rows darkest average has to change to register movement

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        img_counter+=1

        
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        row, column = image.shape #get x and y heights of the image

        #turn image grayscale values into multidimensional array
        rowArray = []
        for i in range(column):
            rowArray.append([])
            for j in range(row):
                rowArray[i].append(image[j,i])

        #calculate mean grayscale values of each row of pixels
        meanRowValues = []
        for i in range(column):
            meanRowValues.append(np.mean(rowArray[i]))

        curDarkRow = np.argmax(meanRowValues)

        #if the darkest row in two successive frames is different, then movement occured
        if(img_counter > 2):
            if(darkestRow+thresh < curDarkRow or darkestRow-thresh > curDarkRow):
                print("CurDarkestRow = {}".format(curDarkRow))
                print("previousDarkestRow = {}".format(darkestRow))
                print("Movement detected!")
                endTime = time.time()
                break
        darkestRow = curDarkRow

        
        

    cam.release()
    cv2.destroyAllWindows()

    print("No movement for {} seconds".format(int(endTime-startTime)))
    
    


def activateAlarm():
    arduinoData = serial.Serial('com9', 9600)
    time.sleep(3)
    arduinoData.write(b'1')
        


main()