from flask import Blueprint, request
from pydantic import ValidationError
from redis_om.model import NotFoundError
from mgr import redis
from .models import Person



helloworld = Blueprint('hw',__name__)

@helloworld.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

def build_results(people):
    response = []
    for person in people:
        response.append(person.dict())

    return { "results": response }

# Create a new person.
@helloworld.route("/person/new", methods=["POST"])
def create_person():
    try:
        print(request.json)
        new_person = Person(**request.json)
        new_person.save()
        return new_person.pk

    except ValidationError as e:
        print(e)
        return "Bad request.", 400

# Update a person's age.
@helloworld.route("/person/<id>/age/<int:new_age>", methods=["POST"])
def update_age(id, new_age):
    try:
        person = Person.get(id)

    except NotFoundError:
        return "Bad request", 400
    
    person.age = new_age
    person.save()
    return "ok"

# Delete a person by ID.
@helloworld.route("/person/<id>/delete", methods=["POST"])
def delete_person(id):
    # Delete returns 1 if the person existed and was 
    # deleted, or 0 if they didn't exist.  For our 
    # purposes, both outcomes can be considered a success.
    Person.delete(id)
    return "ok"

# Find a person by ID.
@helloworld.route("/person/byid/<id>", methods=["GET"])
def find_by_id(id):
    try:
        person = Person.get(id)
        return person.dict()
    except NotFoundError:
        return {}

# Find people with a given first and last name.
@helloworld.route("/people/byname/<first_name>/<last_name>", methods=["GET"])
def find_by_name(first_name, last_name):
    people = Person.find(
        (Person.first_name == first_name) &
        (Person.last_name == last_name)
    ).all()

    return build_results(people)

# Find people within a given age range, and return them sorted by age.
@helloworld.route("/people/byage/<int:min_age>/<int:max_age>", methods=["GET"])
def find_in_age_range(min_age, max_age):
    people = Person.find(
        (Person.age >= min_age) &
        (Person.age <= max_age)
    ).sort_by("age").all()

    return build_results(people)

# Find people with a given skill in a given city.
@helloworld.route("/people/byskill/<desired_skill>/<city>", methods=["GET"])
def find_matching_skill(desired_skill, city):
    people = Person.find(
        (Person.skills << desired_skill) &
        (Person.address.city == city)
    ).all()

    return build_results(people)

# Find people whose personal statements contain a full text search match
# for the supplied search term.
@helloworld.route("/people/bystatement/<search_term>", methods=["GET"])
def find_matching_statements(search_term):
    people = Person.find(Person.personal_statement % search_term).all()

    return build_results(people)

# Expire a person's record after a given number of seconds.
@helloworld.route("/person/<id>/expire/<int:seconds>", methods=["POST"])
def expire_by_id(id, seconds):
    # Get the full Redis key for the supplied ID.
    try:
        person_to_expire = Person.get(id)
        Person.db().expire(person_to_expire.key(), seconds)
    except NotFoundError:
        pass

    # Return OK whatever happens.
    return "ok"


#eof