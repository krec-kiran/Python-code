import os

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship(
        'Employee',
        secondary='department_employee_new_link'
    )


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    departments = relationship(
        Department,
        secondary='department_employee_new_link'
    )


class DepartmentEmployeeLink(Base):
    __tablename__ = 'department_employee_new_link'
    department_id = Column(Integer, ForeignKey('department.id'), primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)


db_name = 'alembic_sample.sqlite'

from sqlalchemy import create_engine

engine = create_engine('sqlite:///' + db_name)

from sqlalchemy.orm import sessionmaker

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.bind = engine
s = session()
IT = Department(name='IT')
Financial = Department(name='Financial')
s.add(IT)
s.add(Financial)
cathy = Employee(name='Cathy')
marry = Employee(name='Marry')
john = Employee(name='John')
s.add(cathy)
s.add(marry)
s.add(john)
cathy.departments.append(Financial)
marry.departments.append(Financial)
john.departments.append(IT)
s.commit()
s.close()