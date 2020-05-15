import pymysql
import os
from os.path import abspath
from os.path import dirname
from os.path import join
from os.path import pardir

from dotenv import load_dotenv
 
dotenv_path = abspath(join(dirname(__file__), pardir, '.env'))
load_dotenv(dotenv_path)


MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')



DB_URI = (
    'mysql+pymysql://{MYSQL_USER}/{MYSQL_DATABASE}').format(
        MYSQL_USER= MYSQL_USER,
        MYSQL_DATABASE=MYSQL_DATABASE)