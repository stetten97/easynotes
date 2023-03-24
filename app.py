from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create the application
app = Flask(__name__)
app.config["SQLAlCHEMY_DATABASE_URI"] = "sqlite://easynotes.db"

db = SQLAlchemy(app)

# create Item Object
class ToDoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=True)
    date_created = db.Column(db.Datetime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form["content"]
        new_task = ToDoList(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            "issue adding new task!"
    else:
        tasks = ToDoList.query.order_by(ToDoList.date_created).all()
        return render_template("index.html", tasks=tasks)
