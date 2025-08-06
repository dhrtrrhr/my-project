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

reuest2 = QLabel("a")
reuest3 = QLabel("x")
reuest4 = QLabel("c")

h1 = QVBoxLayout()
h1.addWidget(reqest1)
h1.addWidget(reqest1_2)
h1.addWidget(reqest1_3)
h1.addWidget(reuest2)
h1.addWidget(reuest3)
h1.addWidget(reuest4)

def search():
   
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?query={reqest1_2.text()}", headers=headers)
    result = response.json()
    print(result)
    response2 = requests.get("https://api.themoviedb.org/3/movie/{movie_id}/images")
    result2 = response.json()
    name = result[reqest1_2.text()]
    # poster = response2[name]
reqest1.clicked.connect(search)





window.setLayout(h1)
window.show()
app.exec()