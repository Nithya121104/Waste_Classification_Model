import os
import cvzone
from cvzone.ClassificationModule import Classifier
import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Load classifier
classifier = Classifier(
    r'C:\Users\nithy\PycharmProjects\wasteclassification\resource\Model\keras_model.h5',
    r'C:\Users\nithy\PycharmProjects\wasteclassification\resource\Model\labels.txt'
)

# Load bin images
imgBinsList = []
pathfolderBins = r"C:\Users\nithy\PycharmProjects\wasteclassification\resource\Bins"
pathList = os.listdir(pathfolderBins)
pathList.sort()  # Sort to load in expected order

for path in pathList:
    imgBinsList.append(cv2.imread(os.path.join(pathfolderBins, path), cv2.IMREAD_UNCHANGED))

# Class ID → bin index mapping
classDic = {
    0: 1,  # Paper
    1: 0,  # Plastic
    2: 2,  # Food waste
    3: 4,  # Glass
    4: 3,  # Metal
    5: None  # Nothing
}

# Load background image once
imgBackgroundBase = cv2.imread(r'C:\Users\nithy\PycharmProjects\wasteclassification\resource\background.png')

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image from webcam.")
        break

    imgResize = cv2.resize(img, (454, 340))
    imgBackground = imgBackgroundBase.copy()

    prediction = classifier.getPrediction(img)
    classID = prediction[1]
    print(f"Detected class: {classID}")

    if classDic[classID] is not None:
        classIDbin = classDic[classID]
        imgBackground = cvzone.overlayPNG(imgBackground, imgBinsList[classIDbin], (750, 160))

    imgBackground[148:148+340, 159:159+454] = imgResize

    cv2.imshow("Webcam", img)
    cv2.imshow("Output", imgBackground)

    # Break loop on Esc key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()


