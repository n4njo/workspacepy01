from config.database import *
from config.mail import *


class App:

    def __init__(self,path):
        stmp_server,port,user,password=[
                'sandbox.smtp.mailtrap.io',
                2525,
                'ef5fb620821dab',
                '88eccce857c667'
                ]
        self.bd:Database=Database(path)        
        self.mail=Mail(stmp_server,port,user,password)