from PyQt6.QtWidgets import *
import requests
from PyQt6.QtGui import QPixmap

headers =  {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM2EyODlkYjliYWY1MTUzMjc1ZmFiMzhhZGZkYWZiZSIsIm5iZiI6MTc1MzI2OTQ1Ny4wNTIsInN1YiI6IjY4ODBjNGQxY2Y3MTI2Y2Q1YWY3NzRkMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YCTpdnDlC47BgczYGYc4CoB3vyD2Ky5FiQlslJCA8ag"
}
app = QApplication([])
window = QWidget()
window.resize(700,600)
reqest1 = QPushButton("Пошук")
reqest1_2 = QLineEdit()
reqest1_3 = QPushButton("Popular Films:")

reqest1_4 = QTextEdit()

reuest2 = QLabel("a")
reuest3 = QLabel("x")
reuest4 = QLabel("c")


# def popular_actours():
#     response3 = requests.get("https://api.themoviedb.org/3/person/popular", headers=headers)
#     result3 = response3.json()
#     print(result3['results'][0]['profile_path'])
#     f1 = result3['results'][0]['profile_path']
#     f2 = result3['results'][1]['profile_path']
#     f3 = result3['results'][2]['profile_path']
#     print(result3)
#     print(f1, f2, f3)
#
#     poster_url2 = f"https://image.tmdb.org/t/p/w500{f1}"
#     poster_url3 = f"https://image.tmdb.org/t/p/w500{f2}"
#     poster_url4 = f"https://image.tmdb.org/t/p/w500{f3}"
#
#     response_img2 = requests.get(poster_url2)
#     pixmap2 = QPixmap()
#     pixmap2.loadFromData(response_img2.content)
#     reuest2.setPixmap(pixmap2)
#
#     response_img3 = requests.get(poster_url3)
#     pixmap3 = QPixmap()
#     pixmap3.loadFromData(response_img3.content)
#     reuest3.setPixmap(pixmap3)
#
#     response_img4 = requests.get(poster_url4)
#     pixmap4 = QPixmap()
#     pixmap4.loadFromData(response_img4.content)
#     reuest4.setPixmap(pixmap4)

def search():
   
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?query={reqest1_2.text()}", headers=headers)
    result = response.json()
    print(result)





    result = result["results"]
    film_id = result[0]["id"]
    response2 = requests.get(f"https://api.themoviedb.org/3/movie/{film_id}/images", headers = headers)
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

def popular_actours_window():

    window2 = QWidget()
    window2.resize(700,600)
    window2.setWindowTitle("Популярны актори")
    v = QHBoxLayout
    a = QLabel("a")
    b = QLabel("b")
    c = QLabel ("c")
    v.addWidget(a)
    v.addWidget(b)
    v.addWidget(c)
    v.setL


    window2.show()
    return window2
reqest1_3.clicked.connect(popular_actours_window)
h1 = QVBoxLayout()
h1.addWidget(reqest1)
h1.addWidget(reqest1_2)
h1.addWidget(reuest2)
h1.addWidget(reqest1_3)

h1.addWidget(reuest3)
h1.addWidget(reuest4)
reqest1.clicked.connect(search)





window.setLayout(h1)
window.show()
app.exec()
