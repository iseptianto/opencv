import cv2
image=cv2.imread("white.png")

cv2.circle(image,(100,100),50,(250,0,0),2)

cv2.rectangle(image,(10,10),(50,50),(250,0,0),3)

cv2.line(image, (5, 5), (300,300),(0,0,255),1)

cv2.imshow("CIRCLE",image)

#necessary

cv2.waitKey(0)
cv2.destroyAllWindows