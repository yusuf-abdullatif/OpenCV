import cv2
# OpenCV DNN
#source: https://github.com/patrick013/Object-Detection---Yolov3/blob/master/model/yolov3.weights
#another source: https://learnopencv.com/deep-learning-based-object-detection-using-yolov3-with-opencv-python-c/
net = cv2.dnn.readNet('model/yolov3.weights', 'model/yolov3.cfg')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255, swapRB=True)
# Initialize Camera
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        (class_ids, scores, bboxes) = model.detect(frame)
        for class_id, score, bbox in zip(class_ids, scores, bboxes):
            (x, y, w, h) = bbox
            cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 0, 50), 3)
        cv2.imshow('Camera image', frame)
        k = cv2.waitKey(100)
        if k==ord('q'):
            break
    else:
        print('ERROR ---> Camera not found!')

cv2.destroyAllWindows()

