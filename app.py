from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/churrasco')
def churrasco():
    adulto = int(request.args.get('adulto', 0))
  
    qtdCarne = adulto * 0.5
    valorCarne = qtdCarne * 50
    qtdLinguica = adulto* 0.3
    valorLinguica = qtdLinguica * 25
    qtdCerveja = adulto * 5
    valorCerveja = qtdCerveja*3.5
    qtdRefri = adulto * 0.5
    valorRefri = qtdRefri * (9.5 / 2)
    total = valorRefri+valorCarne+valorCerveja+valorLinguica
    

    

    return render_template('churrasco.html', qtdCarne = qtdCarne, valorCarne = valorCarne, qtdCerveja = qtdCerveja, qtdLinguica = qtdLinguica, qtdRefri =qtdRefri, total=total,valorCerveja=valorCerveja,valorLinguica=valorLinguica,valorRefri=valorRefri)

if __name__ == '__main__':
    app.run(debug=True)



    

