import mediapipe as mp
import cv2 


mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow("holistic", frame)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
cap.release()
cap.destroyAllWindows()
