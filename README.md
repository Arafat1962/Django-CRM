# Django CRM Project

This Django CRM project allows users to manage customer records. The project is organized into a Django app named `website` within the `dcrm` project directory.

## Project Structure

- `dcrm/`: Django project directory.
  - `dcrm/settings.py`: Django settings for the project.
  - `website/`: Django app directory.
    - `admin.py`: Django admin configuration.
    - `apps.py`: Django app configuration.
    - `forms.py`: Forms used in the project.
    - `models.py`: Database models.
    - `urls.py`: URL patterns for the app.
    - `views.py`: Views for rendering web pages.
    - `templates/`: HTML templates.
      - `add_record.html`: Template for adding customer records.
      - `base.html`: Base template containing common elements.
      - `home.html`: Template for the home page displaying customer records.
      - `navbar.html`: Template for the navigation bar.
      - `record.html`: Template for displaying individual customer records.
      - `register.html`: Template for user registration.
      - `update_record.html`: Template for updating customer records.
    - `migrations/`: Database migration files.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Arafat1962/your-project.git
   cd dcrm
   ```

2. **Install Dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Database Setup:**
   - Update `dcrm/settings.py` with your database configuration in the `DATABASES` section.
   - Apply migrations:
     ```bash
     python manage.py migrate
     ```

4. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the Application:**
   Visit http://localhost:8000/ in your browser.

## Usage

- Home Page: http://localhost:8000/
- Add Record: http://localhost:8000/add_record/
- Update Record: http://localhost:8000/update_record/<record_id>/
- Delete Record: http://localhost:8000/delete_record/<record_id>/

## Contributing

If you would like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

## Credits

- [Bootstrap](https://getbootstrap.com/): Used for styling the web pages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
