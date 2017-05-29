import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# local imports
from app import create_app
from config import app_config
from app.models import Employee, Department, Role, db

app = create_app('development')

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':

    manager.run()
