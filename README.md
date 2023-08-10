# My-Car-Care
Final exam project.

The Car Care App is a Django-based web application designed to help users manage and track maintenance tasks for their vehicles. Whether you're a car enthusiast or simply want to keep your vehicle in optimal condition, this app provides an organized way to stay on top of maintenance needs.

![Screenshot](screenshot.png)  <!-- Replace with an actual screenshot if available -->

## Features

- **User Authentication:** Secure user registration and login system.
- **Vehicle Management:** Add, edit, and delete vehicles with details like make, model, and year.
- **Maintenance Tracking:** Log maintenance tasks for each vehicle, including date, type, and notes.
- **User Roles:** Differentiate between regular users and maintenance moderators.
- **Maintenance Moderation:** Authorized users can moderate and approve maintenance tasks.
- **Responsive Design:** The app is designed to work seamlessly on both desktop and mobile devices.

## Installation

1. Clone the repository: `git clone https://github.com/ZahariBakov/My-Car-Care`
2. Navigate to the project directory: `cd car-care-app`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: 
   `source venv/bin/activate` (Unix-based),
   `venv\Scripts\activate` (Windows)
5. Install the dependencies: `pip install -r requirements.txt`
6. Set up the database: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`

## Usage

1. Access the admin panel by visiting `http://localhost:8000/admin/` and log in with your superuser account.
2. Add vehicles and maintenance tasks through the admin panel.
3. Regular users can log in and manage their vehicles and maintenance tasks.
4. Maintenance moderators can edit or delete maintenance tasks.
5. Car moderators can edit or delete car tasks.
6. Master user group can edit or delete all car and maintenance tasks.


## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m "Add your message"`
4. Push to the branch: `git push origin feature-name`
5. Create a pull request with a description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
- [Font Awesome](https://fontawesome.com/) - The iconic SVG, font, and CSS toolkit.


