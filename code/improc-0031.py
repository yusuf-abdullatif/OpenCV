import pyrealsense2 as rs
import numpy as np
import cv2
import datetime
# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()
# Get device product line for setting a supporting resolution
pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))

found_rgb = False
for s in device.sensors:
    if s.get_info(rs.camera_info.name) == 'RGB Camera':
        found_rgb = True
        break
if not found_rgb:
    print("The demo requires Depth camera with Color sensor")
    exit(0)

config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
if device_product_line == 'L500':
    config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
else:
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
# Start streaming
pipeline.start(config)

# Initialize Camera
cap = cv2.VideoCapture(1)
ret, frame = cap.read()
x = datetime.datetime.now()
fileRGB = 'outRGB'+str(x.year)+str(x.month)+str(x.day)+str(x.hour)+str(x.minute)+str(x.second)+'.avi'
outRGB = cv2.VideoWriter(fileRGB,cv2.VideoWriter_fourcc(*'MJPG'), 30, (frame.shape[1],frame.shape[0]))
numberOfImagesInVideo = 300
nb = 0

try:
    while True:
        # we read an image from the camera
        ret, frame = cap.read()
        # there is an image
        if ret:
            frame = cv2.flip(frame, flipCode = 1)
            if nb<numberOfImagesInVideo:
                outRGB.write(frame)
                nb += 1
            # we display it
            cv2.imshow('Camera image', frame)
        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue
        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        depth_image = cv2.flip(depth_image, flipCode = 1)
        color_image = np.asanyarray(color_frame.get_data())
        color_image = cv2.flip(color_image, flipCode = 1)

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        depth_colormap_dim = depth_colormap.shape
        color_colormap_dim = color_image.shape

        # If depth and color resolutions are different, resize color image to match depth image for display
        if depth_colormap_dim != color_colormap_dim:
            resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], 
                                                    depth_colormap_dim[0]), interpolation=cv2.INTER_AREA)
            images = np.hstack((resized_color_image, depth_colormap))
        else:
            images = np.hstack((color_image, depth_colormap))
        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
        k = cv2.waitKey(10)
        if k==ord('q'):
            break
finally:
    # Stop streaming
    pipeline.stop()
    cv2.destroyAllWindows()
    outRGB.release()
