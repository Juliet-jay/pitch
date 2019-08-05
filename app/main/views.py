from flask import render_template
from . import main
from ..models import User, Pitch, Category, Vote, Comment
from flask_login import login_required, current_user
from .forms import UpdateProfile, PitchForm, CommentForm, CategoryForm
from .. import db, photos

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

   
    category = Category.get_categories()


    return render_template('index.html',  category = category)
