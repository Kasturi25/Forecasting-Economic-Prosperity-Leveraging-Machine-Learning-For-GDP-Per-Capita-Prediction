from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = [
            float(request.form['region']),
            float(request.form['area']),
            float(request.form['coastline']),
            float(request.form['phone']),
            float(request.form['crops']),
            float(request.form['birthrate']),
            float(request.form['agriculture']),
            float(request.form['population']),
            float(request.form['population_density']),
            float(request.form['net_migration']),
            float(request.form['arable']),
            float(request.form['climate']),
            float(request.form['deathrate']),
            float(request.form['industry'])
        ]
        
        # Predict using the loaded model
        prediction = model.predict([data])
        prediction = prediction[0]
    except Exception as e:
        return str(e)

    return render_template('gdp_pred.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
