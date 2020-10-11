import time
import cv2 
from flask import Flask,redirect,url_for,render_template,request,Response

app=Flask(__name__)

@app.route('/video_feed',methods=['GET','POST'])
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    if request.method=='GET':
    
        return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    print("Post")                
    return render_template('Thank.html')


@app.route('/WebCam')
def stuff():
    return render_template('Thank.html')



@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        # Handle POST Request here
        select = request.form.get('comp_select')
        print(select)
        return render_template('WebCam.html')
    year=[{'name':'SE'}, {'name':'TE'}, {'name':'BE'}]
    div = [{'name':'A'}, {'name':'B'}, {'name':'C'}]
    return render_template('index.html',data=year,div=div)

# app = Flask(__name__)

# @app.route('/',method=['GET','POST'])
# def index():
#     if request.method == 'POST':
#         return render_template('WebCam.html')
#     """Video streaming home page."""
#     return render_template('index.html')


def gen():
    """Video streaming generator function."""
    cap = cv2.VideoCapture(0)

    while(cap.isOpened()):
          # Capture frame-by-frame
        ret, img = cap.read()
        if ret == True:
            img = cv2.resize(img, (0,0), fx=0.6, fy=0.6) 
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)
             
        else:
            break       

    cap.release()

            
if __name__ == '__main__':
    app.run(debug=True)
    