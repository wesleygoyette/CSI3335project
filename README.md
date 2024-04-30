# Baseball Stats Flask App

This Flask application provides a platform to access and analyze baseball statistics. It utilizes a MySQL database containing data on teams, players, batting, pitching, and fielding statistics. Users can register, log in, and view statistics for specific teams and years.

## Installation and Setup

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/wesleygoyette/CSI3335project.git
   ```

2. **Set Up the Project Virtual Environment**:
   ```bash
   cd CSI3335project
   ```

   For Windows:
   ```bash
   python -m venv project_env
   .\project_env\Scripts\activate
   ```

   For Linux/MacOS:
   ```bash
   python3 -m venv project_env
   source project_env/bin/activate
   ```

3. **Install Dependencies**:
   After activating the virtual environment, install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have installed these flask libraries
   ```bash
   pip install flask_login
   pip install flask_wtf
   pip install flask_sqlalchemy
   pip install pymysql
   pip install "flask<3" "werkzeug<3"
   ```

5. **Database Setup**:
   - Ensure you have MariaDB installed and running.
   - Create a MySQL database called baseball_baddies and import the provided database schema
   ```SQL
   CREATE DATABASE baseball_baddies;
   USE baseball_baddies;
   \. baseballbaddies.sql
   ```
   - Update the `mysql` dictionary in the `csi3335sp2024.py` file with your MySQL database credentials.

6. **Run the Application**:
   Run the Flask application:
   ```bash
   python app.py
   ```
   The app will be accessible at `http://localhost:3000` in your web browser.

Remember to deactivate the virtual environment once you're done:
```bash
deactivate
```

### New Features:

- **Registration Functionality**: Users can now register accounts to personalize their experience and access additional features.
  
- **Search Persistence**: Improved search functionality now retains previous search queries, enhancing user convenience and navigation efficiency.
  
- **Team Page**: A new dedicated page has been added to display comprehensive information about teams, including years, wins, and losses, providing users with valuable insights into team performance over time.

- **Styling**: New CSS styles with a purple theme.
