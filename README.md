🗑 Waste Classification with Bin Overlay
This project is a real-time waste classification system using OpenCV, TensorFlow/Keras, and cvzone. The system captures input from a webcam, classifies the waste type, and overlays the corresponding bin image on a custom background to indicate where to dispose of the detected waste.

📌 Features
✅ Real-time classification using webcam input
✅ Supports multiple waste categories (paper, plastic, food, glass, metal)
✅ Dynamic bin overlay on a background image
✅ Easily extendable with more categories or updated models

🖥 Tech Stack
Python 3.x

OpenCV

cvzone

TensorFlow / Keras

NumPy

Pre-trained model: keras_model.h5 + labels.txt

🚀 How to Run
1️⃣ Clone or download this repository.

2️⃣ Ensure the following directory structure:

bash
Copy
Edit
project_root/
│
├── resource/
│   ├── Model/
│   │   ├── keras_model.h5
│   │   └── labels.txt
│   ├── Bins/
│   │   ├── bin0.png  # Plastic
│   │   ├── bin1.png  # Paper
│   │   ├── bin2.png  # Food
│   │   ├── bin3.png  # Metal
│   │   └── bin4.png  # Glass
│   └── background.png
3️⃣ Install dependencies:

bash
Copy
Edit
pip install opencv-python cvzone tensorflow numpy
4️⃣ Run the script:

bash
Copy
Edit
python waste_classification.py
⚙️ How It Works
The webcam feed is resized and displayed on a background template.

The Keras model classifies the current frame into one of the predefined waste types.

A corresponding bin image is overlayed on the background.

The user can see both raw webcam and processed output.

Press Esc key to exit.

📝 Class & Bin Mapping
Class ID	Waste Type	Bin Index
0	Paper	1
1	Plastic	0
2	Food Waste	2
3	Glass	4
4	Metal	3
5	None / Unknown	-

📌 Example Output
👉 The app shows the webcam feed on one side and overlays a bin (e.g., paper bin) on the background when paper waste is detected.

🤝 Credits
Built by Nithyashree N C as part of a waste segregation project.
