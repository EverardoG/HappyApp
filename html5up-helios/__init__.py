from flask import Flask, redirect, url_for, request, render_template
from SendEmail import sendEmailTo
import json
# from flask_wtf import Form
# from wtforms import TextField
app = Flask(__name__)
# from NamesCode.Web_Name_Feedback import main as train_names

#adjust_weight_web(adjust, key_word ,category_dict, pickup_line, all_dicts)
# adjust is modifier


@app.route('/', methods=['POST', 'GET']) #
def index(emailaddress=None):
    if request.method == 'POST':
        email = request.form["emailaddress"]
        print(email)
        sendEmailTo(email)
        print("it worked!")
    #pass
    return render_template('index.html')

@app.route('/done/')
def about():
    return render_template('done.html')

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
