import time
import cv2 
from flask import Flask,redirect,url_for,render_template,request,Response

app=Flask(__name__)

# @app.route('/WebCam',methods=['GET','POST'])
# def video_feed():
#     """Video streaming route. Put this in the src attribute of an img tag."""
#     return Response(gen(),
#                     mimetype='multipart/x-mixed-replace; boundary=frame'),render_template('Thank.html')




@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        # Handle POST Request here
        select = request.form.get('comp_select')
        print(select)
        return Response(gen()),render_template('Thank.html')
    year=[{'name':'SE'}, {'name':'TE'}, {'name':'BE'}]
    div = [{'name':'A'}, {'name':'B'}, {'name':'C'}]
    return render_template('index.html',data=year,div=div)

# app = Flask(__name__)

# @app.route('/',method=['GET','POST'])
# def index():
#     if request.method == 'POST':
#         return render_template('index.html')
#     """Video streaming home page."""
#     return render_template('index1.html')


def gen():
    """Video streaming generator function."""
    cap1 = cv2.VideoCapture(0)

    # set is used to set size  3 = width 4 = height 10 = set briteness 

    while True:
        # read() returns bool and img a
        succ2 , img2 =cap1.read()
        img4 = cv2.resize(img2,(700,480))
        # To detect Edges canny image = all black with with white borders.
        # TO convert to Gray Scale
        # Functions to show image output
        cv2.imshow("My WEB_ CAM",img4)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   
            
if __name__ == '__main__':
    app.run(debug=True)
    