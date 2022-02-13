import cv2
import face_recognition
 
imgsaad = face_recognition.load_image_file('Imagebasic/saad.jpg')
imgsaad = cv2.cvtColor(imgsaad,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Imagebasic/saad test.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
 
faceLoc = face_recognition.face_locations(imgsaad)[0]
encodesaad = face_recognition.face_encodings(imgsaad)[0]
cv2.rectangle(imgsaad,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodesaad], encodeTest)
faceDis = face_recognition.face_distance([encodesaad], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('saad', imgsaad)
cv2.imshow('saad Test', imgTest)
cv2.waitKey(0)

 
