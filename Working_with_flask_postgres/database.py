# a simple db py script via sqlalchemy orm.
from sqlalchemy import create_engine, select, Column, Integer, ForeignKey, String, update # integer and column should be sentence case.
from sqlalchemy.orm import registry, Session, relationship

engine = create_engine('postgresql+psycopg2://postgres:sqltopostgre@localhost/pt') # pt short for project_tracker.

mapper_registry = registry()

Base = mapper_registry.generate_base()

class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key = True)
    title = Column(String(length = 25))
    # description = Column(String(length = 25))

    def __repr__(self):
        return f'< Project (project_id = {self.project_id}, Project(title = {self.title}) >'

class Task(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key = True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    description = Column(String(length = 25))

    cux = relationship('Project')  # relationship on the application side is made on the model.

    def __repr__(self):
        return f'< Task (task_id = {self.task_id}, description = {self.description}, project_id = {self.project_id}) >'

Base.metadata.create_all(engine)

with Session(engine) as session:

    # a_record = Project(title = "Clean House")
    # session.add(a_record)
    # session.flush() # creates a pending transaction, such that a project_id is generated.

    # task = Task(project_id = a_record.project_id, description = "Start from bedroom")
    # session.add(task)
    # session.commit()
    # print(list(session.execute(select(Project))))
    # print(list(session.execute(select(Task))))

    # new_task_desc = Task(task_id = in_id, description = in_description +  "-completed")
    # session.add(new_task_desc) # this insert operation will create another record. That is not required.

    # new_task_desc.description = in_description + "-completed"

    # def alter(in_description: str):

    #     # newtask = Task(description = in_description)
    #     # res =  session.execute(select(Task).where(description == in_description)).scalar()
    #     # newtask.description = in_description + " --completed"
    #     # session.commit()
    #     # print(res.description)
    #     update_stmt = update(Task).where(Task.description == in_description).values(description = in_description + " - Done")
    #     session.execute(update_stmt)
    #     session.commit()
    #     print("Alteration complete...\n")
        print(list(session.execute(select(Project))))
        
    # alter("Clean room")
