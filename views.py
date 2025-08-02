from flask import Blueprint, render_template, request, redirect, url_for
from flask import flash
from models import Task, db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

@views.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        task = request.form['task']
        new_task = Task(task=task)
        db.session.add(new_task)
        db.session.commit()
        flash('New task created successfully!', 'success') 
        return redirect(url_for('views.home'))
    return redirect(url_for('views.home'))

@views.route('/edit/<int:task_id>', methods=['POST', 'GET'])
def edit(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        new_task = request.form['task']
        status = request.form.get('status') == 'on'

        if new_task:
            task.task = new_task
            task.status = status
            db.session.commit()
            flash(f'#{task_id} Task Updated Successfully!', 'success')
            return redirect(url_for('views.home'))
    return render_template('edit.html', task=task)

@views.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        db.session.delete(task)
        db.session.commit()
        flash(f'#{task_id} Deleted Successfully!', 'wrong')
        return redirect(url_for('views.home'))
    return redirect(url_for('views.home'))