import cv2
from tracker import *

#Create tracker object
tracker = EuclidianDistance()

cap = cv2.VideoCapture("video_1.mp4")

#Object Detection
object_detector = cv2.createBackgroundSubtractorMOG2(history = 100, varThreshold = 40)

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape

    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []

    for cnt in contours:
        #Calculate and remove small elements
        area = cv2.contourArea(cnt)
        if area > 100
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

            detections.append([x, y, w h])

    #Object Tracking
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y -15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        cv2.rectangle(roi, (x,y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.Waitkey(30)
    if key == 27:
        break
       
    cap.release()
    cv2.destroyAllWindows()
