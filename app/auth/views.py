from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

# local imports
from app.auth import auth
from app.auth.forms import LoginForm, RegistrationForm
from app import db
from app.models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
        Handle requests to the /register route
        Add an employee to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    phone_number=form.phone_number.data,
                    category=form.category.data,
                    description=form.description.data,
                    password=form.password.data)

        # add user to the database
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered!, You may now login.')

        # redirect to login page
        return redirect(url_for('auth.login'))

    # render registration template
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """ Handle requests to the /login route and Log a user in through the login form """

    form = LoginForm()
    if form.validate_on_submit():
        # check whether user exists in the database and whether
        # the password entered matches the password in the database

        user = User.query.filter_by(email=form.email.data).first()

        if user and user.verify_password(form.password.data):

            # log the user in
            login_user(user)

            # redirect to appropriate dashboard page
            if user.is_admin:
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))  # add redirection to index page later

        else:
            flash('Invalid Email/Password combination')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """ Handle requests to the /logout route and Logout a user through the logout link """

    logout_user()
    flash('You have successfully been logged out!')

    # redirect to the login page
    return redirect(url_for('auth.login'))  # add redirect to the index page later
