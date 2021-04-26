from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index1():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def index2():
    return '</br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!'])


@app.route('/image_mars')
def index3():
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="static/img/image.jpg"
                        width="500"
                        height="500" 
                        alt="Марс">
                        <figcaption>Вот она какая, красная планета.</figcaption>
                      </body>
                    </html>'''


@app.route('/promotion_image')
def index4():
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" href="static/css/style11.css" type="text/css"/>
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="static/img/image.jpg"
                        width="500"
                        height="500" 
                        alt="Марс">
                        <div class="alert alert-default">
                          <strong>Человечество вырастает из детства.</strong>
                        </div>
                        <div class="alert alert-success">
                          <strong>Человечеству мала одна планета.</strong>
                        </div>
                        <div class="alert alert-default">
                          <strong>Мы сделаем обитаемыми безжизненные пока планеты.</strong>
                        </div>
                        <div class="alert alert-warning">
                          <strong>И начнем с Марса!</strong>
                        </div>
                        <div class="alert alert-danger">
                          <strong>Присоединяйся!</strong>
                        </div>
                      </body>
                    </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def index5():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотогрфии</h1>
                            <h3 align="center">Для участия в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file" required>
                                    </div>
                                    <br>
                                    <div class="photo">
                                        <img src="{url_for('static', filename='img/image1.png')}" width="286" height="407"
                                        alt="здесь должна была быть картинка, но не нашлась">
                                    </div>
                                    <br>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['file'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')