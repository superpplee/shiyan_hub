# -*- coding:utf-8 -*-

from flask import render_template,flash,redirect

from forms import LoginForm

from app import app



def index():

	user = {'nickname':'Miguel'}

	posts = [
	{
	'author':{'nickname':'John'},
	
	'body':'Beautiful day in Portland!'},

	{
	'author':{'nickname': 'Susan'},
	 'body':'The Avengers movie was so cool!'}
	]	

	return render_template("index.html",title = 'Home',user = user,posts = posts)

@app.route('/login',methods = ['GEt','POST'])


def login():
	form = LoginForm()	
	
	if form.validate_on_submit():

		flash('Login requested for Name: + form.name.data')

		flash('password:' + str(form.password.data))

		flask('remember_me:' + str(form.remember_me.data))

		return redirect('/index')
	
	return render_template('login.html',title = 'Sign In',form=form)
