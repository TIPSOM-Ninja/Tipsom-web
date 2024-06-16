# Tipsom Web Installation Guide

## Step 1: Install Required Software

### Install Python and Git

1. **Download and Install Python**
   - Go to the [official Python website](https://www.python.org/downloads/).
   - Click on the download button for the latest version of Python.
   - Run the installer. Make sure to check the box that says "Add Python to PATH" during installation.
   - Follow the installation prompts to complete the setup.

2. **Download and Install Git**
   - Go to the [official Git website](https://git-scm.com/download/win).
   - Click on the download button to get the latest version of Git for Windows.
   - Run the installer and follow the installation prompts to complete the setup.

### Install PostgreSQL

1. **Download and Install PostgreSQL**
   - Go to the [official PostgreSQL website](https://www.postgresql.org/download/windows/).
   - Click on the download link for Windows.
   - Run the installer. During installation, take note of the username (typically `postgres`) and password you set up. You will need these credentials later.

## Step 2: Prepare the Database

1. **Open pgAdmin or SQL Shell (psql)**
   - If you installed pgAdmin, open it from the Start menu.
   - If you prefer using the command line, open the SQL Shell (psql) from the Start menu.

2. **Create the Database and User**
   - In pgAdmin, connect to your PostgreSQL server using your username and password.
   - Open the Query Tool and run the following SQL commands:
     ```sql
     CREATE DATABASE tipnet;
     CREATE USER tipnetuser WITH PASSWORD 'T1p50m@2024';
     ALTER ROLE tipnetuser SET client_encoding TO 'utf8';
     ALTER ROLE tipnetuser SET default_transaction_isolation TO 'read committed';
     ALTER ROLE tipnetuser SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE tipnet TO tipnetuser;
     ```
   - If using the SQL Shell (psql), run the same commands directly in the shell.

## Step 3: Get the Application Code

1. **Open a Command Prompt or PowerShell**
   - Press `Win + R`, type `cmd` or `powershell`, and press Enter.

2. **Navigate to Your Desired Directory**
   - Use the `cd` command to change directories. For example:
     ```sh
     cd C:\path\to\your\desired\directory
     ```

3. **Clone the Repository**
   - Run the following command to clone the repository:
     ```sh
     git clone {find the link you need}
     ```

## Step 4: Set Up the Django Application

1. **Navigate to the Project Directory**
   - Use the `cd` command to enter the project directory:
     ```sh
     cd case_interview_app
     ```

2. **Set Up a Virtual Environment**
   - Create a virtual environment:
     ```sh
     python -m venv venv
     ```
   - Activate the virtual environment:

     **Windows Command Prompt:**
     ```sh
     venv\Scripts\activate
     ```

     **PowerShell:**
     ```sh
     .\venv\Scripts\Activate.ps1
     ```

3. **Install Project Dependencies**
   - Install the necessary Python packages using pip:
     ```sh
     pip install -r requirements.txt
     ```

4. **Configure the .env File**
   - Navigate to the `tipnet` directory:
     ```sh
     cd tipnet
     ```
   - Copy the example `.env` file and edit it:
     ```sh
     copy .env.example .env
     notepad .env
     ```
   - Edit the `.env` file to include the correct URL, database connection details, and SMTP details. Save and close the file.

5. **Migrate the Database**
   - Apply the database migrations:
     ```sh
     python manage.py migrate
     ```

6. **Load the Database Dump (if provided)**
   - Load the provided SQL dump file:
     ```sh
     psql -U tipnetuser -d tipnet -f tipnet_dump.sql
     ```

7. **Create a Superuser for Django's Admin**
   - Create a superuser account:
     ```sh
     python manage.py createsuperuser
     ```

8. **Collect Static Files**
   - Collect static files for the Django project:
     ```sh
     python manage.py collectstatic
     ```

## Step 5: Run the Django Development Server

- Start the Django development server to test your application locally:
  ```sh
  python manage.py runserver
  ```

- Open a web browser and go to `http://127.0.0.1:8000/` to access the application.

## Step 6: Access Django Admin

- To access the Django admin panel, navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created earlier.

## Troubleshooting

### Virtual Environment Activation Issues
- Ensure you are using the correct command for your shell. For PowerShell, use:
  ```sh
  .\venv\Scripts\Activate.ps1
  ```

### Missing Dependencies
- If you encounter missing module errors, ensure all dependencies are installed:
  ```sh
  pip install -r requirements.txt
  ```

### Database Connection Errors
- Ensure your PostgreSQL service is running and the credentials in the `.env` file are correct. If migrations fail, try running:
  ```sh
  python manage.py makemigrations
  python manage.py migrate
  ```

### Merge Conflicts
- If you encounter syntax errors due to merge conflicts, manually resolve conflicts by editing the affected files and removing conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

### Firewall/Antivirus Issues
- Ensure your firewall or antivirus software is not blocking PostgreSQL or the Django development server.

## Conclusion

By following this guide, you should be able to set up and run the Tipsom Web project on your local machine. If you encounter any issues, refer to the Django and PostgreSQL documentation or contact the project maintainers for assistance.

---
