from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog
)

from videocanvas import VideoCanvas

from videoplayer import VideoPlayer

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Virtual Camera Studio")

        self.resize(1400, 900)

        self.canvas = VideoCanvas()

        self.player = VideoPlayer()

        self.canvas.setPlayer(self.player)

        self.setCentralWidget(self.canvas)

        fileMenu = self.menuBar().addMenu("&File")

        openAction = fileMenu.addAction("Open Video")

        openAction.triggered.connect(self.openVideo)

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

                self.statusBar().showMessage(
                    f"{self.player.width} × {self.player.height}    "
                    f"{self.player.fps:.2f} fps    "
                    f"{self.player.duration():.2f} sec"
                )