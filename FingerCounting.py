import cv2
import HandTrackingModule as htm

wCam, hCam = 640, 480

# Capturing video
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(fingers)
        totalFingers = fingers.count(1)
        print(fingers, totalFingers)

        # To show the count of fingers on screen
        cv2.putText(img, str(totalFingers), (50, 100), cv2.FONT_HERSHEY_PLAIN,
                    7, (255, 255, 0), 10)

    cv2.imshow("Count your Fingers", img)
    k = cv2.waitKey(1)
    if ord('q') == k:
        break
