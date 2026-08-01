"""
VideoPlayer

Responsible for opening videos, decoding frames,
and providing the current frame as a QImage.

Does NOT draw anything.
"""
import cv2
from PySide6.QtGui import QImage


class VideoPlayer:
    
    @property
    def currentTime(self):

        return self.current_frame / self.fps
        
    def __init__(self):

        self.cap = None

        self.filename = ""

        self.frame_count = 0
        self.fps = 0
        self.width = 0
        self.height = 0

        self.current_frame = 0

        self.image = None


    def open(self, filename):

        self.cap = cv2.VideoCapture(filename)

        if not self.cap.isOpened():
            return False

        self.filename = filename

        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        return self.gotoFrame(0)


    def gotoFrame(self, frame_number):

        if self.cap is None:
            return False

        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        ok, frame = self.cap.read()

        if not ok:
            return False

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = frame.shape

        self.image = QImage(
            frame.data,
            w,
            h,
            ch * w,
            QImage.Format_RGB888
        ).copy()

        self.current_frame = frame_number

        return True


    def currentImage(self):

        return self.image


    def duration(self):

        if self.fps == 0:
            return 0

        return self.frame_count / self.fps