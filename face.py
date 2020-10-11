import time
import cv2 
from flask import Flask,redirect,url_for,render_template,request,Response
import os

path = "Dataset\SE\A\d.rohan1927"
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

i=0
while(cap.isOpened()):
          # Capture frame-by-frame
        ret, img = cap.read()
        if ret == True:
            img = cv2.resize(img, (0,0), fx=0.6, fy=0.6) 
            frame = cv2.imencode('.jpg', img)[1].tobytes()
        
            grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(grayImage, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_color = img[y:y + h, x:x + w]
                roi_gray=grayImage[y:y+h,x:x+w]
                print(str(i)+" Object found. Saving locally.") 
                cv2.imwrite(str(path)+'/'+str(i)+".jpg",roi_gray) 
                i=i+1
                cv2.imshow("my wi",roi_gray)
            cv2.imshow('img', img)
            k = cv2.waitKey(30) & 0xff
            if k==27:
                break
            time.sleep(1)
                
        else:
            break       