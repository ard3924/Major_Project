from flask import Flask,render_template,url_for,request

import pandas as pd 
import numpy as np


import pickle

app = Flask(__name__)

random_malware = pickle.load(open('logic_malware.pkl','rb'))
ExtraTree_malware = pickle.load(open('ExtraTree_malware.pkl','rb'))

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset)
        return render_template("preview.html",df_view = df)


@app.route('/prediction')
def prediction():
    return render_template("prediction.html")

@app.route('/predict',methods=["POST"])
def predict():
    if request.method == 'POST':
        
        permissions = [
            'ACCESS_ALL_DOWNLOADS', 'ACCESS_CACHE_FILESYSTEM', 'ACCESS_FINE_LOCATION',
            'ACCESS_NETWORK_STATE', 'ACCESS_SERVICE', 'ACCESS_SHARED_DATA', 'ACCESS_SUPERUSER',
            'ACCESS_WIFI_STATE', 'CAMERA', 'CHANGE_CONFIGURATION', 'DELETE_CACHE_FILES',
            'READ_ATTACHMENT', 'READ_CONTACTS', 'READ_DATA', 'READ_EXTERNAL_STORAGE',
            'READ_GMAIL', 'READ_HISTORY_BOOKMARKS', 'READ_MESSAGES', 'READ_PHONE_STATE',
            'READ_SETTINGS', 'READ_SMS', 'RECEIVE_BOOT_COMPLETED', 'RECEIVE_SMS'
        ]

        sample_data = [request.form[p] for p in permissions]
        
        # For rendering in result.html
        template_context = {p.lower(): "Yes" if request.form[p] == '1' else "No" for p in permissions}

        model = request.form['model']
        
		# Clean the data by convert from unicode to float 
        
        # clean_data = [float(i) for i in sample_data]
        # int_feature = [x for x in sample_data]
        int_feature = [float(i) for i in sample_data]
        print(int_feature)
    

		# Reshape the Data as a Sample not Individual Features
        
        ex1 = np.array(int_feature).reshape(1,-1)
        print(ex1)
		# ex1 = np.array([6.2,3.4,5.4,2.3]).reshape(1,-1)

        # Reloading the Model
        if model == 'LogisticRegression':
           result_prediction = random_malware.predict(ex1)
           
            
        elif model == 'ExtraTreeClassifier':
          result_prediction = ExtraTree_malware.predict(ex1)
           
           
        
        # if result_prediction > 0.5:
        #     result = 'Malware'
        # else:
        #     result = 'Benign'    

          

    return render_template('result.html', prediction_text=result_prediction[0], model=model, **template_context)

@app.route('/performance')
def performance():
    return render_template("performance.html")

@app.route('/chart')
def chart():
    return render_template("chart.html")    

if __name__ == '__main__':
	app.run(debug=True)
