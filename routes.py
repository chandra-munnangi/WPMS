from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import LoginForm, WorkorderForm, ConsigneeForm, ItemForm
from app.models import User, Workorder, Consignee, Item
from flask_login import current_user, login_user, logout_user, login_required
from app.job_number_generator import generate_job_number

@app.route('/')
@app.route('/dashboard')
@login_required
def dashboard():
    # Filter options will be implemented here based on user selections
    workorders = Workorder.query.all()
    return render_template('dashboard.html', workorders=workorders)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_id=form.user_id.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/workorder/new', methods=['GET', 'POST'])
@login_required
def new_workorder():
    form = WorkorderForm()
    if form.validate_on_submit():
        job_number = generate_job_number(form.consignee.data, form.item_name.data)
        workorder = Workorder(
            workorder_no=form.workorder_no.data,
            workorder_date=form.workorder_date.data,
            item_name=form.item_name.data,
            consignee=form.consignee.data,
            allocation_no=form.allocation_no.data,
            quantity=form.quantity.data,
            job_number=job_number
        )
        db.session.add(workorder)
        db.session.commit()
        flash('Workorder created successfully!')
        return redirect(url_for('dashboard'))
    return render_template('workorder_form.html', form=form)

# Add more routes for managing consignees, items, and users