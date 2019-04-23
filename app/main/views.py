from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from .forms import UpdateProfile
from .. import db,photos
from flask_login import login_required



@main.route("/")
def index():
    title="Home"
    return render_template("index.html",title=title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html",user = user)
    

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data

        new_pitch = Pitch(id=id,title=title,content=content,category=category,posted=posted,upvote=upvote,downvote=downvote,comment=comment)
        new_pitch.save_pitch()
        return redirect(url_for('index.html'))
    title = 'New Pitch'
    return render_template('new_pitch.html',title=title,pitch_form=form)


