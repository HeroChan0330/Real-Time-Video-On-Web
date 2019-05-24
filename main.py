#coding:utf8
import sys
import Ctrl
reload(sys)
sys.setdefaultencoding('utf8')
#fucking problem of py 2.* 


# from SimpleCV import Image,Camera
import cv2
import thread,threading
import time
# import ctypes

# from PyLib.FindPipe import *
# from PyLib.FindOilPoint import *
# from PyLib.FishCtrl import *

from flask import Flask, render_template, Response,url_for,send_file,request

networkServer=Flask(__name__,static_folder='static')


def responseImgStream():
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
    if not video.isOpened():
        return
    try:
        while True:
            success, image = video.read()
            ret, jpeg = cv2.imencode('.jpg', image)
            frame=jpeg.tostring()
            # print("frame:",frame)
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            # print("Send stream to client")
    except:
        print("connect lose or fail to capture image")
    finally:
        # if video.isOpened():
        #     video.release()
        pass

@networkServer.route('/command',methods=["GET"])
def command():
    comm=request.args.get('comm')
    val=request.args.get('val')
    if comm=='SetDir':
        Ctrl.dirBtnPress(val)
    elif comm=='ReleaseDir':
        Ctrl.dirBtnRelease(val)
    return "success"

@networkServer.route('/ImgRaw')
def ImgRaw():
    return Response(responseImgStream(),mimetype='multipart/x-mixed-replace; boundary=frame')





def run():
    global networkServer
    with networkServer.test_request_context():
        url_for('static', filename='index.html')
        url_for('static', filename='Video.html')
    networkServer.run(host='0.0.0.0',port=6677)
    
if __name__=="__main__":
    run()
