#coding:utf-8

import os

DEBUG = True

SECRET_KEY = os.urandom(24)


DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'li720333'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo2'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,
                                                                       PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
