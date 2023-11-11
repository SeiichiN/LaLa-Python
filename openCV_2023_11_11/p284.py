import cv2

img = cv2.imread('block.jpg')
cv2.imshow('img', img)
# キー入力があるまで待機
cv2.waitKey(0)
# すべてのウィンドウを破棄
cv2.destroyAllWindows()
