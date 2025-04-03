# Local Setup
- Run ```pip install -r requirements.txt``` to install all dependencies required to run the app mentioned in ```requirements.txt``` which is inside ```docs``` folder

# Local Developments Run
- ```python3 app.py``` will start the flask application in ```development```. This is for running app on local system.

# Replit Run
- Add the ```requirements.txt``` in ```poetry```
- Go to the shell and run ```pip install --upgrade poetry```
- Select and open the ```main.py``` python file and click the Run button.
- The web app will be available at 
- Format will be sort of https://..repl.co

# Folder Structure
- ```project_database.sqlite3``` is the sqlite database. It can be anywhere on the machine just the adjustment in path in ```app.py``` is required. One of the database is shipped for testing purpose.
- The application code for my app is ```/```
- ```static``` a folder in which we have the images and css files used in the app.
- ```templates``` is the default folder where templates are stored

```
BLOG-LITE/
├── app.py
├── models.py
├── project_database.sqlite3
├── readme.md
├── Project Documentation.pdf
├── docs
|   └── requirements.txt
├── static/
|       ├── POST 
|       ├── PROFILE
        ├── IMG
        ├── ab.jpg
        ├── base.css
        ├── login.css
        ├── signup.css
        ├── home.css
        ├── error.jpg
        ├── h1.jpg
        ├── home.jpg
        ├── logo.jpg
        ├── p_background.jpg
|       └── registered.jpg
|
└── templates/
       ├── Add_Blogs.html
       ├── base.html
       ├── comments.html
       ├── edit_blog.html
       ├── edit_profile.html
       ├── error1.html
       ├── error2.html
       ├── error3.html
       ├── error4.html
       ├── error5.html
       ├── followers.html
       ├── following.html
       ├── home.html
       ├── list.html
       ├── login.html
       ├── ok.html
       ├── original.html
       ├── profile.html
       ├── registered.html
       ├── search.html
       ├── signup.html
       ├── user_profile.html
       └── user-feed.html
```