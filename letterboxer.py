import cv2
import numpy as np
import os
import sys


def add_letterboxed(path):
    directory, filename = os.path.split(path)
    name, ext = os.path.splitext(filename)
    new_name = name + '_letterboxed' + ext
    return os.path.join(directory, new_name)


if len(sys.argv) < 2:
    print("Usage: python letterboxer.py <path to image>")
    sys.exit(1)

if not isinstance(sys.argv[1], str):
    print("Error: <path to image> must be a string")
    sys.exit(1)

image_path = str(sys.argv[1])
image_name = os.path.basename(image_path)

image = cv2.imread(image_path)
image_height, image_width = image.shape[:2]

black_image = np.zeros((image_height, image_width, 3), np.uint8)

frame_ratio = float(sys.argv[2]) / 2 if len(sys.argv) == 3 else 0.1 / 2

upper_box = int(image_height - (image_height * frame_ratio))
lower_box = int(image_height * frame_ratio)
black_image[0:lower_box, :] = 255
black_image[upper_box:image_height, :] = 255

final_image = cv2.subtract(image, black_image)
cv2.imshow("Final result", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(add_letterboxed(image_path), final_image)
