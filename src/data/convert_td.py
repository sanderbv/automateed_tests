from dataclasses import dataclass
import json


@dataclass
class Person:
    FirstName: str = None
    LastName: str = None
    Email: str = None
    Mobile: str = None
    Address: str = None


with open('../src/data/testdata.json') as file:
    data = json.load(file)


def generated_person():
    return Person(
        FirstName=data["StudentRegistrationForm"][0]['FirstName'],
        LastName=data["StudentRegistrationForm"][0]['LastName'],
        Email=data["StudentRegistrationForm"][0]['Email'],
        Mobile=data["StudentRegistrationForm"][0]['Mobile'],
        Address=data["StudentRegistrationForm"][0]['Address']
    )

