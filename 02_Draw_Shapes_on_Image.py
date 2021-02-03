#Import Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

#Create a black image to work
black_img = np.zeros(shape=(512,512,3),
                    dtype=np.int16)

#Get the Shape of the Image
black_img.shape

#Show it
plt.imshow(black_img)

#Draw a Circle
cv2.circle(img=black_img,
          center=(400,100),
          radius=50,
          color =(255,0,0),
          thickness=8)

plt.imshow(black_img)

#Filled Circle
cv2.circle(img=black_img,
          center=(400,200),
          radius=50,
          color =(0,255,0),
          thickness=-1)

plt.imshow(black_img)

#Draw a Rectangle
#  The first number is on x-axis & the second on the y-axis

#We need two points. One for up and one diagonally down
cv2.rectangle(black_img,
             pt1=(200,200),
             pt2=(300,300),
             color=(0,255,0),
             thickness=5)

plt.imshow(black_img)

#Draw Triangle
vertices = np.array([[10,450],
                    [110,350],
                    [180,450]],
                   np.int32)

pts = vertices.reshape(-1,1,2)

cv2.polylines(black_img,
             [pts],
             isClosed=True,
             color=(0,0,255),
             thickness=3)

plt.imshow(black_img)

#Filled Rectangle
cv2.rectangle(black_img,
             pt1=(200,50),
             pt2=(300,150),
             color=(137,79,213),
             thickness=-1)

plt.imshow(black_img)

#Filled Triangle
vertices = np.array([[10,250],
                    [110,150],
                    [180,250]],
                   np.int32)

pts = vertices.reshape(-1,1,2)

cv2.fillPoly(black_img,
             [pts],
             color=(255,167,201))

plt.imshow(black_img)

#Draw Line
cv2.line(black_img,
        pt1=(512,0),
        pt2=(0,512),
        color=(255,0,255),
        thickness=3)

plt.imshow(black_img)

#Write Text
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(black_img,
           text='Rhyme',
           org=(210,500),
           fontFace=font,
           fontScale=3,
           color=(255,255,0),
           thickness=3,
           lineType=cv2.LINE_AA)

plt.imshow(black_img)
