from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Place(base):
    __tablename__ = "Place"
    id = Column(Integer, primary_key=True)
    local_name = Column(String)
    address1 = Column(String)
    address2 = Column(String)
    address3 = Column(String)
    keyword = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Place table
limerick = Place(
    local_name="Limerick",
    address1="Main street",
    address2="Love Lane",
    address3="Ireland",
    keyword="Castle"
)
meath = Place(
    local_name="mighty meath",
    address1="Mainly street",
    address2="meath Lane",
    address3="Ireland",
    keyword="Boyne"
)


# add each instance of our programmers to our session
session.add(limerick)
session.add(meath)

# update a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "President"

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# commit our session to the database
session.commit()

# query the database to find all Programmers
places = session.query(Place)
for place in places:
    print(
        place.id,
        place.address1 + ", " + place.address2,
        place.address3,
        "Famous For : " + place.keyword,
        sep=" | "
    )
