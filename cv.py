import cv2

im_path = 'hello.jpg'
img = cv2.imread(im_path)
print (img.shape)

orig = img.copy()
gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5,5), 0)

regen = cv2.cvtColor(blurred,cv2.COLOR_GRAY2BGR)

edged = cv2.Canny(blurred, 0, 50)
# orig_edged = edged.copy()








cv2.imshow('ImageWindow', edged)
cv2.waitKey()