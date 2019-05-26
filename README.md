## IP-REVIEW

This project enables user to sign up/log in to the website,then they can view,comment and rate other people's posts.Their own posts can also be viewed,commented on and rated by other users.The user can create a profile and update it at any point in time.

## SETUP INSTRUCTIONS:
### Prerequisites
1. python3.6
2. venv (virtual environment wrapper)
3. PostgresQl

### Instructions
1.Clone the repository and checkout into the project folder.
```bash
git clone `https://github.com/lydiah2015/IP-review.git`
```
```bash
cd IP-REVIEW
```
2.Create and activate your virtual environment
```bash
python3.6 -m venv virtual
```
```bash
source virtual/bin/activate
```
3. Run `pip install -r requirements.txt` to install all the dependencies of the application
4. Create a `.env` file at the root of your project and Set it up to contain the following:
```
SECRET_KEY='a good secret key'
DEBUG=True
DB_NAME='review'
DB_USER='your_postgres_username'
DB_PASSWORD='your_postgres_password'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```
5. Run `python3.6 manage.py migrate` to migrate your database schema and create a local database instance.
6. Use the command `python3.6 manage.py runserver` to open the project on your browser.



## User Stories
| GENERAL BEHAVIOUR | INPUT | OUTPUT|
|:------------------|:--------|:-----------|
|User wants to search for a profile | They enter the profile name or on the search bar |all relevant profiles are displayed|
|User wants to view the project |They click on the image |projects are displayed|
|User wants to upload an image| They navigate to the admin route and upload the image along with its caption,tag.|Image is uploaded|

## Tecnologies used
```
python3.6
HTML5
venv
django 1.11
```

## Bug reports
To report any bug, create an issue mentioning what the bug is and how to replicate it.

## Contributing
To contribute to the projct, check the issues tab to work on a feature or bug
Fork the repo then create a pull request once done.

## CONTACT INFORMATION
For more information or clarification reach me through my email address : mitchellemakini15@gmail.com

## Licence
copyright (c) Mitchelle Makini 2019
MIT
