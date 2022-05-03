import pyrebase
import os

def upload1():
    config ={
        "apiKey": "AIzaSyAC4EU24xjMQKXP-41I1TnRDIT4KTN7CV8",
        "authDomain": "proxy-detection-1df22.firebaseapp.com",
        "databaseURL": "https://proxy-detection-1df22.firebaseio.com",
        "projectId": "proxy-detection-1df22",
        "storageBucket": "proxy-detection-1df22.appspot.com",
        "messagingSenderId": "17187188207",
        "appId": "1:17187188207:web:63e8c1f5b50862b1c59a1a",
        "vmeasurementId": "G-EPTQX1DS4L"
    }

    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()

    path ="Dataset"
    root = ""

    for (root,dirs,files) in os.walk(path, topdown=True): 
        print (root )
        print (dirs )
        # for images in os.listdir(root):
        #      path= os.path.join(root,images)
        #      print(path)
        #      path_cloud = path
        #      # storage.child("Dataset").put(str(path))
        path =os.path.join(root)
    print(path)
    for images in os.listdir(root):
            path= os.path.join(root,images)
            path_cloud = path
            path_cloud = path_cloud.replace('\\','/')
            print(path_cloud)
            storage.child(path_cloud).put(str(path))     

    print("\n******* Files Upload Successfully  *********\n")    
