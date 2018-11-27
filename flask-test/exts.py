#coding: utf-8
'''
为了防止循环引用创建的附加文件
'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

