import cv2
import time 

 # Use VideoCapture(2) for external camera
#For debug
def breakpoint():
    inp = input("Waiting for input")

# cam_1 = 2; cam_2 = 4 @ aprilgrid
def multicam_capture():
    cam_1 = cv2.VideoCapture(2)
    cam_2 = cv2.VideoCapture(4)
    # cv2.namedWindow("test",cv2.WINDOW_NORMAL)
    img_counter = 0

    while True:
        ret_1, frame_1 = cam_1.read()
        ret_2, frame_2 = cam_2.read()
        timestamp = int(time.time() * 100000)
        # print("timestampe",timestamp)
        # breakpoint()
        # if not ret:
        #     print("failed to grab frame")
        #     break
        cv2.imshow("frame_1", frame_1)
        cv2.imshow("frame_2",frame_2)
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed    
            # for i in range(0,3):
            # img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite("/home/panini/30april/cam1/" + str(timestamp) + ".png" , frame_1)
            cv2.imwrite("/home/panini/30april/cam2/" + str(timestamp) + ".png", frame_2)
            # print("{} written!".format(img_name))
            print("Written!")
            img_counter += 1
                

    cam_1.release()
    cam_2.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    multicam_capture()