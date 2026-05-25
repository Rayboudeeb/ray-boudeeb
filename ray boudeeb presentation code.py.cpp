import cv2
import numpy as np

# Open the road video
cap = cv2.VideoCapture("road.mp4")

while cap.isOpened() :

    # Read each frame
    ret, frame = cap.read()

    # Stop if video ends
    if not ret:
break

# Convert frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges
edges = cv2.Canny(blur, 50, 150)

# Detect lane lines
lines = cv2.HoughLinesP(
    edges,
    1,
    np.pi / 180,
    50,
    minLineLength = 100,
    maxLineGap = 50
)

# Draw detected lane lines
if lines is not None:
for line in lines :

x1, y1, x2, y2 = line[0]

cv2.line(
    frame,
    (x1, y1),
    (x2, y2),
    (0, 255, 0),
    3
)

# Display lane detection output
cv2.imshow("Lane Detection", frame)

# Press Q to quit
if cv2.waitKey(1) & 0xFF == ord('q') :
    break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()