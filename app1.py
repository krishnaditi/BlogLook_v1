from os import path
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, url_for, request, redirect
from models import db, User, Profile, Post, Follow, Comment
from werkzeug.security import generate_password_hash, check_password_hash
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg'}
app = Flask(__name__)

cd= path.abspath(path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+path.join(cd,"project_database.sqlite3")

db.init_app(app)

@app.before_first_request
def create_db():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        check = User.query.filter_by(user_name = username).first()
        if check:
            if check_password_hash(check.password, password):
                fn = check.user_name
                return redirect('/userfeed/{new}'.format(new=fn))
            else:
                return render_template('error3.html')    
        else:
            return render_template('error1.html')
    return render_template('login.html')  

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form.get('name')
        user = request.form.get('username')
        email = request.form.get('email-id')
        password = request.form.get('password')
        check = User.query.filter_by(email = email).first()
        un_check = User.query.filter_by(user_name = user).first()
        if check:
            return render_template('error2.html') 
        elif un_check:
            return render_template('error4.html')    
        else:
            u = User(full_name = name, user_name = user, email = email, password = generate_password_hash(password, method = "sha256"))     
            p = Profile(user_id = user, profile_pic = "no-profile.jpg", total_post = 0)
            db.session.add(p)
            db.session.add(u)
            db.session.commit()
            return render_template('registered.html')
    return render_template('signup.html') 


@app.route('/userfeed/<string:id>')
def userfeed(id):
    u = User.query.filter_by(user_name = id).first()
    p = Profile.query.filter_by(user_id = id).first()
    fr = Follow.query.filter_by(profile_id = p.profile_id).count()
    fl = Follow.query.filter_by(user_id = id).count()

    following = Follow.query.filter_by(user_id=id).all()
    following_pids=[]
    for i in following:
        x = Profile.query.filter_by(profile_id=i.profile_id).first()
        following_pids.append(x.user_id)
    userfeed_posts=[]
    for i in following_pids:
        pst = Post.query.filter_by(user_id=i).all()
        for j in pst:
            post_dict={'post_id': j.post_id, 'user': j.user_id, 'image':j.image, 'heading':j.heading, 'description':j.description, 'timestamp':j.timestamp}
            userfeed_posts.append(post_dict)
    return render_template('user-feed.html', user_id = id, followers = fr, posts = userfeed_posts,
    following = fl, post_count = p.total_post, dp = p.profile_pic, fullname = u.full_name)

@app.route('/profile/<string:id>')
def profile(id):
    u = User.query.filter_by(user_name = id).first()
    p = Profile.query.filter_by(user_id = id).first()
    fr = Follow.query.filter_by(profile_id = p.profile_id).count()
    fl = Follow.query.filter_by(user_id = id).count()
    post = Post.query.filter_by(user_id = id).all()
    posts=[]
    for p_ in post:
        posts_dict={'post_id': p_.post_id, 'image':p_.image, 'heading': p_.heading, 'description': p_.description, 'timestamp': p_.timestamp}
        posts.append(posts_dict)
    return render_template('profile.html', user_id = id, followers = fr, 
    following = fl, post_count = p.total_post, about = p.about,dp = p.profile_pic, 
    fullname = u.full_name, posts = posts)

@app.route('/user/<string:pid>/profile/<string:id>')
def user_profile(pid, id):
    u = User.query.filter_by(user_name = id).first()
    p = Profile.query.filter_by(user_id = id).first()
    fr = Follow.query.filter_by(profile_id = p.profile_id).count()
    fl = Follow.query.filter_by(user_id = id).count()
    user_profile=User.query.filter_by(user_name=pid).first()
    up = Profile.query.filter_by(user_id=pid).first()
    fr_u = Follow.query.filter_by(profile_id = up.profile_id).count()
    fg_u = Follow.query.filter_by(user_id = pid).count()
    user_posts=Post.query.filter_by(user_id=pid).all()
    return render_template('user_profile.html', user_id = id, followers = fr, 
    following = fl, post_count = p.total_post, about = p.about,dp = p.profile_pic, 
    fullname = u.full_name, uprof = user_profile, uprof_ = up,
    frs=fr_u, fgs=fg_u, uposts=user_posts)


@app.route('/followers/<string:id>')
def followers(id):
    u = User.query.filter_by(user_name = id).first()
    p = Profile.query.filter_by(user_id = id).first()
    fr = Follow.query.filter_by(profile_id = p.profile_id).count()
    fl = Follow.query.filter_by(user_id = id).count()
    f = Follow.query.filter_by(profile_id = p.profile_id).all()
    return render_template('followers.html', user_id = id, followers = fr, f = f,
    following = fl, post_count = p.total_post, about = p.about,dp = p.profile_pic, fullname = u.full_name) 

@app.route('/following/<string:id>')
def following(id):
    u = User.query.filter_by(user_name = id).first()
    p = Profile.query.filter_by(user_id = id).first()
    fr = Follow.query.filter_by(profile_id = p.profile_id).count()
    fl = Follow.query.filter_by(user_id = id).count()
    f = Follow.query.filter_by(user_id = id).all()
    l = []
    for i in f:
        ck = Profile.query.filter_by(profile_id = i.profile_id).first()
        l.append((ck.user_id, p.profile_id))
    return render_template('following.html', f = l,ff = p.profile_id, user_id = id, followers = fr, 
    following = fl, post_count = p.total_post, about = p.about,dp = p.profile_pic, fullname = u.full_name) 

@app.route('/f/follow/<int:pid>/<string:id>')
def f(pid, id):
    p1 = Profile.query.filter_by(user_id = id).first()
    p2 = Profile.query.filter_by(profile_id = pid).first()
    
    chk = Follow.query.filter_by(user_id=p2.user_id).filter_by(profile_id=p1.profile_id).first()
    if(chk):
       pass
    else: 
        n_e = Follow(user_id=p2.user_id, profile_id=p1.profile_id)
        db.session.add(n_e) 
        db.session.commit()
    return redirect("/profile/{a}".format(a = p2.user_id))

@app.route('/following/unfollow/<int:pid>/<string:user_id>')
def unf(pid, user_id):
    p1 = Profile.query.filter_by(user_id = user_id).first()
    p2 = Profile.query.filter_by(profile_id = pid).first()

    chk = Follow.query.filter_by(user_id = p2.user_id).filter_by(profile_id = p1.profile_id).first()
    if(chk):
        Follow.query.filter_by(user_id = p2.user_id).filter_by(profile_id = p1.profile_id).delete()
        db.session.commit()
    else: 
        pass
    return redirect("/profile/{a}".format(a = p2.user_id))


@app.route('/follower/unfollow/<int:pid>/<string:user_id>')
def fun(pid, user_id):
    p2 = Profile.query.filter_by(profile_id = pid).first()

    chk = Follow.query.filter_by(user_id = user_id).filter_by(profile_id = pid).first()
    if(chk):
        Follow.query.filter_by(user_id = user_id).filter_by(profile_id = pid).delete()
        db.session.commit()
    else: 
        pass
    return redirect("/profile/{a}".format(a = p2.user_id))    

@app.route('/comments/<string:id>/<int:cid>', methods = ['GET', 'POST'])
def comments(id, cid):
    u = User.query.filter_by(user_name = id).first()
    p = Profile.query.filter_by(user_id = id).first()
    fr = Follow.query.filter_by(profile_id = p.profile_id).count()
    fl = Follow.query.filter_by(user_id = id).count()
    if request.method == 'POST':
        c = request.form.get("r")
        if(c!=''):
            n_c = Comment(post_id = cid, comment = c)
            db.session.add(n_c)
            db.session.commit()
        co = Comment.query.filter_by(post_id = cid).all()
        return redirect('/comments/{i}/{p}'.format(i = id, p = cid))
    co = Comment.query.filter_by(post_id = cid).all()
    return render_template('comments.html',comments = co, user_id = id, followers = fr, 
    following = fl, post_count = p.total_post, about = p.about,dp = p.profile_pic, fullname = u.full_name)

@app.route('/Add_Blogs/<string:id>', methods = ['GET', 'POST'])
def Add_Blogs(id):
    u = User.query.filter_by(user_name = id).first()
    p = Profile.query.filter_by(user_id = id).first()
    fr = Follow.query.filter_by(profile_id = p.profile_id).count()
    fl = Follow.query.filter_by(user_id = id).count()
    if request.method == 'POST':
        wrkng_dir = os.path.abspath(os.path.dirname(__file__))
        path=os.path.join(wrkng_dir, "static/POST/")
        heading = request.form.get('heading')
        description = request.form.get('description')
        img = request.files['blog_image']
        dt = Post.query.get("timestamp")
        imgname = ""
        if img:
            imgname = "{user}{im}.jpeg".format(im = p.total_post, user = id)
            img.save(os.path.join(path, imgname))
        tp = p.total_post + 1
        Profile.query.filter_by(user_id = id).update(dict(total_post = tp))
        db.session.commit()
        post = Post(user_id = id, image = imgname, heading = heading, description = description,
        timestamp = dt)
        db.session.add(post)
        db.session.commit()
        return redirect("/profile/{a}".format(a = id))
    return render_template('Add_Blogs.html', user_id = id, followers = fr, 
    following = fl, post_count = p.total_post, dp = p.profile_pic, fullname = u.full_name) 

@app.route('/editprofile/<string:id>', methods = ['GET', 'POST'])
def editprofile(id):
    u = User.query.filter_by(user_name = id).first()
    p = Profile.query.filter_by(user_id = id).first()
    fr = Follow.query.filter_by(profile_id = p.profile_id).count()
    fl = Follow.query.filter_by(user_id = id).count()
    wrkng_dir = os.path.abspath(os.path.dirname(__file__))
    path=os.path.join(wrkng_dir, "static/PROFILE")    
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        about = request.form.get('about')
        dp = request.files['image']
        if dp:
            dpname = secure_filename(dp.filename)
            dpname = "{us}.jpeg".format(us = id)
            dp.save(os.path.join(path, dpname))
            User.query.filter_by(user_name = id).update(dict(full_name = fullname))
            Profile.query.filter_by(user_id = id).update(dict(about = about, profile_pic = dpname))
            db.session.commit() 
            return redirect("/profile/{a}".format(a = id))
    return render_template('edit_profile.html', user_id = id, followers = fr, 
    following = fl, post_count = p.total_post, fullname = u.full_name, about = p.about, dp = p.profile_pic)        


@app.route('/engagement/<string:id>', methods = ['GET', 'POST'])
def engagement(id):
    wrkng_dir = os.path.abspath(os.path.dirname(__file__))
    path=os.path.join(wrkng_dir, "static/IMG/")
    u = User.query.filter_by(user_name = id).first()
    p = Profile.query.filter_by(user_id = id).first()
    fr = Follow.query.filter_by(profile_id = p.profile_id).count()
    fl = Follow.query.filter_by(user_id = id).count()
    up = u.post
    plt.clf()
    plt.plot([x.heading for x in up], [x.timestamp for x in up], c='r', marker='o')
    plt.ylabel("Time Stamp")
    plt.xlabel("Heading")
    plt.yticks(rotation = 45)
    plt.savefig(path+id+".png")

    return render_template('engagement.html',id = id, user_id = id, followers = fr,
    following = fl, post_count = p.total_post, fullname = u.full_name, about = p.about, dp = p.profile_pic)

@app.route('/editblog/<int:pid>', methods = ['GET', 'POST'])
def editblog(pid):
    q = Post.query.filter_by(post_id = pid).first()
    id = q.user_id
    u = User.query.filter_by(user_name = id).first()
    p = Profile.query.filter_by(user_id = id).first()
    fr = Follow.query.filter_by(profile_id = p.profile_id).count()
    fl = Follow.query.filter_by(user_id = id).count()
    wrkng_dir = os.path.abspath(os.path.dirname(__file__))
    path=os.path.join(wrkng_dir, "static/POST")    
    if request.method == 'POST':
        heading = request.form.get('heading')
        description = request.form.get('description')
        img = request.files['blog_image']
        imname = secure_filename(img.filename)
        imname =  "{user}{im}.jpeg".format(im = pid, user = id)
        img.save(os.path.join(path, imname))
        Post.query.filter_by(post_id = pid).update(dict(heading = heading, description = description, image = imname))
        db.session.commit() 
        return redirect("/profile/{a}".format(a = id))    

    return render_template('edit_blog.html', user_id = id, post_id = pid, followers = fr, 
    dp = p.profile_pic, fullname = u.full_name,
    following = fl, post_count = p.total_post,
    e_heading = q.heading, e_description = q.description, e_image = q.image)       


@app.route('/delete/<string:id>/<int:pid>', methods=['GET', 'POST'])
def delete(id,pid):
    if request.method=='GET':
        return render_template('ok.html', name=id)
    elif request.method=='POST':
        y = request.form.get('delete')
        if (y=='yes'):
            de = Profile.query.filter_by(user_id = id).first()
            tpo = de.total_post - 1
            Profile.query.filter_by(user_id = id).update(dict(total_post = tpo))
            Post.query.filter_by(post_id=pid).delete()
            db.session.commit()
            return redirect("/profile/{a}".format(a = id))
        else:
            return redirect("/profile/{a}".format(a = id))


@app.route('/delete_user/<string:id>', methods=['GET', 'POST'])
def delete_user(id):
    if request.method=='GET':
        return render_template('ok.html', name=id)
    elif request.method=='POST':
        y = request.form.get('delete')
        if (y=='yes'):
            User.query.filter_by(user_name = id).delete()
            Profile.query.filter_by(user_id = id).delete()
            Follow.query.filter_by(user_id = id).delete()
            Post.query.filter_by(user_id = id).delete()
            db.session.commit()
            return redirect("/signup")
        else:
            return redirect("/profile/{a}".format(a = id))

@app.route('/search/<string:id>', methods = ['GET', 'POST'])
def search(id):
    u = User.query.filter_by(user_name = id).first()
    p = Profile.query.filter_by(user_id = id).first()
    fr = Follow.query.filter_by(profile_id = p.profile_id).count()
    fl = Follow.query.filter_by(user_id = id).count()
    if request.method  == 'POST':
        s = request.form.get('q')
        if s:
            element = "%" + s + "%"
            result = Profile.query.filter(Profile.user_id.like(element)).all()
            results=[]
            for i in result:
                if(i.user_id!=id):
                    results.append(i)
            return render_template('search.html', user_id = id, followers = fr, data = results,
            following = fl, post_count = p.total_post, dp = p.profile_pic, fullname = u.full_name)
    return render_template('search.html', user_id = id, followers = fr,
    following = fl, post_count = p.total_post, dp = p.profile_pic, fullname = u.full_name)    
    
@app.route('/follow/<int:pid>/<string:id>')
def followed(pid, id):
    
    chk = Follow.query.filter_by(user_id=id).filter_by(profile_id=pid).first()
    if(chk):
       pass
    else: 
        n_e = Follow(user_id=id, profile_id=pid)
        db.session.add(n_e) 
        db.session.commit()
    return redirect("/search/{a}".format(a = id))

@app.route('/unfollow/<int:pid>/<string:user_id>')
def unfollowed(pid, user_id):
    chk = Follow.query.filter_by(user_id=user_id).first()
    if(chk):
        Follow.query.filter_by(user_id = user_id).delete()
        db.session.commit()
    else: 
        pass
    return redirect("/search/{a}".format(a = user_id))


@app.route('/logout')
def logout():
    return redirect('/login') 


if __name__ == '__main__':
    app.run(debug=True)    
