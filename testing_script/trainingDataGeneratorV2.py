# import libraries
import cv2 as cv
import mediapipe as mp
import os


# function for detecting the hand
def findHand(img):
    # define mediapipe hands model
    mpHands = mp.solutions.hands
    # hands object to detect and track hands
    hands = mpHands.Hands()
    # convert image to grayscale as preprocessing step
    g_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # return detected hands
    return hands.process(g_img)


# function for finding the rectangular bound of the hand detected
def find_rectangle(img, results):
    # use the height and width of the img as a starting point for the x_min, y_min
    h, w, c = img.shape
    # constant to increase the size of the box
    constant = 100
    # check if hand is detected via landmarks
    if results.multi_hand_landmarks:
        # loop through the detected hand landmarks (landmarks include x,y,z positions)
        for handLMs in results.multi_hand_landmarks:
            # define min and max values for coordinates of rectangle
            x_max = 0
            y_max = 0
            x_min = w
            y_min = h
            # loop through the x,y,z positions of the landmarks
            for lm in handLMs.landmark:
                # logic for finding the upper left corner and lower right corner
                # based on the outer points of the hand
                x, y = int(lm.x * w), int(lm.y * h)
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y
        return x_min - constant, y_min - constant, x_max + constant, y_max + constant
    else:
        return None, None, None, None


# function for getting a square image as input to the sign language interpreter model
def get_cropped_image(img, x1, y1, x2, y2):
    # define resolution constant for image preprocessing
    res = (28, 28)
    # constant to add to build a square
    constant = 200
    # find the center of the rectangle
    x, y = int((x2 + x1) / 2), int((y2 + y1) / 2)
    # define slice bounds
    y_l = y - constant
    y_u = y + constant
    x_l = x - constant
    x_u = x + constant
    # try to slice the numpy array
    try:
        cropped_image = img[y_l:y_u, x_l:x_u]
        # only return an image if it has a square resolution shape
        if cropped_image.shape[0] != cropped_image.shape[1]:
            cropped_image = None
        else:
            cropped_image = cv.resize(cropped_image, res)
    # catching index errors when slicing
    except IndexError:
        cropped_image = None
        print('Index Error')
    # return the cropped image
    # resize the cropped image to 28x28 pixels

    return cropped_image


# function for preprocessing image from video to conform to model input requirements
def img_preprocessing(img, resolution):
    # convert color of image to grayscale
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # convert resolution of image
    img = cv.resize(img, resolution)
    return img


# main function call
def main():
    label = 'A'
    path = "./newTrainingData/" + label + "/"
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory '{path}' created successfully")
    else:
        print(f"Directory '{path}' already exists")

    # CONSTANTS

    # define delay to get image from video feed every number of frames
    interval = 0.1
    # laplacian filter variance threshold
    lap_thres = 60

    # define video capture from camera feed
    cap = cv.VideoCapture(0)
    # fps of video feed
    fps = int(cap.get(cv.CAP_PROP_FPS))
    # frame count
    frame_count = 0

    # check if video is unable to be obtained, and print message
    if cap.isOpened() == False:
        print('Error opening video stream')

    # while video is being captured
    while (cap.isOpened()):
        # read the video from camera feed
        ret, frame = cap.read()
        # if video is being returned

        if ret == True:
            # detect hands
            detection_results = findHand(frame)
            # find rectangular bound around detected hand
            x1, y1, x2, y2 = find_rectangle(frame, detection_results)

            # if bound is found
            if x1:
                # get cropped image for model input if possible
                cropped_img = get_cropped_image(frame, x1, y1, x2, y2)
                # crop28x28 = cropped_img.resize((28, 28))

                # if cropped image is found
                if cropped_img is not None:
                    # increment frame count
                    frame_count += 1
                    # logic for getting image every interval
                    if frame_count % (fps * interval) == 0:

                        # define laplacian filter to detect image if image is blurry (high variance = sharper image)
                        laplacian = cv.Laplacian(frame, cv.CV_64F).var()
                        if laplacian > lap_thres:
                            # REPLACE CODE WITH IMREAD AND PASS INTO MODEL
                            # cv.imshow('Cropped Image',img_preprocessing(cropped_img,res))

                            filename = "cropped_image_{}.jpg".format(frame_count)
                            # Save the cropped image to local storage
                            cv.imwrite(path + filename, cropped_img)
                            print("File saved ", filename)

                # draw rectangular bound in frame if found
                cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # launch window and display
            cv.imshow('Sign Language Interpreter', frame)

            # quit if q is pressed
            if cv.waitKey(25) & 0xFF == ord('q'):
                break

        # quit if video is not returned
        else:
            break
    # release video capture and destroy imshow windows
    cap.release()
    cv.destroyAllWindows()


# entry
if __name__ == '__main__':
    main()
