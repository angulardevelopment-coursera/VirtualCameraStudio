from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt


class VideoCanvas(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 600)

    def paintEvent(self, event):

        painter = QPainter(self)

        # Background
        painter.fillRect(self.rect(), QColor(35, 35, 35))

        # Temporary text
        painter.setPen(Qt.white)
        painter.drawText(
            self.rect(),
            Qt.AlignCenter,
            "No Video Loaded"
        )