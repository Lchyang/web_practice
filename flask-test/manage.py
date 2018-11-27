#coding:utf-8

from exts import db
from views import app
from flask_script import Manager
#flask 的命令行工具
from flask_migrate import Migrate,MigrateCommand
from models import User


manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()