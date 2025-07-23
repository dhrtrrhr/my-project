from PyQt6.QtWidgets import *
import requests


app = QApplication([])
window = QWidget()

reuest1 = QLabel("Пошук")
reuest1_2 = QLineEdit()


reuest2 = QLabel("a")
reuest3 = QLabel("x")
reuest4 = QLabel("c")

h1 = QVBoxLayout()
h1.addWidget(reuest1)
h1.addWidget(reuest1_2)
h1.addWidget(reuest2)
h1.addWidget(reuest3)
h1.addWidget(reuest4)








window.setLayout(h1)
window.show()
app.exec()