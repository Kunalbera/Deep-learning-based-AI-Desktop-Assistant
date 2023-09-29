from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv("Cleaned_Car.csv")


@app.route('/',methods=['GET','POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique())
    fuel_type = sorted(car['fuel_type'].unique(), reverse=True)

    companies.insert(0,"Select Company")
    car_models.insert(0, "Select Car Model")
    year.insert(0, "Select Year Of Purchase")
    fuel_type.insert(0, "Select Fuel Type")
    return render_template('index.html', companies=companies, car_models=car_models, year=year, fuel_type=fuel_type)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        company = request.form.get('company')
        car_model = request.form.get('car_models')
        year = int(request.form.get('year'))
        fuel_type = request.form.get('fuel_type')
        kms_driven = int(request.form.get('kilo_driven'))
        print(company, car_model, year, fuel_type, kms_driven)

        prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                                data=np.array([car_model, company, year, kms_driven, fuel_type]).reshape(1,5)))
        print(prediction)
        return str(np.round(prediction[0]))

    except ValueError:
        return "Please Fill All The Required Fields !!"


if __name__ == "__main__":
    app.run(debug=True)
