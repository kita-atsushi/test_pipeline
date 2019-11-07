import hug


@hug.get('/hello')
def hello(name):
    """Says Hello to a user"""
    return "Hello {}!".format(name)

@hug.get('/hi')
def hi(name):
    """Says Hi to a user"""
    return "Hi {}!".format(name)

@hug.get('/namaste')
def hi(name):
    """Says Hi to a user"""
    return "Hi {}!".format(name)
