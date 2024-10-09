from flask import Flask,render_template,url_for,request,redirect,flash
from form import infoForm
from model import load_my_model,predict
from PIL import UnidentifiedImageError,Image
import os

# Allowed file extensions for images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Check if the uploaded file has an allowed image extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this_is_a_secret_key'



@app.route('/',methods=["GET","POST"])
@app.route('/home',methods=["GET","POST"])


def home():
    message=""
    form = infoForm()
    return render_template("home.html",form=form,message=message)



@app.route('/analyse',methods =["GET","POST"])
def analyse():
    
    
    
    patient_name = request.form.get('patientname')
    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = file.filename
        img_path = 'static/uploads/' + filename 

        file.save(img_path)
        model = load_my_model("static/model/bt_fun.h5")
        result = predict(img_path,model)
        return render_template("analyse.html", patient_name=patient_name, path=img_path, result=result)
    form = infoForm()
    message = "Please Upload Image(png, jpg, jpeg, gif)"
    return render_template("home.html",form=form,message=message)

 
if __name__ == '__main__':
    app.run(debug=True)