from .models import User


# (1)Returns all users from user table
def get_all_users():
    return User.objects.all()


# (2)Returns first user in table
def first_user():
    return User.objects.first()


# (3)Returns last user in table
def last_user():
    return User.objects.last()


# (4)Returns single user by name
def user_by_name(user_name):
    return User.objects.get(name=user_name)


# ***(5)Returns single user by id
def user_by_id(user_id):
    return User.objects.get(id=user_id)
