from flask import Flask,render_template,request
import math
app = Flask(__name__)


import datetime
@app.route('/')
def home():
    return render_template('quattro_4.html')

@app.route('/Geometria', methods = ['GET'])
def geo():
    geometria = request.args.getlist("geometria")
    base = float(request.args.get('base'))
    altezza = float(request.args.get('altezza'))
    print(geometria)
    if geometria == ["Area", "Diagonale"]:
        area = base * altezza
        diagonale = math.sqrt(base ** 2 + altezza ** 2)
        return render_template('esercizio4.html', Area = area, Diagonale = diagonale)
    elif "Diagonale" in geometria:
        diagonale = math.sqrt(base ** 2 + altezza ** 2)
        return render_template('result_3.html', Diagonale = diagonale)
    elif "Area" in geometria:
        area = base * altezza
        return render_template('result_2.html',Base = base,Altezza=altezza, Area = area)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)