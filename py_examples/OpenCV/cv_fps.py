
import numpy as np
import time
import cv2

cap = cv2.VideoCapture(0)
total_time = 0;
frame_count = 0;
while(True):
    start_time = time.time()
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    #print("                                  ",time.time())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    end_time = time.time()
    frame_count += 1;
    total_time += end_time-start_time
    if frame_count % 100 == 0:
        print(frame_count/total_time)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
