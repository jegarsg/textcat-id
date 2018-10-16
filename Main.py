from flask import Flask,jsonify,request
from Model.Dataseed import tasks
from Model.Teks import Teks
from flasgger import Swagger
import spacy

app = Flask(__name__)
Swagger(app)

def load_spacy_model():
    global model

    model = spacy.load("C:\\Users\\JEGARSG\\Music\\15iterasi")
    print('Model loaded successfully..')

@app.route("/get/task",methods =['GET'])
def getTask():

    """
    Ini endpoint get.
    ---
    tags:
        - Rest Controller
    parameter:
    responses:
        200:
            description: Success Get Data

    """
    return jsonify({'tasks': tasks})

@app.route("/predict",methods =['POST'])
def predict():
    """
        Ini adalah endpoint untuk prediksi model.
        ---
        tags:
            - Rest Controller
        parameters:
          - name : body
            in: body
            required: true
            schema:
                id: -Teks
                required:
                    - teks
                properties:
                    teks:
                        type: string
                        description: Masukkan kalimat yang kan diprediksi.
                        default: ""
        responses:
            200:
                description: Prediksi Sukses.


        """
    data = {'success': False}
    data['predictions']=[]


    new_task = request.get_json()
    teks = new_task['teks']

    # ---prediksi sentimen kalimat----#
    pred = model(teks)

    data['predictions'].append(pred.cats)
    data["success"] = True

    return jsonify(data)



if __name__ == '__main__':
    load_spacy_model()
    app.run(debug = True)
