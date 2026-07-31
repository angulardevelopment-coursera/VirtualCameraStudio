from PySide6.QtWidgets import QMainWindow

from videocanvas import VideoCanvas

import cv2

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Virtual Camera Studio")

        self.resize(1400,900)

        self.canvas = VideoCanvas()

        self.setCentralWidget(self.canvas)
        
    def loadVideo(self, filename):

        self.cap = cv2.VideoCapture(filename)

        ok, frame = self.cap.read()

        if ok:

            self.frame = frame

            self.update()