from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/juegos/wutering-waves')
def juego_wutering_waves():
    images=[
        (0,"image/wutering/camelia-4.jpg"),
        (1,"image/wutering/iuno-1.jpg"),
        (2,"image/wutering/jinshi-3.jpg")

    ]
    return render_template('wuwa.html',images=images,carousel_id='carrusel_wuwa')

@app.route('/juegos/genshin-impact')
def juego_genshin_impact():
    images= [
        (0,'image/genshin/ei.jpg'),
        (1,'image/genshin/furina.jpg'),
        (2,'image/genshin/emelie.jpg')
    ]

    return render_template('genshin.html',images=images,carousel_id='carrusel_genshin')

if __name__ == ('__main__'):
    app.run(debug=True)