# Credit Card Score Predictor & Analyzer

## Overview
The Credit Card Score Predictor & Analyzer is a web-based application designed to predict and analyze credit card scores using machine learning algorithms. The project utilizes the UCI Credit Card dataset for training and testing the model. The backend of the application is built using Django, and MySQL is used as the database. A Random Forest algorithm is used to predict the credit scores.

## Features
- **User Authentication**: Secure login and registration system for users.
- **Credit Score Prediction**: Users can input their financial details to predict their credit score using a Random Forest model.
- **Data Analysis**: Visual representation of the analysis of credit scores.
- **History Tracking**: Users can view their past credit score predictions.

## Project Structure
The project consists of several key components:
- `manage.py`: Script for managing the Django project.
- `requirements.txt`: File listing the required packages.
- `README.md`: Documentation for the project.
- `db.sqlite3`: SQLite database file (if using SQLite for development).
- `credit_predictor/`: Main application directory containing Django app code.
- `users/`: Application directory for handling user-related functionality.
- `config/`: Configuration directory containing settings and URL configurations.

## Installation

### Prerequisites
- Python 3.x
- Django 3.x
- MySQL 8.x
- MySQL Connector/Python

### Steps

1. **Clone the repository:**
   - Clone the project repository from GitHub to your local machine.

2. **Set up the virtual environment:**
   - Create a virtual environment for the project and activate it.

3. **Install the required packages:**
   - Install all necessary packages listed in the `requirements.txt` file.

4. **Database Configuration:**
   - Create a MySQL database.
   - Update the database settings in the `settings.py` file with your MySQL database credentials.

5. **Run migrations:**
   - Apply database migrations to set up the database schema.

6. **Load the UCI Credit Card dataset:**
   - Download the dataset from the UCI repository.
   - Load the dataset into your MySQL database using a script or Django management command.

7. **Create a superuser:**
   - Create an administrative user for accessing the Django admin interface.

8. **Run the server:**
   - Start the Django development server to run the application.

## Usage

1. **Access the application:**
   - Open your web browser and go to `http://127.0.0.1:8000/`.

2. **Register/Login:**
   - Register a new account or log in using existing credentials.

3. **Predict Credit Score:**
   - Navigate to the credit score prediction page, enter the required financial details, and submit the form to get your credit score.

4. **View Analysis:**
   - Access the data analysis section to view graphical representations and insights of credit scores.

## Machine Learning Model

The application uses a Random Forest algorithm for predicting credit scores. The model is trained using the UCI Credit Card dataset.

### Training the Model

1. **Preprocess the data:**
   - Handle missing values, normalize/scale features if necessary, and encode categorical variables.

2. **Train the Random Forest model:**
   - Split the data into training and testing sets, train the Random Forest model on the training data, and evaluate it on the test data.

3. **Save the trained model:**
   - Save the trained Random Forest model to a file for later use.

4. **Load and use the model in your Django views:**
   - Load the saved model file and use it to make predictions in your Django views.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes.
4. Commit your changes with a descriptive message.
5. Push your branch to your forked repository.
6. Create a Pull Request to the main repository.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements
- The UCI Machine Learning Repository for providing the Credit Card dataset.
- Django and MySQL for providing robust frameworks and tools for web development and database management.
- Scikit-learn for providing machine learning algorithms and tools.
