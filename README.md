#🖥️ Eye Controllable Personal Computer
Control your computer using only your eyes – designed especially for people with ALS and severe physical disabilities.

#📌 Inspiration
###Many individuals with ALS, cerebral palsy, or other severe physical disabilities can only move their eyes and limited facial muscles.
###Traditional computers require hand-based input, creating barriers to education, employment, and communication.
###Our solution gives them full control of a computer — using nothing but their gaze.

#🚀 Features

###Real-time eye tracking for cursor movement.
###Blink-based clicking (left eye blink for click, both eyes closed for selection).
###Eye-controlled keyboard for typing without hands.
###Open/close files and applications hands-free.
###Works with a standard webcam — no expensive hardware required.

#🛠️ Built With

###Python – Core programming language
###OpenCV – Computer vision and image processing
###MediaPipe – Ultra-fast facial and eye landmark detection
###PyAutoGUI – Mouse and keyboard simulation
###PyQt5 – GUI interface development
###CNN (Convolutional Neural Network) – Eye movement classification
###NumPy & Pandas – Data processing
###Matplotlib – Visualization for testing/debugging

#📂 How It Works

###Face & Eye Detection – Uses MediaPipe/OpenCV to detect facial landmarks.
###Gaze Estimation – Calculates gaze ratio from left & right eyes to detect screen position.
###Blink Detection – Recognizes blinks using eye aspect ratio for clicks/selections.
###Cursor Control – Maps gaze position to cursor movement on the screen.
###Eye Keyboard – Highlights keys in sequence, selects on blink.

#📦 Installation

###1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/priyanka-gandhi-s/EC-PC.git
cd EC-PC
2️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the application
bash
Copy
Edit
python main.py

#⚙️ Requirements

###Python 3.9+
###Webcam
###Works on Windows, macOS, and Linux

#🎯 Use Cases

###Assistive Technology for ALS, cerebral palsy, spinal cord injury patients.
###Hands-free computing in sterile or industrial environments.
###Research in eye-tracking and HCI.

#🏆 Accomplishments

###Created a low-cost eye control system using only a webcam.
###Integrated real-time tracking with smooth cursor movement.
###Developed an eye-controlled keyboard for full text input.

#🔮 Future Improvements

###More accurate gaze detection using deep learning-based models.
###Multi-language voice synthesis integration.
###Cloud-based user profiles for portability.

#📜 License
###This project is licensed under the MIT License – see the LICENSE file for details.


