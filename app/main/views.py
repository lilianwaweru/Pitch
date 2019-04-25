from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos
from flask_login import login_required

@main.route('/')
def index():
    # pickup = Pitch.get_pitch('pickup')
    # interview = Pitch.get_pitch('interview')
    # product = Pitch.get_pitch('product')
    # promotion = Pitch.get_pitch('promotion')

    return render_template('index.html')


@main.route('/pitch/interview')
def interview():
    pitch = Pitch.get_pitch('interview')

    return render_template('interview.html',pitch = pitch)

@main.route('/pitch/pickup')
@login_required
def pickup():
    pitch_form = PitchForm()

    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        category = pitch_form.category.data

        new_pitch = Pitch(pitch_content=pitch,pitch_category = category,user = current_user)
        new_pitch.save_pitch()

    all_pitches = Pitch.get_all_pitches()

    return render_template('pickup.html',pitch_form = pitch_form, pitches = all_pitches)

@main.route('/pitch/promotion')
def promotion():
    pitch = Pitch.get_pitch('promotion')
    return render_template('promotion',pitch = pitch)




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

@main.route('/Pitch', methods = ['GET', 'POST'])
@login_required
def pitches():
    pitch_form = PitchForm()
    
    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        cat = pitch_form.category.data

        new_pitch = Pitch(content=pitch, category = cat)
        new_pitch.save_pitch()

        return redirect(url_for('main.pitches'))

    all_pitches = Pitch.get_all_pitches()
    
    return render_template('new_pitch.html', pitch_form = pitch_form, pitches = all_pitches)


@main.route('/comments/<int:id>',methods = ['GET','POST'])
@login_required
def comment(id):
    
    my_pitch = Pitch.query.get(id)
    comment_form = CommentForm()

    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comment(comment = comment_data, pitch_id = id)
        new_comment.save_comment()

        return redirect(url_for('main.comment',id=id))

    all_comments = Comment.get_comment(id)


    return render_template('comments.html',pitch = my_pitch, comment_form = comment_form, comments = all_comments)