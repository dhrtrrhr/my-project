from PyQt6.QtWidgets import *
import requests
from PyQt6.QtGui import QPixmap

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM2EyODlkYjliYWY1MTUzMjc1ZmFiMzhhZGZkYWZiZSIsIm5iZiI6MTc1MzI2OTQ1Ny4wNTIsInN1YiI6IjY4ODBjNGQxY2Y3MTI2Y2Q1YWY3NzRkMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YCTpdnDlC47BgczYGYc4CoB3vyD2Ky5FiQlslJCA8ag"
}
app = QApplication([])
window = QWidget()
window.resize(700, 600)
reqest1 = QPushButton("Пошук")
reqest1_2 = QLineEdit()
reqest1_3 = QPushButton("Popular Authors:")

reqest1_4 = QTextEdit()

reuest2 = QLabel("a")
reuest3 = QLabel("x")
reuest4 = QLabel("c")
request5 = QLabel("v")
app.setStyleSheet("""



    QPushButton
    {
        font-size: 25px;
        font-family: Impact;
        border-style: groove;
        border-width: 3px;
        border-color: black;
    }
    QPushButton
    {
        color: green;
    }
    QPushButton:hover{
        background-color: A9A9A9;
    }
    
    

""")


def popular_actours():
    response3 = requests.get("https://api.themoviedb.org/3/person/popular", headers=headers)
    result3 = response3.json()
    f1 = result3['results'][0]['name']
    f2 = result3['results'][1]['name']
    f3 = result3['results'][2]['name']
    reuest3.setText(f1)
    reuest4.setText(f2)
    request5.setText(f3)



    print(f1)

def search():
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?query={reqest1_2.text()}", headers=headers)
    result = response.json()
    print(result)

    result = result["results"]
    film_id = result[0]["id"]
    response2 = requests.get(f"https://api.themoviedb.org/3/movie/{film_id}/images", headers=headers)
    result2 = response2.json()
    poster_path = result2["posters"][0]["file_path"]

    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"

    print(film_id)
    print(response2.json())
    print(poster_url)

    response_img = requests.get(poster_url)
    pixmap = QPixmap()
    pixmap.loadFromData(response_img.content)
    reuest2.setPixmap(pixmap)
    reuest2.setPixmap(pixmap.scaled(200, 200))



reqest1_3.clicked.connect(popular_actours)
h1 = QVBoxLayout()
h1.addWidget(reqest1)
h1.addWidget(reqest1_2)
h1.addWidget(reuest2)
h1.addWidget(reqest1_3)

h1.addWidget(reuest3)
h1.addWidget(reuest4)
h1.addWidget(request5)
reqest1.clicked.connect(search)

window.setLayout(h1)
window.show()
app.exec()