from csi3335sp2024 import mysql
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash

log_file_name = "requests.log"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fewfwfefgelkngelknglkenlknelgknlekngrlknelknelgkn'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{mysql['user']}:{mysql['password']}@{mysql['location']}/{mysql['database']}"

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False, default=False)

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

    @property
    def slugging_percentage(self):
        return round(((self.b_HR * 4) + (self.b_3B * 3) + (self.b_2B * 2) + (self.b_H - self.b_3B - self.b_2B - self.b_HR)) / self.b_AB,2) if self.b_AB != 0 else 0

    @property
    def batting_average(self):
        return round(self.b_H / self.b_AB, 2) if self.b_AB != 0 else 0

    @property
    def on_base_percentage(self):
        ab = self.b_AB if self.b_AB is not None else 0
        bb = self.b_BB if self.b_BB is not None else 0
        hbp = self.b_HBP if self.b_HBP is not None else 0
        sf = self.b_SF if self.b_SF is not None else 0
        
        denominator = ab + bb + hbp + sf
        
        return round((self.b_H + bb + hbp) / denominator, 2) if denominator != 0 else 0

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

    @property
    def IP(self):
        return round(self.p_IPOuts / 3, 2) if self.p_IPOuts is not None else 0
    
    @property
    def WHiP(self):
        return round((self.p_BB + self.p_H) / (self.p_IPOuts / 3), 2) if self.p_IPOuts is not None and (self.p_BB + self.p_H) is not None else 0
    
    @property
    def SO9(self):
        return round(9 * self.p_SO / (self.p_IPOuts / 3), 2) if self.p_IPOuts is not None and self.p_SO is not None else 0
    
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

class Fielding(db.Model):
    __tablename__ = 'fielding'
    
    fielding_ID = db.Column(db.Integer, primary_key=True)
    playerID = db.Column(db.String(9), nullable=False)
    yearID = db.Column(db.SmallInteger, nullable=False)
    teamID = db.Column(db.String(3), nullable=False)
    stint = db.Column(db.SmallInteger, nullable=False)
    position = db.Column(db.String(2))  # nullable set to True as per the table description
    f_G = db.Column(db.SmallInteger)
    f_GS = db.Column(db.SmallInteger)
    f_InnOuts = db.Column(db.SmallInteger)
    f_PO = db.Column(db.SmallInteger)
    f_A = db.Column(db.SmallInteger)
    f_E = db.Column(db.SmallInteger)
    f_DP = db.Column(db.SmallInteger)
    f_PB = db.Column(db.SmallInteger)
    f_WP = db.Column(db.SmallInteger)
    f_SB = db.Column(db.SmallInteger)
    f_CS = db.Column(db.SmallInteger)
    f_ZR = db.Column(db.Float)

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

@app.before_request
def log_request_info():
    if current_user.is_authenticated and current_user.email:
        with open(log_file_name, 'a') as file:
            file.write(current_user.email + ": " + request.method + " " + request.full_path + "\n") 
        

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

@app.route('/', methods=["GET"])
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
            fielding_stats = db.session.query(Fielding, People).join(People, Fielding.playerID == People.playerID).filter(Fielding.teamID == team_id).group_by(Fielding.yearID, Fielding.position).order_by(People.playerID).all()

            if batting_stats and pitching_stats:

                return render_template('result.html', team=team_name, year=year, batting_stats=batting_stats, pitching_stats=pitching_stats, fielding_stats=fielding_stats)
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

@app.route('/admin')
@login_required
def admin():
    if not current_user.isAdmin:

        return redirect(url_for('home'))
    else:

        users = User.query.with_entities(User.email, User.isAdmin).all()
        user_details = [{'email': user[0], 'isAdmin': user[1]} for user in users]

        all_lines = [] 
        total_requests = 0

        with open(log_file_name, 'r') as file:
            for line in file:
                all_lines.append(line.strip()) 
                total_requests += 1

        all_lines.reverse()
        
        return render_template('admin.html', all_lines=all_lines, total_requests=total_requests, user_details=user_details)
    
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=3000)
