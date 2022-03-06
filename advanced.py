import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication, QPushButton
from PyQt5.Qt import QInputDialog, QPushButton, QGridLayout, QMessageBox


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.v1 = QLineEdit()
        self.v11 = QLineEdit()
        self.v2 = QLineEdit()
        self.v22 = QLineEdit()
        self.t11 = QLabel('-')
        self.t22 = QLabel('-')
        self.T11 = QLabel('-')
        self.T22 = QLabel('-')
        self.error = QLabel('')

        calc_button = QPushButton('Рассчёт', self)

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel('Первая высота подъема и опускания стола'), 0, 0)
        layout.addWidget(self.l1, 0, 1)

        layout.addWidget(QLabel('Вторая высота подъема и опускания стола'), 1, 0)
        layout.addWidget(self.l2, 1, 1)

        layout.addWidget(QLabel('Первая скорость подъема стола'), 2, 0)
        layout.addWidget(self.v1, 2, 1)

        layout.addWidget(QLabel('Вторая скорость подъема стола'), 3, 0)
        layout.addWidget(self.v11, 3, 1)

        layout.addWidget(QLabel('Первая скорость опускания (ретракта) стола'), 4, 0)
        layout.addWidget(self.v2, 4, 1)

        layout.addWidget(QLabel('Вторая скорость опускания (ретракта) стола'), 5, 0)
        layout.addWidget(self.v22, 5, 1)

        layout.addWidget(QLabel('Время подъема стола (TSMC)'), 6, 0)
        layout.addWidget(self.t11, 6, 1)

        layout.addWidget(QLabel('Время опускания (ретракта) стола (TSMC)'), 7, 0)
        layout.addWidget(self.t22, 7, 1)

        layout.addWidget(QLabel('Минимальная задержка выключения (TSMC)'), 8, 0)
        layout.addWidget(self.T11, 8, 1)

        layout.addWidget(QLabel('Максимальная задержка выключения (TSMC)'), 9, 0)
        layout.addWidget(self.T22, 9, 1)

        layout.addWidget(calc_button, 10, 0)
        layout.addWidget(self.error, 10, 1)
        calc_button.clicked.connect(self.calc_action)

    def calc_action(self):
        try:
            l1 = float(self.l1.text())
            l2 = float(self.l2.text())
            v1 = float(self.v1.text())
            v11 = float(self.v11.text())
            v2 = float(self.v2.text())
            v22 = float(self.v22.text())
            t11 = l1/(v1/60)+l2/(v11/60)
            t22 = l1/(v2/60)+l2/(v22/60)
            T11 = t11 + t22 + 2
            T22 = t11 + t22 + 3
            self.t11.setText(str(round(t11, 2)))
            self.t22.setText(str(round(t22, 2)))
            self.T11.setText(str(round(T11, 2)))
            self.T22.setText(str(round(T22, 2)))
            self.error.setText("")
        except:
            self.t11.setText('-')
            self.t22.setText('-')
            self.T11.setText('-')
            self.T22.setText('-')
            self.error.setText("Wrong Input")

if __name__ == '__main__':
    app = QApplication([])

    window = Window()
    window.setWindowTitle('Продвинутый калькулятор печати')
    window.show()


    app.exec()