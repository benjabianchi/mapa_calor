import numpy as np
import cv2
import copy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--video', type=str, required=True)
parser.add_argument('--realtime', type=str, required=True)
args = parser.parse_args()
video_path = args.video
real_time = args.realtime
def heatmap(video_path,real_time):
    if video_path == "0":
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture("../data/market.mp4")
    # pip install opencv-contrib-python
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

    # number of frames is a variable for development purposes, you can change the for loop to a while(cap.isOpened()) instead to go through the whole video
    num_frames = 10000

    first_iteration_indicator = 1
    for i in range(0, num_frames):
        '''
        There are some important reasons this if statement exists:
            -in the first run there is no previous frame, so this accounts for that
            -the first frame is saved to be used for the overlay after the accumulation has occurred
            -the height and width of the video are used to create an empty image for accumulation (accum_image)
        '''
        if (first_iteration_indicator == 1):
            ret, frame = cap.read()
            first_frame = copy.deepcopy(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            height, width = gray.shape[:2]
            accum_image = np.zeros((height, width), np.uint8)
            first_iteration_indicator = 0
        else:
            ret, frame = cap.read()  # read a frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert to grayscale

            fgmask = fgbg.apply(gray)  # remove the background

            # for testing purposes, show the result of the background subtraction
            # cv2.imshow('diff-bkgnd-frame', fgmask)

            # apply a binary threshold only keeping pixels above thresh and setting the result to maxValue.  If you want
            # motion to be picked up more, increase the value of maxValue.  To pick up the least amount of motion over time, set maxValue = 1
            thresh = 2
            maxValue = 2
            ret, th1 = cv2.threshold(fgmask, thresh, maxValue, cv2.THRESH_BINARY)
            # for testing purposes, show the threshold image
            # cv2.imwrite('diff-th1.jpg', th1)

            # add to the accumulated image
            accum_image = cv2.add(accum_image, th1)
            # for testing purposes, show the accumulated image
            # cv2.imwrite('diff-accum.jpg', accum_image)

            # for testing purposes, control frame by frame
            # raw_input("press any key to continue")

        # for testing purposes, show the current frame
        new_frame = cv2.applyColorMap(accum_image, cv2.COLORMAP_HOT)
        size = 240

        resize_frame= cv2.resize(new_frame, (size, size))

        color_image = im_color = cv2.applyColorMap(accum_image, cv2.COLORMAP_HOT)
            # for testing purposes, show the colorMap image
            # cv2.imwrite('diff-color.jpg', color_image)

            # overlay the color mapped image to the first frame
        result_overlay = cv2.addWeighted(frame, 0.7, color_image, 0.9, 0)
        result_overlay = cv2.resize(result_overlay, (720,720))
        #resize_frame = cv2.resize(result_overlay, (size, size))
        if real_time == "True":
            cv2.imshow('Termo Camara', result_overlay)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # apply a color map
    # COLORMAP_PINK also works well, COLORMAP_BONE is acceptable if the background is dark
    #color_image = im_color = cv2.applyColorMap(accum_image, cv2.COLORMAP_HOT)
    # for testing purposes, show the colorMap image
    # cv2.imwrite('diff-color.jpg', color_image)

    # overlay the color mapped image to the first frame
    #result_overlay = cv2.addWeighted(first_frame, 0.7, color_image, 0.9, 0)

    # save the final overlay image
    print("Guardando imagenes...")
    cv2.imwrite('../output/diff-overlay.jpg', result_overlay)
    #image = cv2.imread("../output/diff-overlay.jpg")
    #cv2.imshow("image",color_image)
    #cv2.imshow("image",result_overlay)
    cv2.imwrite('../output/colors.jpg', color_image)
    print("Imagenes guardadas!")
    # cleanup
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    print("Corriendo")
    heatmap(video_path,real_time)
