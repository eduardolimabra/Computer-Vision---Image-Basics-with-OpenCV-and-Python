# Import Libraries
import cv2
import numpy as np


# Function
# x,y, flags, param are feed from OpenCV automaticaly
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,
                  (x,y),
                  70,
                  (35,69,78),
                  1)



# Connect the Function with the Callback
cv2.namedWindow(winname='my_drawing')


# Callback
cv2.setMouseCallback('my_drawing', draw_circle)

# Using OpenCV to show the Image
img = np.zeros((512,512,3),
              np.int8)

while True:
    
    cv2.imshow('my_drawing', img)
    
    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()
