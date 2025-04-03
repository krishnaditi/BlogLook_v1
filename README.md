# <img src="https://img.icons8.com/ios-filled/50/000000/blog.png" width="25"/> BlogLook_V1 Application
 
_A Social Platform for Blog Management using Flask, SQLAlchemy, HTML, CSS & Bootstrap_  

![Python](https://img.shields.io/badge/Python-3.8-blue)  ![Flask](https://img.shields.io/badge/Flask-2.0-blue)  ![Vue.js](https://img.shields.io/badge/Vue.js-3.0-42b883?logo=vue.js)  ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4-green)  ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-purple?logo=bootstrap)  
 ![HTML(https://img.shields.io/badge/HTML-5-orange?logo=html5)  ![CSS](https://img.shields.io/badge/CSS-3-blue?logo=css3)  


## 📌 About The Project  
The BlogLook Application is a web platform that allows users to socially connect with other users and then can manage their blogs. 

### 🔹 Key Features  
✔️ Social Application  
✔️ Blog Management Workflow  
✔️ Following & Follower System    

## 🛠️ Tech Stack  
- **Backend:** Flask, SQLAlchemy  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite    

## ⚙️ Installation  
1. Clone the repository  
   ```sh
   git clone https://github.com/krishnaditi/BlogLook_v1.git

2. python -m venv venv
   - On **Ubuntu / MacOS**:  
     source venv/bin/activate
   - On **Windows**:  
     venv\Scripts\activate
  
4. pip install -r requirements.txt

5. flask run


## 📂 Folder Structure  


```plaintext
/BlogLook_v1
│-- backend
│   ├── application        # Backend folder
│   │   ├── static         # Images and CSV files
│   │   ├── templates      # HTML pages for triggered jobs
│   │   ├── api.py         # Flask APIs
│   │   ├── cache.py       # Cache initialization
│   │   ├── clry.py        # Celery initialization
│   │   ├── emailgen.py    # SMTP initialization
│   │   ├── models.py      # Database tables
│   │   ├── tasks.py       # Jobs triggered
|   |
│   ├── 21f1004270-Project Documentation.pdf  # Project Report
│   ├── app.py            # Configuration and API endpoints
│   ├── requirements.txt   # Libraries used
│
│-- frontend
│   ├── src
│   │   ├── assets         # Images
│   │   ├── components     # Vue components
│   │   │   ├── Add_Blogs.vue
│   │   │   ├── DeleteBlog.vue
│   │   │   ├── DeleteUser.vue
│   │   │   ├── EngageMent.vue
│   │   │   ├── FollowersPg.vue
│   │   │   ├── FollowingPg.vue
│   │   │   ├── HomePage.vue
│   │   │   ├── LoginPage.vue
│   │   │   ├── MyProfile.vue
│   │   │   ├── OtherProfile.vue
│   │   │   ├── ...
│   │   ├── router
│   │   ├── store
│   │   ├── views
│   │   │   ├── App.vue
│   │   │   ├── main.js
│
│-- README.md
│-- openapi.yaml

```


## 👤 Author  
**Aditi Krishana**  
🔗 [GitHub](https://github.com/krishnaditi) | [LinkedIn](https://linkedin.com/in/aditi-krishana)  
📧 Email: krishanaaditi@gmail.com  

## 🎉 Acknowledgments  
Thanks to [Bootstrap](https://getbootstrap.com/) & [Flask](https://flask.palletsprojects.com/) for making this project possible.

