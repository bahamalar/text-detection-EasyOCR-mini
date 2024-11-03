import os
import cv2
import easyocr
import matplotlib.pyplot as plt


# read image
input_dir = './data'

for i in sorted(os.listdir(input_dir)):
    img = cv2.imread(os.path.join(input_dir, i))

    # instance text detector
    reader = easyocr.Reader(['en'], gpu=True)


    # detect text on image
    text = reader.readtext(img)


    # draw bbox and text
    threshold = 0.25

    for t in text:
        print(t)

        bbox, text, score = t

        if score > threshold:
            cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 5)
            cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255,0,0), 2)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # bgr -> rgb for matplotlib
    plt.show()