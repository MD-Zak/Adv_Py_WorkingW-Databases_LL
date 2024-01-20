from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, select
from sqlalchemy.orm import registry, relationship, Session

def insert_db():
    with Session(engine) as session: #To create a Transaction cux in sqlAl, use Session.

            organise_closet_project = Project(title = 'Organise closet',
            description = 'Organise closet by color and style') #makes a project obj using the project model.

            session.add(organise_closet_project) #Add used to add a new entry

            session.flush() #This is as same as begin and end in a transaction.

            tasks = [
            Task(project_id = organise_closet_project.project_id, 
            description = 'Decide what clothes to donate'),
            Task(project_id = organise_closet_project.project_id,
            description = 'Organise summer clothes'),
            Task(project_id = organise_closet_project.project_id,
            description = 'Organise winter clothes')
            ]

            session.bulk_save_objects(tasks) #Bulk_save_objects adds multiple entries together.

            session.commit() #All changes are saved. This commit can also be done using session.close(), session.rollback().

def retrieve_db(w_cnd):
    with Session(engine) as session:
        smt = select(Project).where(Project.title == w_cnd)
        results = session.execute(smt)
        project_scalar = results.scalar() #Used to retrieve the first row in the results.

        smt = select(Task).where(Task.project_id == project_scalar.project_id)
        results = session.execute(smt)
        for task in results:
            print(task)

engine = create_engine('mysql+mysqlconnector://root:sqltoshell@localhost:3306/projects',
echo = True) #create_engine() syntax: create_engine('db_type[dialect]+db_driver://username:password@where_db_lives:port_number/connecting_db_name')
# echo = True, will print statements, letting us know what sqlAl does in the background.

#IMPLEMENTATION:

mapper_registry = registry() #the orm only obj. Registry allows us to access the Metadata collection,
# (i.e., Metadata obj, a dictionary which stores a series of tables, with table name-table obj as k-v pairs).

# mapper_registry.metadata 
##accessing the Metadata obj. with Registry.

#In ORM, the table objs. are accessed indirectly through directives applied to mapped classes.

#Each mapped classes is based on a common base class, called the Declarative Base.

Base = mapper_registry.generate_base() #Creating a new Base class.

class Project(Base): #To create a model of the Projects table.
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key = True)
    title = Column(String(length = 50))
    description = Column(String(length = 50))

    def __repr__(self): #Func. to show a printable representation of the obj.
        return "<Project(title = '{0}', description = '{1}')>".format(
            self.title, self.description)

class Task(Base): #Creates a model of the Tasks table.
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    description = Column(String(length=50))

    project = relationship("Project")

    def __repr__(self):
        return "<Task(description='{}')>".format(self.description)

Base.metadata.create_all(engine) #Creates the tables if there are not already present.

# insert_db()
        
retrieve_db('Organise closet')