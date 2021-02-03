#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Matplotlib & PIL

#Import Libraries

import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

#Use the PIL for the image

from PIL import Image
img = Image.open('images/rock.jpg')
img

#Rotate the Image
img.rotate(-90)

#Check the Type of the Image
type(img)

#Turn the image into an array
img_array = np.asarray(img)
type(img_array)

#Get the Height, Width & Channels
img_array.shape
plt.imshow(img_array)

#      R G B channels
#      Red channel is in position No 0,
#      Green channel is in position No 1,
#      Blue channel is in position No 2.
#      The Colour Values are from 0 == no colour from the channel, to 255 == full colour from the channel.

img_test = img_array.copy()

#Only Red channel
plt.imshow(img_test[:,:,0])

#Scale Red channel to Gray
plt.imshow(img_test[:,:,0], cmap='gray')

#Only Green channel
plt.imshow(img_test[:,:,1])

#Scale Green channel to Gray
plt.imshow(img_test[:,:,1], cmap = 'gray')

#Only Blue channel
plt.imshow(img_test[:,:,2])

#Scale Blue channel to Gray
plt.imshow(img_test[:,:,2], cmap = 'gray')

#Remove Red Colour
img_test[:, :, 0] = 0

plt.imshow(img_test)

#Remove Green Colour
img_test[:, :, 1] = 0

plt.imshow(img_test)

#Remove Blue Colour
img_test[:, :, 2] = 0

plt.imshow(img_test)

# 2. OpenCV

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

#Import OpenCV
import cv2

#Get the image with the imread
img = cv2.imread('images/rock.jpg')

#Always check the type
img.shape

#Let's see the image with the imshow
plt.imshow(img)

#     Until now we were working with Matplotlib and RGB.
##    OpenCV is reading the channel as BGR.

#We will convert OpenCV to the channels of the photo.
img_fix = cv2.cvtColor(img, 
       
                       cv2.COLOR_BGR2RGB)
plt.imshow(img_fix)

#Scale it to Gray and check the Shape
img_gray = cv2.imread('images/rock.jpg',
                     cv2.IMREAD_GRAYSCALE)

img_gray.shape

plt.imshow(img_gray, cmap='gray')

#Resize the image
#To resize the image we change the Height Width --> Width Height
img_new = cv2.resize(img_fix,
                    (1000, 400))

plt.imshow(img_new)

#Resize with Ratio
width_ratio = 0.5
height_ratio = 0.5

img2 = cv2.resize(img_fix,
                 (0,0),
                 img_fix,
                 width_ratio,
                 height_ratio)

plt.imshow(img2)

img2.shape

#Flip on Horizontal Axis
img_3 = cv2.flip(img_fix, 0)

plt.imshow(img_3)

#Flip on Vertical Axis
img_3 = cv2.flip(img_fix, 1)

plt.imshow(img_3)

#Flip on Horizontal and on Vertical Axis
img_3 = cv2.flip(img_fix, -1)

plt.imshow(img_3)

#Change the size of our canva
last_img = plt.figure(figsize=(10,7))
ilp = last_img.add_subplot(111)
ilp.imshow(img_fix)


# In[ ]:




