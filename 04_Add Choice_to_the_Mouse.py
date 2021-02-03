# Import Libraries
import cv2
import numpy as np

# Function
# x,y, flags, param are feed from OpenCV automaticaly
def draw_circle(event, x, y, flags, param):
    # Left Button Down
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,
                  (x, y),
                  100,
                  (75,131,251),
                  -1)
    # Right Button Down
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,
                  (x, y),
                  50,
                  (251,75,131),
                  -1)

# Connect the Function with the Callback
cv2.namedWindow(winname='my_draw')


# Callback
cv2.setMouseCallback('my_draw', draw_circle)

# Using OpenCV to show the Image
img = np.zeros((512,512,3),
              np.int8)

while True:
    
    cv2.imshow('my_draw', img)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

