
import cv2
import numpy as np
import face_recognition as fr
if __name__ == '__main__':
    #Ben Afflek/1.jpg
    #get true for Elton John/2.jpg and Elton John/3.jpg
    img_ben = fr.load_image_file('Resources/ben_afflek/2.jpg')
    img_ben = cv2.cvtColor(img_ben, cv2.COLOR_BGR2RGB)
    img_ben2 = fr.load_image_file('Resources/ben_afflek/5.jpg')
    img_ben2 = cv2.cvtColor(img_ben2, cv2.COLOR_BGR2RGB)


    #gives the position points for making rectangle across face
    face_location = fr.face_locations(img_ben)[0] #because we are sending 1 image, so we need first element of this
    #now we encode the face
    encode_ben = fr.face_encodings(img_ben)[0]
    cv2.rectangle(img_ben, (face_location[3], face_location[0]), (face_location[1], face_location[2]), (255, 0, 255), 2)
    
    #gives the position points for making rectangle across face
    face_location2 = fr.face_locations(img_ben2)[0] #because we are sending 1 image, so we need first element of this
    #now we encode the face
    encode_ben2 = fr.face_encodings(img_ben2)[0]
    cv2.rectangle(img_ben2, (face_location2[3], face_location2[0]), (face_location2[1], face_location2[2]), (255, 0, 255), 2)

    
    results = fr.compare_faces([encode_ben], encode_ben2)
    faceDis = fr.face_distance([encode_ben], encode_ben2)
    print(results, faceDis)
    #bacuse we have fasDis in decimal points, we are using np.round, 50,50 is the position
    cv2.putText(img_ben2, f'{results} {np.round(faceDis,2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

    
    #cv2.putText(img_ben, 20)

    cv2.imshow('Ben', img_ben)
    cv2.imshow('Ben1', img_ben2)

    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
