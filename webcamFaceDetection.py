import cv2
from BlazeFaceDetection.blazeFaceDetector import blazeFaceDetector

scoreThreshold = 0.7
iouThreshold = 0.3

# Initialize face detector
faceDetector = blazeFaceDetector("front", scoreThreshold, iouThreshold)

# Initialize webcam
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:

	# Read frame from the webcam
	ret, img = camera.read()	

	# Detect faces
	detectionResults = faceDetector.detectFaces(img)

	# Draw detections
	img_plot = faceDetector.drawDetections(img, detectionResults)
	cv2.imshow("detections", img_plot)

	# Press key q to stop
	if cv2.waitKey(1) == ord('q'):
		break

camera.release()
cv2.destroyAllWindows()
