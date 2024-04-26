from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask_user:abc12345@localhost/test'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.email}')"
    
class Team(db.Model):
    __tablename__ = 'teams'
    
    teams_ID = db.Column(db.Integer, primary_key=True)
    teamID = db.Column(db.String(3), nullable=False)
    yearID = db.Column(db.SmallInteger, nullable=False)
    lgID = db.Column(db.String(2))
    divID = db.Column(db.String(1))
    franchID = db.Column(db.String(3))
    team_name = db.Column(db.String(50))
    team_rank = db.Column(db.SmallInteger)
    team_G = db.Column(db.SmallInteger)
    team_G_home = db.Column(db.SmallInteger)
    team_W = db.Column(db.SmallInteger)
    team_L = db.Column(db.SmallInteger)
    DivWin = db.Column(db.String(1))
    WCWin = db.Column(db.String(1))
    LgWin = db.Column(db.String(1))
    WSWin = db.Column(db.String(1))
    team_R = db.Column(db.SmallInteger)
    team_AB = db.Column(db.SmallInteger)
    team_H = db.Column(db.SmallInteger)
    team_2B = db.Column(db.SmallInteger)
    team_3B = db.Column(db.SmallInteger)
    team_HR = db.Column(db.SmallInteger)
    team_BB = db.Column(db.SmallInteger)
    team_SO = db.Column(db.SmallInteger)
    team_SB = db.Column(db.SmallInteger)
    team_CS = db.Column(db.SmallInteger)
    team_HBP = db.Column(db.SmallInteger)
    team_SF = db.Column(db.SmallInteger)
    team_RA = db.Column(db.SmallInteger)
    team_ER = db.Column(db.SmallInteger)
    team_ERA = db.Column(db.Float)
    team_CG = db.Column(db.SmallInteger)
    team_SHO = db.Column(db.SmallInteger)
    team_SV = db.Column(db.SmallInteger)
    team_IPouts = db.Column(db.Integer)
    team_HA = db.Column(db.SmallInteger)
    team_HRA = db.Column(db.SmallInteger)
    team_BBA = db.Column(db.SmallInteger)
    team_SOA = db.Column(db.SmallInteger)
    team_E = db.Column(db.SmallInteger)
    team_DP = db.Column(db.SmallInteger)
    team_FP = db.Column(db.Float)
    park_name = db.Column(db.String(50))
    team_attendance = db.Column(db.Integer)
    team_BPF = db.Column(db.SmallInteger)
    team_PPF = db.Column(db.SmallInteger)
    team_projW = db.Column(db.SmallInteger)
    team_projL = db.Column(db.SmallInteger)

# Define the Batting model
class Batting(db.Model):
    __tablename__ = 'batting'
    
    batting_ID = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.String(9), nullable=False)
    yearID = db.Column(db.SmallInteger, nullable=False)
    teamID = db.Column(db.String(3), nullable=False)
    stint = db.Column(db.SmallInteger, nullable=False)
    b_G = db.Column(db.SmallInteger)
    b_AB = db.Column(db.SmallInteger)
    b_R = db.Column(db.SmallInteger)
    b_H = db.Column(db.SmallInteger)
    b_2B = db.Column(db.SmallInteger)
    b_3B = db.Column(db.SmallInteger)
    b_HR = db.Column(db.SmallInteger)
    b_RBI = db.Column(db.SmallInteger)
    b_SB = db.Column(db.SmallInteger)
    b_CS = db.Column(db.SmallInteger)
    b_BB = db.Column(db.SmallInteger)
    b_SO = db.Column(db.SmallInteger)
    b_IBB = db.Column(db.SmallInteger)
    b_HBP = db.Column(db.SmallInteger)
    b_SH = db.Column(db.SmallInteger)
    b_SF = db.Column(db.SmallInteger)
    b_GIDP = db.Column(db.SmallInteger)

