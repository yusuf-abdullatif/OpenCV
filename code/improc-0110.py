import cv2
import numpy
def show_webcam(mirror=False):
    ddepth = cv2.CV_8U
    kernel_size = 3
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        imgSift = img.copy()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        grayLaplace = cv2.Laplacian(gray, ddepth, ksize=kernel_size)

        # Applying SIFT detector
        sift = cv2.SIFT_create()
        kp, descriptor = sift.detectAndCompute(grayLaplace, None)
        
        # Marking the keypoint on the image using circles
        imgSift=cv2.drawKeypoints(grayLaplace,
                            kp ,
                            imgSift,
                            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        if mirror: 
            img = cv2.flip(img, 1)
            imgSift = cv2.flip(imgSift, 1)
        cv2.imshow('my webcam', img)
        cv2.imshow('SIFT', imgSift)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()
def main():
    show_webcam(mirror=True)
if __name__ == '__main__':
    main()
