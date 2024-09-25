from flask import * # bad practice
import pickle

app = Flask(__name__)

# model = pickle.load(open('./model/model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def welcome():

    data = {
        'message': 'Bienvenido a  MetaFoodCraft',
        'status': 'success',
        'items': ['🍌', '🍏', '🍉', '🥝']
    }

    return jsonify(data)

@app.route('/new', methods=['POST'])
def newUser():
    data = request.get_json()

    print(data)  # Imprimir los datos recibidos

    return jsonify({"message": "Datos recibidos", "data": data}), 200


@app.route("/predecir", methods=['POST'])
def predict():
    cuartos = int(request.form['cuartos'])
    distancia = int(request.form['distancia'])
    
    predict = model.predict([[cuartos, distancia]])    
    
    output = round(predict[0], 2)

    return render_template('index.html', predictText=f'La ksa con 4 cuartos tiene {predict}')

if __name__ == '__main__':
    app.run()