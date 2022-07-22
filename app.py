from flask import Flask, request, render_template
import pandas as pd
import joblib

# Declare a Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("dashboard.html")

@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        clf = joblib.load("clf.pkl")
        
        # Get values through input bars
        account_length = request.form.get("account_length")
        location_code = request.form.get("location_code")
        intertiol_plan = request.form.get("intertiol_plan")
        voice_mail_plan = request.form.get("voice_mail_plan")
        number_vm_messages = request.form.get("number_vm_messages")
        total_day_min = request.form.get("total_day_min")
        total_day_calls = request.form.get("total_day_calls")
        total_day_charge = request.form.get("total_day_charge")
        total_eve_min = request.form.get("total_eve_min")
        total_eve_calls = request.form.get("total_eve_calls")
        total_eve_charge = request.form.get("total_eve_charge")
        total_night_minutes = request.form.get("total_night_minutes")
        total_night_calls = request.form.get("total_night_calls")
        total_night_charge = request.form.get("total_night_charge")
        total_intl_minutes = request.form.get("total_intl_minutes")
        total_intl_calls = request.form.get("total_intl_calls")
        total_intl_charge = request.form.get("total_intl_charge")
        customer_service_calls = request.form.get("customer_service_calls")
        
        # Put inputs to dataframe
        X = pd.DataFrame([[account_length, location_code,
                           intertiol_plan, voice_mail_plan, number_vm_messages,
                           total_day_min, total_day_calls, total_day_charge,
                           total_eve_min, total_eve_calls, total_eve_charge,
                           total_night_minutes, total_night_calls, total_night_charge,
                           total_intl_minutes, total_intl_calls, total_intl_charge,
                           customer_service_calls
                           ]], columns =
                         ["account_length",
                          "location_code",
                          "intertiol_plan", "voice_mail_plan", "number_vm_messages",
                          "total_day_min", "total_day_calls", "total_day_charge",
                          "total_eve_min", "total_eve_calls", "total_eve_charge",
                          "total_night_minutes", "total_night_calls", "total_night_charge",
                          "total_intl_minutes", "total_intl_calls", "total_intl_charge",
                          "customer_service_calls"
                          ])
        
        # Get prediction
        prediction = clf.predict(X)[0]
        
    else:
        prediction = ""
        
    return render_template("result.html", output = prediction)

# Running the app
if __name__ == '__main__':
    app.run(debug = True)
