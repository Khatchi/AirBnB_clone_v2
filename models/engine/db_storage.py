#!/usr/bin/python3
""" This module defines the database storage.
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State, Base
from models.city import City, Base
from models.review import Review
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
import os

user = os.environ.get("HBNB_MYSQL_USER")
pwd = os.environ.get("HBNB_MYSQL_PWD")
host = os.environ.get("HBNB_MYSQL_HOST")
database = os.environ.get("HBNB_MYSQL_DB")
env = os.environ.get("HBNB_ENV")


class DBStorage:
    """Database storage class
    Attributes: __engine, __session.
    """

    __engine = None
    __session = None
    Session = None

    def __init__(self):
        """Class constructor for creating db engine"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, database),
            pool_pre_ping=True,
        )
        if env == "test":
            metadata = MetaData()
            metadata.drop_all(self.__engine, checkfirst=False)

    def all(self, cls=None):
        """public instance method that returns a dict.
        """
        if cls is None:
            cls = [State, City, User, Place, Review, Amenity]
            query = []
            for c in cls:
                query.extend(self.__session.query(c).all())
        else:
            query = self.__session.query(cls).all()
        cls_objs = {}
        for obj in query:
            cls_objs[obj.to_dict()["__class__"] + "." + obj.id] = obj
        return cls_objs

    def search(self, cls=None, **kwargs):
        """  """
        objs = self.all(cls)
        for key, obj in objs.items():
            flag = 0
            for attr, value in kwargs.items():
                if getattr(obj, attr) != value:
                    flag = 1
                    break
            if flag == 0:
                return obj
        return None

    def new(self, obj):
        """a public instance method that adds a
        new object to a pending state of the database transaction"""
        self.__session.add(obj)

    def save(self):
        """a public instance method that persists the actions
        performed in the current transaction"""
        self.__session.commit()

    def delete(self, obj=None):
        """a public instance method that deletes a created instance
        from the database"""
        if obj:
            self.__session.delete(obj)

    def call(self, string):
        """a public instance method used for executing
        sql commands on the class's engine"""
        self.__engine.execute(string)

    def start_session(self):
        self.__session = DBStorage.Session()

    def stop_session(self):
        self.save()
        self.__session.close()

    def reload(self):
        """A public instance method that creates
        an initialized, thread-safe session.
        """

        Base.metadata.create_all(self.__engine)

        DBStorage.Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = DBStorage.Session()

    def close(self):
        """This calls the remove() method on self.__session"""
        self.__session.close()
