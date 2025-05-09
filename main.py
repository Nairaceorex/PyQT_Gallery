import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QSpinBox,
    QHBoxLayout,
    QSlider,
    QStackedLayout,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class ImageGallery(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Gallery")
        self.setGeometry(100, 100, 600, 400)

        # Список изображений и описаний
        self.images = [
            ("img/image1.jpg", "Описание 1"),
            ("img/image2.jpg", "Описание 2"),
            ("img/image3.jpg", "Описание 3"),
            ("img/image4.jpg", "Описание 4"),
            ("img/image5.jpg", "Описание 5"),
            ("img/image6.jpg", "Описание 6"),
            ("img/image7.jpg", "Описание 7"),
            ("img/image8.jpg", "Описание 8"),
            ("img/image9.jpg", "Описание 9"),
            ("img/image10.jpg", "Описание 10"),
        ]

        self.layout = QVBoxLayout(self)

        # QStackedLayout для картинок и описаний
        self.stacked_layout = QStackedLayout()

        for image_path, description in self.images:
            image_widget = self.create_image_widget(image_path, description)
            self.stacked_layout.addWidget(image_widget)

        # Слайдер и спинбокс для переключения изображений
        self.control_layout = QHBoxLayout()

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(len(self.images) - 1)
        self.slider.valueChanged.connect(self.change_image)

        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(0)
        self.spin_box.setMaximum(len(self.images) - 1)
        self.spin_box.valueChanged.connect(self.change_image)

        self.slider.valueChanged.connect(self.spin_box.setValue)
        self.spin_box.valueChanged.connect(self.slider.setValue)

        self.control_layout.addWidget(self.slider)
        self.control_layout.addWidget(self.spin_box)

        self.layout.addLayout(self.stacked_layout)
        self.layout.addLayout(self.control_layout)

    def create_image_widget(self, image_path, description):
        widget = QWidget()
        layout = QVBoxLayout()

        pixmap = QPixmap(image_path)
        image_label = QLabel()
        image_label.setPixmap(pixmap.scaled(500, 300, Qt.KeepAspectRatio))

        description_label = QLabel(description)
        description_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(image_label)
        layout.addWidget(description_label)
        widget.setLayout(layout)

        return widget

    def change_image(self, index):
        self.stacked_layout.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    gallery = ImageGallery()
    gallery.show()

    sys.exit(app.exec_())
