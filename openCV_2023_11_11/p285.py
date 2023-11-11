import cv2

img = cv2.imread('block.jpg')
cv2.imshow('img', img)
# キー入力があるまで待機
cv2.waitKey(0)
# すべてのウィンドウを破棄
cv2.destroyAllWindows()

height = img.shape[0]
width = img.shape[1]
res_img = cv2.resize(img, (int(width/2), int(height/2)))
cv2.imshow('img', res_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('resized.jpg', res_img)