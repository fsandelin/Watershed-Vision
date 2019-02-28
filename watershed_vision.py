import cv2
import numpy as np
from colors import create_colorMap

IMG_URL = 'images/1.JPG'
WINDOW_NAME_IMAGE = 'Image'
WINDOW_NAME_WATERSHED = 'Watershed Segmentation'
IMG_SIZE_MULTIPLIER = 0.5

def original_image_clicked(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_image, (int(x/IMG_SIZE_MULTIPLIER), int(y/IMG_SIZE_MULTIPLIER)), 10, (current_marker), -1)
        cv2.circle(img_copy, (int(x/IMG_SIZE_MULTIPLIER), int(y/IMG_SIZE_MULTIPLIER)), 10, colors[current_marker], -1)


img = cv2.imread(IMG_URL)
img_copy = img.copy()
marker_image = np.zeros(img.shape[:2], dtype=np.int32)
segments = np.zeros(img.shape, dtype=np.uint8)

cv2.namedWindow(WINDOW_NAME_IMAGE)
cv2.namedWindow(WINDOW_NAME_WATERSHED)
cv2.setMouseCallback(WINDOW_NAME_IMAGE, original_image_clicked, dict())

colors = create_colorMap()
current_marker = 1
n_markers = 10

while True:
  cv2.imshow(WINDOW_NAME_WATERSHED, cv2.resize(segments, (0, 0), fx=IMG_SIZE_MULTIPLIER, fy=IMG_SIZE_MULTIPLIER))
  cv2.imshow(WINDOW_NAME_IMAGE, cv2.resize(img_copy, (0, 0), fx=IMG_SIZE_MULTIPLIER, fy=IMG_SIZE_MULTIPLIER))

  marker_image_copy = marker_image.copy()
  cv2.watershed(img, marker_image_copy)
  segments = np.zeros(img.shape, dtype = np.uint8)
  
  for color_ind in range(n_markers):
      segments[marker_image_copy == color_ind] = colors[color_ind]

  k = cv2.waitKey(1)
  if k == 27:
      break
  elif k == ord('c'):
      img_copy = img.copy()
      marker_image = np.zeros(img.shape[:2], dtype=np.int32)
      segments = np.zeros(img.shape, dtype = np.uint8)    
  elif k > 0 and chr(k).isdigit():
      current_marker = int(chr(k))

cv2.destroyAllWindows()