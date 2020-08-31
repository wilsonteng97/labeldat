from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Organisation(db.Model):
    org_id = db.Column(db.Integer, primary_key=True, nullable=False)

    name = db.Column(db.String(80), nullable=False)
    is_enterprise = db.Column(db.Boolean, nullable=False)

    project = db.relationship('Project', backref='organisation', lazy=True, nullable=True) # parent 1-to-many w Project
    user = db.relationship('User', backref='organisation', lazy=True) # parent 1-to-many w User

    def __repr__(self):
        return f"<Organisation {self.org_id} | {self.name} | Enterprise : {self.is_enterprise}>"

class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True, nullable=False)
    org_id = db.Column(db.Integer, db.ForeignKey('organisation.org_id'), primary_key=True, nullable=False) # child 1-to-many w Organisation
    # org_id = db.Column(db.Integer, primary_key=True, nullable=False) # FK w org_id

    project_name = db.Column(db.String(80), nullable=False)
    layout = db.Column(db.String, nullable=False)
    data_type = db.Column(db.String(80), nullable=False)
    outsource_labelling = db.Column(db.Boolean, nullable=False)

    task = db.relationship('Task', backref='task', lazy=True, nullable=True) # parent 1-to-many w Task
    project_manager = db.relationship('ProjectManager', backref='project_manager', lazy=False) # parent 1-to-many w ProjectManager

    def __repr__(self):
        return f"<Project {self.project_id} | {self.project_name} | Organisation : {self.org_id}>"

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    org_id = db.Column(db.Integer, db.ForeignKey('organisation.org_id'), primary_key=True, nullable=False) # child 1-to-many w Organisation
    # org_id = db.Column(db.Integer, primary_key=True) # FK w org_id

    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(256), nullable=False) # SHA256 Encryption (?)
    name = db.Column(db.String(120), nullable=False)

    project_manager = db.relationship('ProjectManager', uselist=False, backref='user') # parent 1-to-1 w ProjectManager 
    label =  db.relationship('Label', backref='user', lazy=True, nullable=True) # parent 1-to-many w label

    def __repr__(self):
        return f"<User {self.user_id} | {self.username} ({self.name}) | Organisation : {self.org_id}>"

class ProjectManager(db.Model):
    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'), primary_key=True, nullable=False) # Child 1-to-many w Project
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True, nullable=False) # Child 1-to-1 w User
    # project_id = db.Column(db.Integer, primary_key=True) # FK w project_id
    # user_id = db.Column(db.Integer, primary_key=True) # FK w user_id

    def __repr__(self):
        return f"<ProjectManager | project_id : {self.project_id} | user_id : {self.user_id}>"

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'), primary_key=True, nullable=False) # Child 1-to-Many w Project
    # project_id = db.Column(db.Integer, primary_key=True) # FK w project_id

    filename = db.Column(db.String(200), nullable=False)
    item_data = db.Column(db.String, nullable=False) # Base64 String (?)

    label = db.relationship('Label', backref='task', lazy=True, nullable=True) # Parent 1-to-Many w Label

    def __repr__(self):
        return f"<Task | task_id : {self.task_id} | project_id : {self.project_id} | filename : {self.filename}>"

class Label(db.Model):
    task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'), primary_key=True, nullable=False) # Child 1-to-Many w Task
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True, nullable=False) # Child 1-to-Many w User
    # task_id = db.Column(db.Integer, primary_key=True) # FK w task_id
    # user_id = db.Column(db.Integer, primary_key=True) # FK w user_id

    label_data = db.Column(db.String, nullable=False) # JSON

    def __repr__(self):
        return f"<Label | task_id : {self.task_id} | user_id : {self.user_id}>"
