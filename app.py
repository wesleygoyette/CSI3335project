from flask import Flask, render_template, redirect, url_for, session
from flask_session import Session
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fer1feg1lk1nglek21gke121423rt0lkn1ge1l1kn1xglklg1krlkneg1lne'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register')
def register():
    # Implement registration logic if needed (not covered in this example)
    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.is_submitted:
        if "wes@wes" == form.email.data and "abc123" == form.password.data:

            session["isLoggedIn"] = True

            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", form=form, error="Invalid credentials")

    return render_template("login.html", form=form)

@app.route('/dashboard')
def dashboard():

    if not session.get("isLoggedIn"):
        return redirect(url_for("login"))

    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug=True)
