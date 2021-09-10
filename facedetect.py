import cv2
import pkg_resources
#haar_xml = pkg_resources.resource_filename('cv2', 'data/haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier(haar_xml)
image = cv2.imread("Seema.jpg")
image = cv2.resize(image, (800,533))
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


retval = cv2.CascadeClassifier.empty(face_cascade)
print(retval)
faces=face_cascade.detectMultiScale(gray_image,scaleFactor=1.10,minNeighbors=5)


if retval == False:
    for x, y, w, h in faces:
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.imshow("Face Detector", image)
        k = cv2.waitKey(2000)
    cv2.destroyAllWindows()

    cv2.imwrite("kids_face_detected.jpeg", image)