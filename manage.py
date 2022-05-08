# from app import create_app,db
# from flask_script import Manager,Server
# from app.models import User,Pitch
# from  flask_migrate import Migrate, MigrateCommand
# #Creating app instance
# app = create_app('development')

# manager = Manager(app)

# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)

# manager.add_command('server',Server)

# @manager.shell
# def make_shell_context():
#     return dict(app = app,db = db,User = User,Pitch=Pitch )

# if __name__ == '__main__':
#     manager.run()
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from .application import app, db


MIGRATION_DIR = os.path.join('models', 'migrations')


migrate = Migrate(app, db, directory=MIGRATION_DIR)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()