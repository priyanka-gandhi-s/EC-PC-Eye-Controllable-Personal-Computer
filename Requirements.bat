@echo off
echo Installing required Python packages...

py -3.10 -m pip install --upgrade pip

py -3.10 -m pip install PyQt5
py -3.10 -m pip install matplotlib
py -3.10 -m pip install pyqt_switch
py -3.10 -m pip install opencv-python
py -3.10 -m pip install pyautogui
py -3.10 -m pip install mediapipe
py -3.10 -m pip install pyttsx3
py -3.10 -m pip install SpeechRecognition
py -3.10 -m pip install wikipedia

echo All packages installed.

echo Running app.py...
py -3.10 app.py

pause
