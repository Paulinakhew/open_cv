import cv2

path = ""
img = cv2.imread(path)
# img = cv2.imread(path, 0)  # load up photo in grayscale

# Adaptive Mean Thresholding
# img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Adaptive Gaussian Thresholding
# img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)

if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img, point1, point2, color=(255, 23, 25), thickness=2)

cv2.imshow(path, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
