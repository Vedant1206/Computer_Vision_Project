from base64 import encodebytes
import cv2
import numpy as np
import face_recognition as fr
import os

path = 'Resources\People'
images = []
names = []
list = os.listdir(path)
print(list)

for i in list:
    curImg = cv2.imread(f'{path}/{i}')
    images.append(curImg)
    names.append(os.path.splitext(i)[0])
print(names)

def findEncoding(images):
       encodeList = []
       for img in images:
           #we have to convert in rgb
           img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
           encode = fr.face_encodings(img)[0]
           encodeList.append(encode)
       return encodeList

encodeKnownList = findEncoding(images)
print('Encoding complete')#len(encodeKnownList))

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    #resizing it because it will be faster
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesFrame = fr.face_locations(imgS)
    encodesFrame = fr.face_encodings(imgS, facesFrame)

    for encodeFace, faceLoc in zip(encodesFrame, facesFrame):
        matches = fr.compare_faces(encodeKnownList, encodeFace)
        faceDis = fr.face_distance(encodeKnownList, encodeFace)
        print(faceDis)
        mainIndex = np.argmin(faceDis)
        
        if matches[mainIndex]:
            name = names[mainIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0),2)
            cv2.rectangle(img, (x1,y1-35), (x2,y2), (0,255,0))
            cv2.putText(img, name,(x1+5, y2-5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255,255), 2)


    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):  # waitkey returns the value of the key so if we press d, break
            break

cv2.destroyAllWindows()