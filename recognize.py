import csv
import cv2
from datetime import datetime

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

names = ['no', 'bala', 'external', '-', '-', '-']


cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
f = open(current_date+'.csv', 'w+')
lmwriter = csv.writer(f)



while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)  # Flip vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])


        if (confidence <= 50):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))

        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(
            img,
            str(id),
            (x + 5, y - 5),
            font,
            1,
            (255, 255, 255),
            2
        )
        cv2.putText(
            img,
            str(confidence),
            (x + 5, y + h - 5),
            font,
            1,
            (255, 255, 0),
            1
        )

        print(id)
        time = now.strftime('%Y-%m-%d %H-%M-%S')
        lmwriter.writerow([id,time])


    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()