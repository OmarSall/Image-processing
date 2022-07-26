import cv2

img = cv2.imread("galaxy.jpg",0)

#in python image is a number array

print(type(img))
print(img)

print(img.shape)            #resolution
print(img.ndim)

resized_image = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))      #(width, height)

cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg",resized_image)
cv2.waitKey(0)       #holds for 2 s, if you have 0 the programm will wait when you press the button
cv2.destroyAllWindows()