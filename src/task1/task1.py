#!/usr/bin/env python3

######### Task 1 ##########
# Create a class VideoPlayer. The class must have:
# 1. A constructor
# 2. One class method to display the frames
###########################

# Import required python modules
import numpy as np
import cv2 as cv
import os

# Get current working directory and prints it
cdir = os.getcwd()
print(cdir)

class VideoPlayer:
    def __init__(self):
        # initialize the video capture
        self.cap = cv.VideoCapture(cdir+"/src/test_video.mp4")

        # Checks if video file is valid
        if not self.cap.isOpened():
            print("Cannot open video file")
            # if video file invalid, we exit code.
            # No need to process rest of the code
            exit()

    # function for displaying video capture
    def display(self):
        # if video file is valid, we read the frames one by one and display it
        while True:
            # Capture frame-by-frame
            # using read method of VideoCapture class
            # This function requires 2 things, the frame and a boolean, flagging a frame
            # has been read correctly
            ret, frame = self.cap.read()

            # We use boolean to indicate user, if video ended 
            # or unexpected error
            if not ret:
                print("Can't recieve fram (video ended?). Exiting ...")
                # If no longer recieving frame, break from while loop
                break
                
            # If everything goes well, we have a frame
            # displays the resulting frame
            cv.imshow('frame', frame)

            # Press 'q' to exit display early
            if cv.waitKey(1) == ord('q'):
                break
        
        # when everything done, release capture
        self.cap.release()

# Holds main high level logic that gets executed when python file is called
def main():
    # Create Video_Player object
    Video_Player = VideoPlayer()

    # calls display function to display the capture
    Video_Player.display()

    # when completed, closes all windows
    cv.destroyAllWindows()

# Call the main function
if __name__ == "__main__":
    main()