import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)

yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])

prev_y = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i in contours:
        area = cv2.contourArea(i)
        if area > 300:
            x, y, w, h = cv2.boundingRect(i)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            #cv2.drawContours(frame, i, -1, (0, 255, 0), 2) #(Support)

            if y < prev_y:
                pyautogui.press("space")
            prev_y = y

    #cv2.imshow("mask", mask) #(Support)

    cv2.imshow("Virtual PC Controller (Developed By - Jay Banerjee", frame)
    if cv2.waitKey(10) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
