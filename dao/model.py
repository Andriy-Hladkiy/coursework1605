from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class ormBuilding(Base):
    __tablename__ = 'Building'

    build_number = Column(String(20), primary_key=True)
    build_address = Column(String(20))
    floors_number = Column(String(20))

    Lesson_ = relationship('ormLesson')


class ormUsers(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(40))
    user_surname = Column(String(30))
    user_email = Column(String(30))
    user_groupe = Column(String(40))
    user_faculty = Column(String(40))
    user_course = Column(String(40))
    #lesson_name = Column(String(20), ForeignKey('Lesson.lesson_name'), nullable=False)



class ormLesson(Base):
    __tablename__ = 'Lesson'

    lesson_name = Column(String(20), primary_key=True)
    classroom_number = Column(Integer)
    build_number = Column(String, ForeignKey('Building.build_number'), nullable=False)

    Users__ = relationship('ormUsers')
