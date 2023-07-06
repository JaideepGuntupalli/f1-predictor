import pandas as pd
from flask import Flask, jsonify, request
import joblib
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

model = joblib.load('rffinal.pkl')


@app.route('/predictGrid', methods=['POST', 'OPTIONS'])
@cross_origin()
def predictDriverPos():
    drivers = {18: 'Valtteri Bottas',
               8: 'Lance Stroll',
               6: 'George Russell',
               5: 'Fernando Alonso',
               10: 'Lewis Hamilton',
               17: 'Sergio Pérez',
               7: 'Kevin Magnussen',
               1: 'Carlos Sainz',
               9: 'Lando Norris',
               3: 'Charles Leclerc',
               12: 'Max Verstappen',
               16: 'Pierre Gasly',
               0: 'Alexander Albon',
               2: 'Carlos Sainz Jr.',
               19: 'Yuki Tsunoda',
               15: 'Oscar Piastri',
               4: 'Esteban Ocon',
               11: 'Logan Sargeant',
               20: 'Zhou Guanyu',
               13: 'Nico Hülkenberg',
               14: 'Nyck de Vries'}
    constructors = {9: 'Williams',
                    4: 'McLaren',
                    2: 'Ferrari',
                    5: 'Mercedes',
                    1: 'AlphaTauri',
                    0: 'Alfa Romeo',
                    7: 'Red Bull',
                    3: 'Haas F1 Team',
                    6: 'Racing Point',
                    8: 'Renault'}

    # jeddah . las vegas ,miami , qatar, imola  - missing ,
    rounds = {0: 'Albert Park Grand Prix Circuit',
              24: 'Shanghai International Circuit',
              4: 'Bahrain International Circuit',
              9: 'Circuit de Barcelona-Catalunya',
              10: 'Circuit de Monaco',
              18: 'Istanbul Park',
              25: 'Silverstone Circuit',
              21: 'Nürburgring',
              16: 'Hungaroring',
              28: 'Valencia Street Circuit',
              12: 'Circuit de Spa-Francorchamps',
              1: 'Autodromo Nazionale di Monza',
              20: 'Marina Bay Street Circuit',
              27: 'Suzuka Circuit',
              3: 'Autódromo José Carlos Pace',
              29: 'Yas Marina Circuit',
              7: 'Circuit Gilles Villeneuve',
              11: 'Circuit de Nevers Magny-Cours',
              15: 'Hockenheimring',
              14: 'Fuji Speedway',
              17: 'Indianapolis Motor Speedway',
              19: 'Korean International Circuit',
              26: 'Sochi Autodrom',
              5: 'Baku City Circuit',
              22: 'Red Bull Ring',
              13: 'Circuit of the Americas',
              2: 'Autódromo Hermanos Rodríguez',
              8: 'Circuit Paul Ricard',
              6: 'Buddh International Circuit'}

    constructor_reliabilities = {"Ferrari": 0.8243589743589743,
                                 "Red Bull": 0.7508650519031141,
                                 "Mercedes": 0.8778054862842892,
                                 "Racing Point": 0.5902335456475584,
                                 "Williams": 0.5699614890885751,
                                 "Alfa Romeo": 0.3952755905511811,
                                 "AlphaTauri": 0.4553903345724907,
                                 "McLaren": 0.6344916344916345,
                                 "Renault": 0.6018518518518519,
                                 "Haas F1 Team": 0.34302325581395354}

    driverconfidences = {"Lewis Hamilton": 0.9407114624505929, "George Russell": 0.9583333333333334,
                         "Max Verstappen": 0.9142857142857143, "Sergio Pérez": 0.9333333333333333,
                         "Charles Leclerc": 0.8444444444444444, "Carlos Sainz": 0.9038461538461539,
                         "Lando Norris": 0.9166666666666666, "Oscar Piastri": 0.8, "Esteban Ocon": 0.9230769230769231,
                         "Pierre Gasly": 0.9387755102040817, "Yuki Tsunoda": 0.8, "Nyck de Vries": 0.8,
                         "Fernando Alonso": 0.93266, "Lance Stroll": 0.9230769230769231,
                         "Valtteri Bottas": 0.965034965034965, "Zhou Guanyu": 0.8, "Alexander Albon": 0.956522,
                         "Logan Sargeant": 0.8, "Kevin Magnussen": 0.9523809523809523, "Nico Hülkenberg": 0.8}

    data = request.get_json(force=True)
    # input : round  ,driver name, quali pos
    # get the round, driver name and quali pos stored in variables from json
    driver_name = data['name']
    round = data['round']
    qualifying_pos = data['qualifying_pos']
    constructerselected = ""
    if driver_name == "Lewis Hamilton" or driver_name == "George Russel":
        constructerselected = "Mercedes"
    elif driver_name == "Max Verstappen" or driver_name == "Sergio Pérez":
        constructerselected = "Red Bull"
    elif driver_name == "Charles Leclerc" or driver_name == "Carlos Sainz":
        constructerselected = "Ferrari"
    elif driver_name == "Lando Norris" or driver_name == "Oscar Piastri":
        constructerselected = "McLaren"
    elif driver_name == "Esteban Ocon" or driver_name == "Pierre Gasly":
        constructerselected = "Alpine"
    elif driver_name == "Yuki Tsunoda" or driver_name == "Nyck de Vries":
        constructerselected = "AlphaTauri"
    elif driver_name == "Fernando Alonso" or driver_name == "Lance Stroll":
        constructerselected = "Aston Martin"
    elif driver_name == "Valtteri Bottas" or driver_name == "Zhou Guanyu":
        constructerselected = "Alfa Romeo"
    elif driver_name == "Alexander Albon" or driver_name == "Logan Sargeant":
        constructerselected = "Williams"
    elif driver_name == "Kevin Magnussen" or driver_name == "Nico Hülkenberg":
        constructerselected = "Haas F1 Team"

    # encode driver from the dict provided above
    driver_id = None
    for id, name in drivers.items():
        if name.lower() == driver_name.lower():
            driver_id = id
            break

    constructor_id = None
    for id, name in constructors.items():
        if name.lower() == constructerselected.lower():
            constructor_id = id
            break

    round_id = None
    for id, name in rounds.items():
        if name.lower() == round.lower():
            round_id = id
            break
    reliability = constructor_reliabilities[constructerselected]
    driverconfidence = driverconfidences[driver_name]
    data = {
        'GP_name': [round_id],
        'quali_pos': [qualifying_pos],
        'constructor': [constructor_id],
        'driver': [driver_id],
        'driver_confidence': [driverconfidence],
        'constructor_relaiblity': [reliability],
    }

    df = pd.DataFrame(data)
    prediction = model.predict(df)
    print(prediction)
    print(constructor_id)
    print(driverconfidence)
    print(reliability)
    print(driver_id)
    print(round_id)
    print(qualifying_pos)
    print(driver_name)
    print(constructerselected)
    print(round)

    results = prediction.tolist()
    results = jsonify(results)
    # results.headers.add('Access-Control-Allow-Origin', 'https://f1-predictor.gjd.one')
    results.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    results.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return results


if __name__ == '__main__':
    # app.run(debug=True, port=8000)
    app.run()
