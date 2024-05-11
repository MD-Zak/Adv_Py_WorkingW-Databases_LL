from flask import Flask, render_template, flash, redirect, url_for, request # render_template mod renders html files
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://postgres:sqltopostgre@localhost/pt'
app.config["SECRET_KEY"] = b'\xc0\xbe\x03\xad\x91\xf0\xbe\xae4\xcf\x04?\xc4\xa1\x8c=\xca\xa4V\x1c\xbdiJ@'
db = SQLAlchemy(app) # creates a database obj. after the config of sqlal and flask.

class Project(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(length = 25))

    cux_of_proj = db.relationship('Task', back_populates = 'cux_of_task', cascade = "all, delete-orphan")

class Task(db.Model):
    __tablename__ = 'tasks'
    task_id = db.Column(db.Integer, primary_key = True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    description = db.Column(db.String(length = 25))

    cux_of_task = db.relationship('Project', back_populates = 'cux_of_proj')

#Define a home route
@app.route("/")

#Display
def show_project():
    return render_template("projects_home.html", to_projects_html = Project.query.all()) # The flask-sqlalchemy ext. makes Project model possible,
    # along with db.Model we are able to query.all(), an iterable from the database through the database models.
    # And finally, render_template is used here to passed the iterable data from database to the html page so as to render them.

@app.route("/projects/<project_id>") # project_id from homepage projects_home.html
def show_tasks(project_id):
    return render_template("tasks_page.html", tasks_page_proj = Project.query.filter_by(project_id = project_id).first(), # there should only be one proj with this id, so we will use first() to grab the first one.
    to_tasks_page = Task.query.filter_by(project_id = project_id).all())

#Adding

@app.route("/add/projects", methods = ['POST'])
def add_project():
    if not request.form["project-title"]:
        flash("Enter a project title.", "Red")
    else:
        db.session.add(Project(title = request.form["project-title"]))
        db.session.commit()
        flash("Project added successfully", "Green")
    return redirect(url_for('show_project'))

@app.route("/add/tasks/<project_id>", methods = ['POST']) # only project_id would work. as this path is according to the columns in the database.
def add_tasks(project_id):
    if not request.form["Task-name"]: # the request form is case sensitive.
        flash("Enter a task associated with the project.", "blue")
    else:
        db.session.add(Task(description = request.form["Task-name"], project_id = project_id))
        db.session.commit()
        flash("Task added successfully", "Green")
    return redirect(url_for('show_tasks',project_id = project_id)) # we pass project_id from the path to the func. show_tasks.

#Deletion

# @app.route("/removes_tasks/<task_id>", methods = ['POST'])
# def removes_tasks(task_id):

#     # pending_task_delete = Task.query.filter_by(task_id = task_id).first()
#     # original_project_id = pending_task_delete.cux_of_task.project_id
#     # db.session.delete(pending_task_delete)
#     # db.session.commit()
#     # flash("Task deleted successfully", "Red")

#     return redirect(url_for('show_tasks', project_id = original_project_id))

@app.route("/removes_projects/<project_id>", methods = ["POST"])
def removes_proj(project_id):

    pending_proj_delete = Project.query.filter_by(project_id = project_id).first()
    db.session.delete(pending_proj_delete)
    # db.session.commit()
    flash("Project removed successfully.", "red")
    return redirect(url_for('show_project'))

#Alter

@app.route("/completes_tasks/<descrip>", methods = ["POST"])
def progress_update(descrip : str):

    # update_stmt = update(Task).where(Task.description == in_description).values(description = in_description + " - Done")
    # session.execute(update_stmt)
    # session.commit()
    print(descrip)
    print(type(descrip))
    pending_update = Task.query.filter_by(project_id = 2).first()
    original_project_id = pending_update.cux_of_task.project_id
    # db.session.update(Task(description = descrip + " - Done."))
    # # db.session.update(pending_update)
    # db.session.commit()
#     #retrieve the old value.
#     old_descrp = db.session.select(Task.query.filter_by(description = description))
#     new_descrp = old_descrp + '-completed'
#     pending_update = Task(description = new_descrp)
#     db.session.update(pending_update)

# db.session.add(Task(description = task.description + '-completed', project_id = project_id))

    flash("Alteration complete...\n", "green")
    return redirect(url_for('show_tasks', project_id = original_project_id))


app.run(debug = True, host = "127.0.0.1", port = 3000)


