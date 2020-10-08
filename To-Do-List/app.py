from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'any random secret'
db = SQLAlchemy(app)


class TODO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def hello():
    db.create_all()
    if request.method == 'POST':
        task = request.form['content']
        new_task = TODO(content=task)
        try:
            db.session.add(new_task)
            db.session.commit()
            flash('Successfully added!')
            return redirect('/')
        except Exception:
            flash('An error occurred')
            return redirect('/')
    else:
        tasks = TODO.query.order_by(TODO.date_created).all()
        return render_template("toDoListTemplate.html", tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task = TODO.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        flash('Successfully deleted')
        return redirect('/')
    except Exception:
        flash('An error occurred')
        return redirect('/')


@app.route('/modify/<int:id>', methods=['POST', 'GET'])
def modify(id):
    task = TODO.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            flash("Successfully updated")
            return redirect('/')
        except Exception:
            flash("An error occurred")
            return redirect('/')
    else:
        return render_template("toDoListTemplate.html", tasks=task)


if __name__ == '__main__':
    app.run(debug=True)
