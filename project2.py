import cv2
image=cv2.imread("white.png")
text="Python is very amazing"
position =(50,50)
font=cv2.FONT_HERSHEY_SIMPLEX
font_scale=1
color=(0,1,230)
thickness=2
cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

resized_image = cv2.resize(image, (300, 300))
cv2.imshow("Text on image", resized_image)


cv2.circle(image,(100,100),50,(250,0,0),2)

cv2.rectangle(image,(10,10),(50,50),(250,0,0),3)

cv2.line(image, (5, 5), (300,300),(0,0,255),1)

cv2.imshow("CIRCLE",image)

#necessary

cv2.waitKey(0)
cv2.destroyAllWindows