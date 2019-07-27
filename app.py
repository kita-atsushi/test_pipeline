import hug


@hug.get('/hello')
def hello(name):
    """Says Hello to a user"""
    return "Hello {}!".format(name)

