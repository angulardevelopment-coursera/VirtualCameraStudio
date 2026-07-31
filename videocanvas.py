from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QImage
from PySide6.QtCore import Qt

import cv2


class VideoCanvas(QWidget):

    def __init__(self):
        super().__init__()

        self.player = None
        
    def setPlayer(self, player):

        self.player = player

        self.update()
        
    def loadVideo(self, filename):

        cap = cv2.VideoCapture(filename)

        ok, frame = cap.read()

        cap.release()

        if not ok:
            print("Couldn't load video.")
            return

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = frame.shape

        bytesPerLine = ch * w

        self.image = QImage(
            frame.data,
            w,
            h,
            bytesPerLine,
            QImage.Format_RGB888
        ).copy()

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.fillRect(self.rect(), QColor(40,40,40))

        if self.player is None or self.player.currentImage() is None:

            painter.setPen(Qt.white)

            painter.drawText(
                self.rect(),
                Qt.AlignCenter,
                "No Video Loaded"
            )

            return

        scaled = self.player.currentImage().scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        x = (self.width()-scaled.width())//2
        y = (self.height()-scaled.height())//2

        painter.drawImage(x, y, scaled)