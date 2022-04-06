import cv2
cap = cv2.VideoCapture("http://192.168.2.112:4747/video")
while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue
    cv2.imshow("pose", cv2.flip(image, 1))

    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()

