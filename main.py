from PyQt6.QtWidgets import *
import requests

headers =  {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM2EyODlkYjliYWY1MTUzMjc1ZmFiMzhhZGZkYWZiZSIsIm5iZiI6MTc1MzI2OTQ1Ny4wNTIsInN1YiI6IjY4ODBjNGQxY2Y3MTI2Y2Q1YWY3NzRkMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.YCTpdnDlC47BgczYGYc4CoB3vyD2Ky5FiQlslJCA8ag"
}
app = QApplication([])
window = QWidget()
window.resize(700,600)
reqest1 = QPushButton("Пошук")
reqest1_2 = QLineEdit()
reqest1_3 = QLabel("Popular Films:")

reqest1_4 = QTextEdit()

reuest2 = QLabel("a")
reuest3 = QLabel("x")
reuest4 = QLabel("c")




def search():
   
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?query={reqest1_2.text()}", headers=headers)
    result = response.json()
    print(result)

    response3 = requests.get("https://api.themoviedb.org/3/movie/popular", headers = headers)
    result3 = response3.json()
    print(result3)



    result = result["results"]
    film_id = result[0]["id"]
    response2 = requests.get(f"https://api.themoviedb.org/3/movie/{film_id}/images", headers = headers)
    result2 = response2.json()
    poster = result2["backdrops"][0]["file_path"]
    print(film_id)
    print(response2.json())
    reuest2.setText(poster)


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