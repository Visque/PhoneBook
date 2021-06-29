# PhoneBook App

    This phonebook application is made using django.

    Features include: -
    1. User registration
    2. User signin
    3. User Creating contacts
    4. User acessing the Public Database (Includes contacts made by all users)

## MANUAL

    1. Create a folder and put all the files in it.
    2. Create a virtual env `virtualenv env`.
    3. work on the virtual env by `source env/bin/activate`.
    4. Install the virtual env requirments by `pip install -r requirements.txt`.
    5. Always make migrations by `python manage.py makemigrations`.
    6. Migrate using `python manage.py migrate`.
    7. Run the app by `python manage.py runserver`.

    ```
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    June 29, 2021 - 15:52:47
    Django version 3.2.4, using settings 'Phonebook.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
    8. Open the link `http://127.0.0.1:8000/`.