from PyQt6.QtWidgets import *
import requests



app = QApplication([])
window = QWidget()

reuest1 = QLabel("Пошук")
reuest1_2 = QLineEdit()
searched_films= QTextEdit()

popular_lbl = QLabel("Popular films:")

reuest2 = QLabel("a")
reuest3 = QLabel("x")
reuest4 = QLabel("c")

h1 = QVBoxLayout()
h1.addWidget(reuest1)
h1.addWidget(reuest1_2)
h1.addWidget(popular_lbl)
h1.addWidget(reuest2)
h1.addWidget(reuest3)
h1.addWidget(reuest4)

def search():

    response = requests.get("https://api.themoviedb.org/3/discover/movie")
    result = response.json()
    response2 = requests.get("https://api.themoviedb.org/3/tv/{series_id}/keywords")
    result2 = response2.json()
    name = response2[popular_lbl.text()]
    searched_films.append(name)
    








window.setLayout(h1)
window.show()
app.exec()