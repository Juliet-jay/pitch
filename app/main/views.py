from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .forms import UpdateProfile,PostAPitch,PostAComment
from .. import db,photos
from ..models import User,Pitch,Comment

@main.route('/')
def landingpage():

    return render_template('index.html')

@main.route('/timeline',methods=['GET','POST'])
@login_required
def timeline():
    form = PostAPitch()
    if form.validate_on_submit():
        new_pitch = Pitch(upvotes=0,downvotes=0,title=form.title.data,content=form.content.data,user_id=current_user.id)
        new_pitch.save_pitch()
        return redirect(url_for('main.timeline'))
    pitches= Pitch.get_pitches()
    users = User.query.all()

    return render_template('timeline.html',form=form,pitches=pitches,users=users)
 
@main.route('/user/profile/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    pitches = Pitch.query.order_by(Pitch.posted.desc()).all()
    
    return render_template('profile.html', user = user, pitches=pitches)

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

    return render_template('profile.html',form=form,user =user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.update_profile',uname=uname))

@main.route('/pitch/new', methods=['GET', 'POST'])
@login_required
def new_pitch():
    pitch_form = PostAPitch()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.text.data

        # Updated pitch instance
        new_pitch = Pitch(pitch_title=title, pitch_content=pitch, user=current_user)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('pitch.html', title=title)


  

