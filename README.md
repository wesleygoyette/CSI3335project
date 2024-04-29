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
   - Ensure you have MySQL installed and running.
   - Create a MySQL database and import the provided database schema.
   - Update the `mysql` dictionary in the `app.py` file with your MySQL database credentials.

5. **Run the Application**:
   Run the Flask application:
   ```bash
   python app.py
   ```
   The app will be accessible at `http://localhost:3000` in your web browser.

## Usage

- **Register**: New users can register by providing a valid email and password.
- **Login**: Registered users can log in to access the application's features.
- **Home**: Upon login, users are directed to the home page where they can search for baseball statistics by team and year.
- **Search**: Users can select a team and a year to view batting, pitching, and fielding statistics for that team in the specified year.
- **Admin Dashboard**: Admin users have access to an admin dashboard where they can view user details and request logs.

## File Structure

- **app.py**: Main Flask application file containing routes and database models.
- **templates/**: Directory containing HTML templates for rendering pages.
- **static/**: Directory containing static files such as CSS stylesheets and JavaScript files.
- **requirements.txt**: File listing all required Python dependencies.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Remember to deactivate the virtual environment once you're done:
```bash
deactivate
```