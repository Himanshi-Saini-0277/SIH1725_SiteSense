import cv2
import os

video = cv2.VideoCapture(0)

imageDetect = cv2.CascadeClassifier('SIH1725_SiteSense/SiteSense/haarcascade_frontalface_default.xml')
count = 0

nameID = str(input("Enter Day number: ")).lower()
path = os.path.join('SIH1725_SiteSense', 'SiteSense', 'static', 'Images', nameID)

Exist = os.path.exists(path)

if Exist:
    print("Name Already Taken")
    nameID = str(input("Enter Day Number Again: ")).lower()
    path = os.path.join('SIH1725_SiteSense', 'SiteSense', 'static', 'Images', nameID)
    os.mkdir(path)
else:
    os.mkdir(path)
    
while True:
    ret, frame = video.read()
    if not ret:
        break

    faces = imageDetect.detectMultiScale(frame, 1.3, 5)
    for x, y, w, h in faces:
        count += 1
        filename = os.path.join(path, f'{count}.jpg')
        print("Creating images: " + filename)
        cv2.imwrite(filename, frame[y:y+h, x:x+w])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
    cv2.imshow("Window Frame", frame)
    if count > 10:
        break
    
video.release()
cv2.destroyAllWindows()
