import cv2, time
#first, we need to read a video file

video=cv2.VideoCapture(0) #0,1,2,3,... (from webcam) or filepath

while True:
    check, frame = video.read() #boolean and numpyarr

    #print(check)
    #print(frame)
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #nat = cv2.cvtColor(frame,cv2.COLOR_BGR2Luv)
    #time.sleep(3)
    #cv2.imshow("Capturing",gray)
    cv2.imshow("Capturing",frame)

    cv2.waitKey(1)
    #key=cv2.waitKey(10)
    #if key==ord('q'):
    #    break
    
video.release()


cv2.destroyAllWindows()
