import os


class Config(object): 
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_will_never_guess'
    
    
