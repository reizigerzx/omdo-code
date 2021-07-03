# OpenCV


## Video or Camera
1. Load camera or video
	```python
	cap = cv.VideoCapture(0)
	```

2. For security reason, check if video is loaded or camera is opened
	```python
	if not cap.isOpened():
		exit()
	```
	or
	```python
	if cap.isOpened():
		#capture here
	```
	
3. fff
	```python
	success, image = cap.read()
	```