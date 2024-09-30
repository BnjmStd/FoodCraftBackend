from flask import * # bad practice
import pickle

# ORM 
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

if __name__ == '__main__':
    app.run()