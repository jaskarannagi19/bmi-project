from flask import *
from demo import run_file





app = Flask(__name__)



@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')




@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save("uploads/"+f.filename)

        bmi = run_file("uploads/"+f.filename)

    return "Calculated BMI=={}".format(bmi)












if __name__ == '__main__':
    app.run(debug = True)