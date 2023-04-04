from flask import Flask,render_template,request
app = Flask(__name__)

import datetime
@app.route('/')
def home():
    return render_template('due_2.html')

@app.route('/Area', methods = ['GET'])
def Arearett():
    if request.args.get('base').isdigit() == True and  request.args.get('altezza').isdigit() == True:
        base = float(request.args.get('base'))
        altezza = float(request.args.get('altezza'))
        if base > 0 and altezza > 0 :
            area = base * altezza
            return render_template('result_2.html',Base = base,Altezza=altezza, Area = area)

        else:
            return render_template('errore.html', msg= "dati negativi")
    else:
         return render_template('errore.html', msg= "hai inserito una stringa")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)