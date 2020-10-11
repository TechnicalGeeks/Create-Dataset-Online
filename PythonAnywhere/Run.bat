start /B python flask_app.py
start /B /W "" "http://127.0.0.1:5000/"


echo ********* Wait of Process to Finishs ****************
start "" python upload.py
pause
