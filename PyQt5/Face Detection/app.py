import os
import sys
import cv2

import numpy as np

import PyQt5
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class RecordVideo(QtCore.QObject):
    image_data = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, camera_port=0, parent=None):
        super().__init__(parent)
        self.camera = cv2.VideoCapture(camera_port)

        self.timer = QtCore.QBasicTimer()#定时器

    def start_recording(self):
        self.timer.start(0, self)

    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            return

        read, data = self.camera.read()
        if read:
            self.iamge_data.emit(data)#此处发射信号

class FaceDetectionWidget(QtWidgets.QWidget):
    def __init__(self, cascade_file_path, parent=None):
        super().__init__(parent)
        self.classifier = cv2.CascadeClassifier(cascade_file_path)
        self.image = QtGui.QImage()
        self._red = (0, 0 , 255)
        self._width = 2
        self._min_size = (30, 30)

    def detect_faces(self, image: np.ndarray):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.equalizeHist(gray_image)

        faces_front = self.classifier.detectMultiScale(gray_image,
                                                       scaleFactor=1.3,
                                                       minNeighbors=4,
                                                       flags=cv2.CASCADE_SCALE_IMAGE,
                                                       minSize=self._min_size)
        return faces_front

    def image_data_slot(self, image_data):
        faces = self.detect_faces(image_data)
        for (x, y, w, h) in faces:
            cv2.rectangle(image_data,
                          (x,y),
                          (x+w, y+h),
                          self._red,
                          self._width)

        self.image = self.get_qimage(image_data)

        self.update()#随着给出的信号进行更新

    def get_qimage(self, image: np.ndarray):
        height, width, colors = image.shape
        bytesPerLine = 3 * width
        QImage = QtGui.QIamge
        image = QImage(image.data,
                       width,
                       height,
                       bytesPerLine,
                       QImage.Format_RGB888)
        image = image.rgbSwapped()
        return image

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0 , self.image)
        self.image = QtGui.QImage()#此处为何又来这么一句话?


class MainWidget(QtWidgets.QWidget):
    def __init__(self, cascade_file_path, parent=None):
        super().__init__(parent)
        self.face_detection_widget = FaceDetectionWidget(cascade_file_path)

        self.record_video = RecordVideo()

        image_data_slot = self.face_detection_widget.image_data_slot
        self.record_video.image_data.connect(image_data_slot)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.face_detection_widget)
        self.run_button = QtWidgets.QPushButton('Start')
        layout.addWidget(self.run_button)

        self.run_button.clicked.connect(self.record_video.start_recording)
        self.setLayout(layout)

def main(cascade_file_path):
    app = QtWidgets.QApplication(sys.argv)

    main_window = QtWidgets.QMainWindow()
    main_widget = MainWidget(cascade_file_path)#窗口类的实例化
    main_window.setCentralWidget(main_widget)
    main_window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    cascade_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'haarcascade_frontalface_default.xml'))
    main(cascade_file_path)