import os
import flask
import csv
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

def gauss(filename): #Метод Гаусса для реения системы линейных уравнений
    A = list()
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            A.append(row)

    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            A[i][j] = int(A[i][j])

    a = len(A[0])
    b = len(A)
    for k in range(0, a - 1): #По сути выбираем элементы глав. диагонали(те самый, на котрый буем делить)
        for q in range(k + 1, b): #Выбираем столбец, под элементом глав. диагонали, который мы выбрали выше
            for z in range(k, a): #Выбираем строку, начиная с элемента, индекс столбца которого равен индексу элемента на диагонаи
                w = A[q][k] / A[k][k]
                A[q][z] -= w * A[k][z]
    for l in range(b - 1, -1, - 1):
        for t in range(l - 1, -1, - 1):
            p = A[t][l] / A[l][l]
            A[t][a - 1] -= p * A[l][a - 1]
            A[t][l] = 0
    o = [0] * b
    for k in range(0, b): # Функция возваращает массив с решениями системы уравнений
      o[k] = A[k][k]
    return(o)

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.rsplit('.', 1)[1] == 'csv':
            filename = secure_filename(file.filename)
            file.save(os.path.join(filename))
            result = gauss(filename)
            os.remove(os.path.join(filename))
            file.close()
            return flask.render_template(
                'index.html', result=', '.join(str(e) for e in result)
            )
    return flask.render_template(
        'index.html', result = False
    )



if __name__ == '__main__':
    app.run()

