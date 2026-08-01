"""
VideoCanvas

Responsible only for drawing the current video frame
and any overlays (crop rectangle, guides, handles,
safe areas, etc.)

Does NOT decode video.
"""
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QImage
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen

import cv2


class VideoCanvas(QWidget):

    def __init__(self):
        super().__init__()

        self.player = None
        
    def setPlayer(self, player):

        self.player = player

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

        image = self.player.currentImage()

        scaled = image.scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        offset_x = (self.width() - scaled.width()) // 2
        offset_y = (self.height() - scaled.height()) // 2

        painter.drawImage(offset_x, offset_y, scaled)
        
        
        
        pen = QPen(Qt.red)
        pen.setWidth(3)

        painter.setPen(pen)
        
        camera_width = scaled.width() * 0.8
        camera_height = camera_width * 9 / 16
        
        camera_x = offset_x + (scaled.width() - camera_width) / 2
        camera_y = offset_y + (scaled.height() - camera_height) / 2
        
        painter.drawRect(
            int(camera_x),
            int(camera_y),
            int(camera_width),
            int(camera_height)
        )
        
        