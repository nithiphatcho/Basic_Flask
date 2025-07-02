from flask import Flask,render_template,request,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,RadioField,SelectField,TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
Bootstrap(app)

class MyForm(FlaskForm):
    name = StringField("ป้อนชื่อของคุณ",validators=[DataRequired()])
    isAccept= BooleanField("ยอมรับเงื่อนไขบริการข้อมูล")
    gender = RadioField('เพศ',choices=[('M','ชาย'),('F','หญิง'),('O','อื่นๆ')])
    skill = SelectField('ความสามารถพิเศษ',choices=[('พูดภาษาอังกฤษ','พูดภาษาอังกฤษ'),('ร้องเพลง','ร้องเพลง'),('เขียนเกม','เขียนเกม')])
    address = TextAreaField("ที่อยู่ของคุณ")
    submit = SubmitField("บันทึก")

@app.route('/',methods=['GET','POST'])
def index():
    # name = False
    # isAccept = False
    # gender = False
    # skill = False
    # address = False

    form=MyForm()
    if form.validate_on_submit():
        flash("บันทึกข้อมูลเรียบร้อย")
        session['name'] = form.name.data
        session['isAccept'] = form.isAccept.data
        session['gender'] = form.gender.data
        session['skill'] = form.skill.data
        session['address'] = form.address.data
        # Clear Data
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
        form.address.data = ""
    return render_template("index.html",form=form)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/admin')
def profile():
    return render_template("admin.html")

# @app.route('/')
# def index():
#     data = {"name":"Nithiphat","age":30,"salary":"18000"}
#     return render_template("index.html",mydata = data)

# @app.route('/about')
# def about():
#     product = ["เสื้อผ้า","เตารีด","ผ้าห่ม","ยาสามัญประจำบ้าน","คีย์บอร์ด"]
#     return render_template("about.html",myproduct = product)

# @app.route('/admin')
# def profile():
#     #ชื่อ อายุ
#     username = "Nithiphat"
#     return render_template("admin.html",username = username)

# @app.route('/sendData')
# def signupForm():
#     fname=request.args.get('fname')
#     description=request.args.get('description')
#     return render_template("thankyou.html",data={"name":fname, "description":description})

# @app.route('/user/<name>/<age>')
# def member(name,age):
#     return "<h1>ชื่อ : {}, อายุ : {} </h1>".format(name[0],age)

if __name__ == "__main__":
    app.run(debug=True)