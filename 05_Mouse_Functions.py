# Import Libraries
import cv2
import numpy as np


# Variables
# TRUE when the mouse button is DOWN
# FALSE when the mouse button is UP
drawing = False
ex = -1
ey = -1

# Function
# x,y, flags, param are feed from OpenCV automaticaly
def draw_rectangle(event,x,y,flags,params):
    
    global ex, ey, drawing 
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ex, ey = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,
                         (ex,ey),
                         (x,y,),
                         (255,0,255),
                         -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,
                    (ex,ey),
                    (x,y,),
                    (255,0,255),
                    -1)         
            

# Connect the Function with the Callback
img = np.zeros((512,512,3),np.int8)

cv2.namedWindow(winname='my_draw')

# Callback
cv2.setMouseCallback('my_draw', draw_rectangle)

# Using OpenCV to show the Image
while True:
    
    cv2.imshow('my_draw', img)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows
