import cv2
import numpy as np

#to output the video
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', forcc, 20.0, (640,480))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #if needs to be converted to grayscale
    #out.write(frame) # to ouput video
    cv2.imshow('frame', frame)
    #cv2.imshow('gray', gray) #if needs to be converted to grayscale
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.relase() #output the video
cv2.destroyAllWindows()
