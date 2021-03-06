import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

im= cv2.imread("C:/Users/Anshul/PycharmProjects/Opencv/Resources/car.jpg")
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
print("number of cars is: "+ str(label.count("car")))