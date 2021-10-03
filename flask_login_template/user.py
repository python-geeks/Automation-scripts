from flask import render_template, flash, redirect, session, request
from forms import registerForm, loginForm
from passlib.hash import sha256_crypt
import setup.config as config
import uuid


class User:
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user

    def register(self):
        reg_form = registerForm(request.form)
        login_form = loginForm(request.form)
        if request.method == "POST":
            if reg_form.submit1.data and reg_form.validate():
                user = {
                    "_id": uuid.uuid4().hex,
                    "name": reg_form.name.data,
                    "email": reg_form.email.data,
                    "username": reg_form.username.data,
                    "password": reg_form.password.data}
                user['password'] = sha256_crypt.encrypt(user['password'])
                if config.db.users.find_one({"email": user['email']}):
                    error = "Email already exists!"
                    return render_template(
                        config.template,
                        error=error,
                        reg_form=reg_form,
                        login_form=login_form)
                if config.db.users.insert_one(user):
                    self.start_session(user)
                    flash('You are now registered and can log in!', 'success')
                    return render_template(
                        config.template,
                        reg_form=reg_form,
                        login_form=login_form)
            elif login_form.submit2.data and login_form.validate():
                user = config.db.users.find_one(
                    {"username": login_form.username.data})
                if user:
                    if sha256_crypt.verify(
                            login_form.password.data, user['password']):
                        self.start_session(user)
                        return render_template('dashboard.html')
                    else:
                        error = 'Incorrect login details!'
                        return render_template(
                            config.template,
                            error=error,
                            reg_form=reg_form,
                            login_form=login_form)
                else:
                    error = 'Username not found!'
                    return render_template(
                        config.template,
                        error=error,
                        reg_form=reg_form,
                        login_form=login_form)
            error = 'Check the registered details!'
            return render_template(
                config.template,
                error=error,
                reg_form=reg_form,
                login_form=login_form)
        else:
            try:
                return render_template(
                    config.template,
                    reg_form=reg_form,
                    login_form=login_form)
            except Exception:
                return "Given template does not exists."

    def logout(self):
        session.clear()
        flash("You are now logged out!", "success")
        return redirect('/')
