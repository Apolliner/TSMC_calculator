import sys
from PyQt5.Qt import QPushButton, QGridLayout
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget, QLabel, QLineEdit, QApplication
from PyQt5.Qt import QApplication
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QLineEdit

import sys

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Калькулятор 3D печати'
        self.left = 600
        self.top = 400
        self.width = 700
        self.height = 500
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = StandardCalculator()
        self.tab2 = AdvancedCalculator()

        self.tabs.addTab(self.tab1, "Стандартный")
        self.tabs.addTab(self.tab2, "Продвинутый")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class StandardCalculator(QWidget):

    def __init__(self):
        super().__init__()

        reg_ex = QRegExp("[0-9.]{200}")

        self.L = QLineEdit()
        self.L.setValidator(QRegExpValidator(reg_ex, self.L))
        self.v1 = QLineEdit()
        self.v1.setValidator(QRegExpValidator(reg_ex, self.v1))
        self.v2 = QLineEdit()
        self.v2.setValidator(QRegExpValidator(reg_ex, self.v2))
        self.t1 = QLabel('-')
        self.t2 = QLabel('-')
        self.T1 = QLabel('-')
        self.T2 = QLabel('-')


        calc_button = QPushButton('Рассчёт', self)
        clear_button = QPushButton('Очистить', self)

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel('Высота подъема и опускания стола'), 0, 0)
        layout.addWidget(self.L, 0, 1)

        layout.addWidget(QLabel('Скорость подъема стола'), 1, 0)
        layout.addWidget(self.v1, 1, 1)

        layout.addWidget(QLabel('Скорость опускания (ретракта) стола'), 2, 0)
        layout.addWidget(self.v2, 2, 1)

        layout.addWidget(QLabel('Скорость подъема стола'), 3, 0)
        layout.addWidget(self.t1, 3, 1)

        layout.addWidget(QLabel('Скорость опускания (ретракта) стола'), 4, 0)
        layout.addWidget(self.t2, 4, 1)

        layout.addWidget(QLabel('Минимальная задержка выключения'), 5, 0)
        layout.addWidget(self.T1, 5, 1)

        layout.addWidget(QLabel('Максимальная задержка выключения'), 6, 0)
        layout.addWidget(self.T2, 6, 1)

        layout.addWidget(calc_button, 7, 1)
        layout.addWidget(clear_button, 7, 0)
        calc_button.clicked.connect(self.calc_action)
        clear_button.clicked.connect(self.clear_action)
        start = 8
        for i in range(3):
            n = start + i
            layout.addWidget(QLabel(''), n, 0)


    def calc_action(self):
        try:
            L = float(self.L.text())
            v1 = float(self.v1.text())
            v2 = float(self.v2.text())
            t1 = L/(v1/60)
            t2 = L/(v2/60)
            T1 = t1 + t2 + 2
            T2 = t1 + t2 + 3
            self.t1.setStyleSheet('color: black')
            self.t2.setStyleSheet('color: black')
            self.T1.setStyleSheet('color: black')
            self.T2.setStyleSheet('color: black')

            self.t1.setText(str(round(t1, 2)))
            self.t2.setText(str(round(t2, 2)))
            self.T1.setText(str(round(T1, 2)))
            self.T2.setText(str(round(T2, 2)))
        except:
            self.t1.setStyleSheet('color: red')
            self.t2.setStyleSheet('color: red')
            self.T1.setStyleSheet('color: red')
            self.T2.setStyleSheet('color: red')

            self.t1.setText('Некорректный ввод')
            self.t2.setText('Некорректный ввод')
            self.T1.setText('Некорректный ввод')
            self.T2.setText('Некорректный ввод')


    def clear_action(self):
        self.L.clear()
        self.v1.clear()
        self.v2.clear()
        self.t1.setStyleSheet('color: black')
        self.t2.setStyleSheet('color: black')
        self.T1.setStyleSheet('color: black')
        self.T2.setStyleSheet('color: black')
        self.t1.setText('-')
        self.t2.setText('-')
        self.T1.setText('-')
        self.T2.setText('-')


class AdvancedCalculator(QWidget):

    def __init__(self):
        super().__init__()

        reg_ex = QRegExp("[0-9.]{200}")

        self.l1 = QLineEdit()
        self.l1.setValidator(QRegExpValidator(reg_ex, self.l1))
        self.l2 = QLineEdit()
        self.l2.setValidator(QRegExpValidator(reg_ex, self.l2))
        self.v1 = QLineEdit()
        self.v1.setValidator(QRegExpValidator(reg_ex, self.v1))
        self.v11 = QLineEdit()
        self.v11.setValidator(QRegExpValidator(reg_ex, self.v11))
        self.v2 = QLineEdit()
        self.v2.setValidator(QRegExpValidator(reg_ex, self.v2))
        self.v22 = QLineEdit()
        self.v22.setValidator(QRegExpValidator(reg_ex, self.v22))
        self.t11 = QLabel('-')
        self.t22 = QLabel('-')
        self.T11 = QLabel('-')
        self.T22 = QLabel('-')

        calc_button = QPushButton('Рассчёт', self)
        clear_button = QPushButton('Очистить', self)

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

        layout.addWidget(calc_button, 10, 1)
        layout.addWidget(clear_button, 10, 0)
        calc_button.clicked.connect(self.calc_action)
        clear_button.clicked.connect(self.clear_action)

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
            self.t11.setStyleSheet('color: black')
            self.t22.setStyleSheet('color: black')
            self.T11.setStyleSheet('color: black')
            self.T22.setStyleSheet('color: black')
            self.t11.setText(str(round(t11, 2)))
            self.t22.setText(str(round(t22, 2)))
            self.T11.setText(str(round(T11, 2)))
            self.T22.setText(str(round(T22, 2)))
        except Exception as e:
            self.t11.setStyleSheet('color: red')
            self.t22.setStyleSheet('color: red')
            self.T11.setStyleSheet('color: red')
            self.T22.setStyleSheet('color: red')
            self.t11.setText('Некорректный ввод')
            self.t22.setText('Некорректный ввод')
            self.T11.setText('Некорректный ввод')
            self.T22.setText('Некорректный ввод')

    def clear_action(self):
        self.l1.clear()
        self.l2.clear()
        self.v1.clear()
        self.v11.clear()
        self.v2.clear()
        self.v22.clear()
        self.t11.setStyleSheet('color: black')
        self.t22.setStyleSheet('color: black')
        self.T11.setStyleSheet('color: black')
        self.T22.setStyleSheet('color: black')
        self.t11.setText('-')
        self.t22.setText('-')
        self.T11.setText('-')
        self.T22.setText('-')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())