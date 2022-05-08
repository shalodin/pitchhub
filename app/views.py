# from flask import render_template,redirect, url_for
# # from app import app
# from . import main
# from wtforms import form
# from main.forms import PitchesForm
# from models import Pitch,User


# #views
# @main.route('/')
# def index():
#     '''
#     View root page function that returns the index page and its data
#     '''
#     title='Pitches Thrills'
#     return render_template('index.html',title=title)


# @main.route('/pitch/newpitch', methods=['POST', 'GET'])

# def new_pitch():
#     form = PitchesForm()
#     if form.validate_on_submit():
#         title = form.pitch_title.data
#         category = form.pitch_category.data
#         newPitch = form.pitch_comment.data

#         #update pitch instance
#         new_pitch = Pitch(title=title,
#                           category=category,
#                           comment=newPitch)
                          

#         #save pitch
#         new_pitch.save_pitch()
#         return redirect(url_for('.index'))

#     title = 'Add New pitch'
#     return render_template('pitches.html', title=title, pitchesform=form)



# @main.route('/category/sports')
# def sports():
#     '''
#     view function to display sports pitches
#     '''
#     sports_title ='sports Pitches'
#     return render_template('pitches/sports.html',title=sports_title)

# @main.route('/category/business')
# def business():
#     '''
#     view function to display business pitches
#     '''
#     business_title='Business Pitches'
#     return render_template('pitches/business.html',title=business_title)


# @main.route('/category/interview')
# def interview():
#     '''
#     view function to display interview pitches
#     '''
#     interview_title ='Interview Pitches'
#     return render_template('pitches/interview.html',title=interview_title)

# @main.route('/category/love')
# def love():
#     '''
#     view function to display love pitches
#     '''
#     love_title='Love Pitches'
#     return render_template('pitches/love.html',title=love_title)


# @main.route('/category/study')
# def study():
#     '''
#     view function to display study pitches
#     '''
#     study_title='Study Pitches'
#     return render_template('pitches/study.html',title=study_title)


# @main.route('/category/politics')
# def politics():
#     '''
#     view function to display business pitches
#     '''
#     politics_title = 'Politics Pitches'
#     return render_template('pitches/politics.html',title=politics_title)