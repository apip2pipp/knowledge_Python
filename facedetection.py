import cv2

# Load the face detector XML file
face_cascade = cv2.CascadeClassifier(r'D:\nguliAH_POLINEMA\miniProject_python\mentahan\cindy.jpg')

# Check if the file was loaded properly
if face_cascade.empty():
    print("Error: Could not load face detector XML!")
    exit()

# Load the image and convert it to grayscale
img = cv2.imread(r'D:\nguliAH_POLINEMA\miniProject_python\mentahan\cindy.jpg')
if img is None:
    print("Error: Image file not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangles around the faces
for (x, y, w, h) in faces: 
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Save the image with detected faces
cv2.imwrite("face_detected.png", img) 
print('Successfully saved')
