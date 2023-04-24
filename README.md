# add-letterboxes

Add letterboxes to an image

---

## Setup

`pip3 install opencv-python`

`pip3 install numpy`

---

## Instructions

`python letterboxer.py path to image <0-1>`

Replace `<path to image>` with your image file

(Optional) Replace `0-1` with any value between 0 and 1 corresponding to the percentage you want the resulting letterbox to take up

**Default value is 0.1**

0 = No letterbox (the full image remains)

1 = Full letterbox (all black)

0.5 = Half letterbox (half the image remains)

Once the image has been generated, it will show on screen. Press any key to exit and it will be saved in the same directory as your original image
