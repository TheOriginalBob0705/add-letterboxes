import numpy as np
import cv2

image = cv2.imread("screencap.png")
image_height, image_width = image.shape[:2]

black_image = np.zeros((image_height, image_width, 3), np.uint8)

frame_ratio = 0.90

lower_box = int(image_height - (image_height * frame_ratio))
upper_box = int(image_height * frame_ratio)
black_image[0:lower_box, 0:image_width] = 255
black_image[upper_box:image_height, 0:image_width] = 255

final_image = cv2.subtract(image, black_image)

cv2.imshow('result', final_image), cv2.waitKey(0)
cv2.destroyAllWindows()
