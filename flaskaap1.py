from flask import Flask, render_template, Response,jsonify,request,session
#importing all required libraries
#we need render_template to render html 
#Response,jsonify to convert our output into jsonnify format
#response,session to store confidence value path

import cv2
#cv2 to run yolov7 model

from hubconfCustom import video_detection
app = Flask(__name__)#initializing flask


app.config['UPLOAD_FOLDER'] = 'static/files'#input videos to run detection are stored here

def generate_frames(path_x = '',conf_ = 0.2): #it takes the path of input video file and confidence and gives the output with boundary boxes around detected objects, also we get the frmae rate ,video size,total objects detected
    yolo_output = video_detection(path_x,conf_)
    for detection_,FPS_,xl,yl in yolo_output: # these are those 4 thungs as detected objets , frame resolution etc
        ref,buffer=cv2.imencode('.jpg',detection_)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')#it returns 4 things as object detected in each frame, count of object ,fps and resolution of current frame

@app.route('/video')
def video():
    return Response(generate_frames(path_x=r'C:\Users\mihar\OneDrive\Desktop\minr web\yolov7\static\files\pexels_videos_2103099 (2160p) (online-video-cutter.com) (1).mp4',conf_=0.25), mimetype='multipart/x-mixed-replace; boundary=frame ')

if __name__ == "__main__":
    app.run(debug=True)

