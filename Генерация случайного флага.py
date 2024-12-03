import copy
import random
import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog


class RandomFlag(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.draw = None
        self.base = [80, 80, 120, 30]

    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Генерация флага')

        self.button = QPushButton(self)
        self.button.move(20, 40)
        self.button.setText("Ввести количество цветов флага")
        self.button.clicked.connect(self.run)

    def run(self):

        # Ввод количества цветов с помощью диалогового окна
        i, okBtnPressed = QInputDialog.getInt(
            self,
            "Введите число цветов флага",
            "Сколько цветов?", 3, 1, 10, 1)
        if okBtnPressed:
            self.draw = i

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.drawFlag(qp)
            qp.end()

    def drawFlag(self, qp):
        base = copy.copy(self.base)
        for i in range(self.draw):
            # Генерация случайного цвета по RGB-схеме
            rand_color = QColor(*[random.randrange(255) for _ in range(3)])
            qp.setBrush(rand_color)
            # Рисуем полоску
            qp.drawRect(*base)
            # Смещаемся вниз
            base[1] += 30
        self.draw = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomFlag()
    ex.show()
    sys.exit(app.exec())
