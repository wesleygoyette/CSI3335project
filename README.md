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

4. **Database Setup**:
   - Ensure you have MariaDB installed and running.
   - Create a MySQL database and import the provided database schema.
   - Update the `mysql` dictionary in the `csi3335sp2024.py` file with your MySQL database credentials.

5. **Run the Application**:
   Run the Flask application:
   ```bash
   python app.py
   ```
   The app will be accessible at `http://localhost:3000` in your web browser.

Remember to deactivate the virtual environment once you're done:
```bash
deactivate
```