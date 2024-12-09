import cv2  # import package for image caputuring and proccessing
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)   # Initiating video caputring , Here zero(0) indicates the first device camera
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)  # To access particular point of the face, we use refine funtion
screen_w, screen_h = pyautogui.size()
while True:  # intiting loop for camera
    _, frame = cam.read()  # to read the caputered image
    frame = cv2.flip(frame, 1)  # to flip the camera angle according to our face
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # converting normal image to RGB image  for better image identifcaton
    output = face_mesh.process(rgb_frame)  # storing the converted rgb image in a variable
    landmark_points = output.multi_face_landmarks  # capute the x,y location of the face
    frame_h, frame_w, _ = frame.shape  # Taking refrence using the shpae of the op screen
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):   # This describe the particular eye  # enumerate funtion is used to use the particular number using the id ,for the referece our eye has four points , in that we are using one as the curser.
            x = int(landmark.x * frame_w)     # convering the float value into int  //
            y = int(landmark.y * frame_h)     # //
            cv2.circle(frame, (x, y), 3, (0, 255, 0))     # (0,255,0) gives green color
            if id == 1 :
                screen_x = screen_w / frame_w * x   # To increase the range of the curser on the screen
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145],landmarks[159]]
        for landmark in left:  # for the other eye
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)

    cv2.imshow("Eye_controller", frame)   # To show caputred fotage
    cv2.waitKey(1)   # show the output, by delaying 1sec


    cv2.waitKey(1)   # show the output, by delaying 1sec

