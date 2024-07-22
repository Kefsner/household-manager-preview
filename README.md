# Household Manager

## Overview
Household Manager is a robust web application designed to efficiently manage household activities. It provides tools to oversee finances, organize shopping lists, securely store documents, and more, tailored to meet the unique needs of each household.

### Features in V1.0
- **User Authentication**: Securely register and log in to access personalized household management tools.
- **Finance Management**: Track incomes and expenses, manage credit card transactions, and derive financial insights through interactive dashboards.
- **Multi-user Support**: Allows multiple users to collaboratively manage household activities, enhancing cooperative planning and tracking.
- **Data Visualization**: Uses Chart.js for dynamic and responsive financial charts and graphs.

### Planned Future Features
- **Shopping List Management**: Create, manage, and analyze shopping lists to monitor shopping habits and predict future costs.
- **AI-Enhanced Tools**: Utilize AI-driven predictions to forecast shopping expenses and suggest frequent purchases.
- **Document Storage**: Secure options for storing and organizing important household documents.
- **Mobile App Integration**: Develop a mobile application for accessible household management on-the-go.
- **Task Management**: Manage daily tasks efficiently with a comprehensive to-do list feature.
- **Bill Management**: Track and manage regular household bills such as utilities.
- **Note-Taking Capabilities**: Implement enhanced note-taking features, including voice-to-text and image recognition functionalities.
- **Multi Language Support**: Enable multi-language support for global accessibility.
- **Import Bank Statements**: Allow users to import bank statements for automated financial tracking.

## Technologies
- **Frontend/Backend**: Developed using Django.
- **Database**: Currently uses SQLite3, with plans to transition to PostgreSQL for production.
- **Data Visualization**: Implemented with Chart.js.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.12 or higher
- Django 5.0.6
- Dependencies as listed in the `requirements.txt` file.

### Installation
To install Household Manager for local development:
1. Clone the repository:
   ```bash
   git clone https://github.com/Kefsner/household-manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd household-manager
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
To run Household Manager locally:
1. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```
2. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
3. Access the application at `http://localhost:8000`.

Future deployment plans include hosting the application on a live server to enable remote access and developing a mobile app for enhanced accessibility.

## Contributors
- **Kesley Raimundo** - *Initial Development* - [Kefsner](https://github.com/Kefsner)

## License
This project is protected under proprietary rights. For more details, see the [LICENSE.md](LICENSE.md) file.