from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog
)

from PySide6.QtGui import QGuiApplication

from videocanvas import VideoCanvas

from videoplayer import VideoPlayer

import os

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Virtual Camera Studio")
        
        self.canvas = VideoCanvas()

        self.player = VideoPlayer()

        self.canvas.setPlayer(self.player)

        self.setCentralWidget(self.canvas)

        status = self.statusBar()
        
        status.showMessage("Ready")

        fileMenu = self.menuBar().addMenu("&File")

        openAction = fileMenu.addAction("Open Video")

        openAction.triggered.connect(self.openVideo)

        self.showMaximized()
        
    def openVideo(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open Video",
            "",
            "Videos (*.mov *.mp4 *.avi)"
        )

        if filename:

            if self.player.open(filename):

                self.canvas.update()

                video_name = os.path.basename(filename)

                self.statusBar().showMessage(
                    f"{video_name}    "
                    f"{self.player.width} × {self.player.height}    "
                    f"{self.player.fps:.2f} fps    "
                    f"{self.player.duration():.2f} sec"
                )