# Define the Pitching model
class Pitching(db.Model):
    __tablename__ = 'pitching'
    
    pitching_ID = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.String(9), nullable=False)
    yearID = db.Column(db.SmallInteger, nullable=False)
    teamID = db.Column(db.String(3), nullable=False)
    stint = db.Column(db.SmallInteger, nullable=False)
    p_W = db.Column(db.SmallInteger)
    p_L = db.Column(db.SmallInteger)
    p_G = db.Column(db.SmallInteger)
    p_GS = db.Column(db.SmallInteger)
    p_CG = db.Column(db.SmallInteger)
    p_SHO = db.Column(db.SmallInteger)
    p_SV = db.Column(db.SmallInteger)
    p_IPOuts = db.Column(db.Integer)
    p_H = db.Column(db.SmallInteger)
    p_ER = db.Column(db.SmallInteger)
    p_HR = db.Column(db.SmallInteger)
    p_BB = db.Column(db.SmallInteger)
    p_SO = db.Column(db.SmallInteger)
    p_BAOpp = db.Column(db.Float)
    p_ERA = db.Column(db.Float)
    p_IBB = db.Column(db.SmallInteger)
    p_WP = db.Column(db.SmallInteger)
    p_HBP = db.Column(db.SmallInteger)
    p_BK = db.Column(db.SmallInteger)
    p_BFP = db.Column(db.SmallInteger)
    p_GF = db.Column(db.SmallInteger)
    p_R = db.Column(db.SmallInteger)
    p_SH = db.Column(db.SmallInteger)
    p_SF = db.Column(db.SmallInteger)
    p_GIDP = db.Column(db.SmallInteger)
    
# Define the People model
class People(db.Model):
    __tablename__ = 'people'
    
    playerID = db.Column(db.String(9), primary_key=True)
    birthYear = db.Column(db.Integer)
    birthMonth = db.Column(db.Integer)
    birthDay = db.Column(db.Integer)
    birthCountry = db.Column(db.String(255))
    birthState = db.Column(db.String(255))
    birthCity = db.Column(db.String(255))
    deathYear = db.Column(db.Integer)
    deathMonth = db.Column(db.Integer)
    deathDay = db.Column(db.Integer)
    deathCountry = db.Column(db.String(255))
    deathState = db.Column(db.String(255))
    deathCity = db.Column(db.String(255))
    nameFirst = db.Column(db.String(255))
    nameLast = db.Column(db.String(255), index=True)
    nameGiven = db.Column(db.String(255))
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    bats = db.Column(db.String(255))
    throws = db.Column(db.String(255))
    debutDate = db.Column(db.Date)
    finalGameDate = db.Column(db.Date)

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=["GET", "POST"])
@login_required
def home():

    if request.args.get("team") and request.args.get("year"):

        team_name = request.args.get("team")
        year = request.args.get("year")

        team = Team.query.filter_by(team_name=team_name).first()

        if team:
            team_id = team.teamID

            batting_stats = db.session.query(Batting, People).join(People, Batting.playerID == People.playerID).filter(Batting.teamID == team_id, Batting.yearID == year).all()
            pitching_stats = db.session.query(Pitching, People).join(People, Pitching.playerID == People.playerID).filter(Pitching.teamID == team_id, Pitching.yearID == year).all()

            if batting_stats and pitching_stats:

                return render_template('result.html', team=team_name, year=year, batting_stats=batting_stats, pitching_stats=pitching_stats)
            else:
                return render_template('404.html'), 404
        else:
            return render_template('404.html'), 404
        

    team_names = db.session.query(Team.team_name).distinct().order_by(Team.team_name).all()
    # Convert the result to a list of strings
    team_names_list = [name[0] for name in team_names]

    # Query team names and corresponding years
    team_data = db.session.query(Team.team_name, Team.yearID).distinct().order_by(Team.team_name, Team.yearID.desc()).all()
    
    # Convert the result to a dictionary where keys are team names and values are lists of years
    team_years_dict = {}
    for team, year in team_data:
        if team in team_years_dict:
            team_years_dict[team].append(year)
        else:
            team_years_dict[team] = [year]

    if request.args.get("prevTeam") and request.args.get("prevYear"):
        return render_template('search.html', teams=team_names_list, team_years_dict=team_years_dict, prevTeam=request.args.get("prevTeam"), prevYear=request.args.get("prevYear"))
    else:
        return render_template('search.html', teams=team_names_list, team_years_dict=team_years_dict)

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    next_page = request.args.get('next')

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(next_page or url_for('home'))

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.is_submitted():
        if form.validate():

            existing_user_email = User.query.filter_by(email=form.email.data).first()

            if existing_user_email:
                return render_template('register.html', form=form, error="Email already exists")

            hashed_password = generate_password_hash(form.password.data, method='sha256')
            new_user = User(email=form.email.data, password=hashed_password)
            
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login'))
        else:
            return render_template('register.html', form=form, error="Password must match")

    return render_template('register.html', form=form)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == '__main__':

    app.run(debug=True, host="localhost", port=3000)
