# -*- coding: utf-8 -*
import numpy as np
import cv2 as cv

def reco_webcam():

   face_cascade = cv.CascadeClassifier('C:/Users/Proprietaire/facerecognition/haarcascade/haarcascade_frontalface_default.xml')
   eye_cascade = cv.CascadeClassifier('C:/Users/Proprietaire/facerecognition/haarcascade/haarcascade_eye.xml')

   #Webcam capture
   video_capture = cv.VideoCapture(0)
   while True :
       ret, frame = video_capture.read()
       frame = cv.flip(frame, 1)

       gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray, 1.3, 5)


       for (x,y,w,h) in faces:
           cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
           eyes = eye_cascade.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eyes:
               cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
       cv.imshow('img',frame)
       if cv.waitKey(1) == 27:
           break  # esc to quit
   cv.destroyAllWindows()

#reco_webcam()


def detectionimage ():
    face_cascade = cv.CascadeClassifier('C:/Users/Proprietaire/facerecognition/haarcascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('C:/Users/Proprietaire/facerecognition/haarcascade/haarcascade_eye.xml')
    img = cv.imread('C:/Users/Proprietaire/facerecognition/data/herve-biausser.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv.imshow('img',img)
    cv.waitKey(0)
    cv.destroyAllWindows()

detectionimage()
