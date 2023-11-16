import cv2

img = cv2.imread('block.jpg')
print(img)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
height = img.shape[0]
width = img.shape[1]
resized_img = cv2.resize(img, (int(width/2), int(height/2)))
cv2.imwrite('resized.jpg', resized_img)
# cv2.imshow('resized_img', resized_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

gray_img = cv2.cvtColor(resized_img, cv2.COLOR_RGB2GRAY)
cv2.imwrite('gray.jpg', gray_img)
# cv2.imshow('gray_img', gray_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

canny_img = cv2.Canny(resized_img, 50, 100)
cv2.imwrite('canny.jpg', canny_img)
cv2.imshow('canny_img', canny_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
