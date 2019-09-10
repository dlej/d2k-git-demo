class HelloWorld(object):

    def __init__(self):

        self.message = 'hello world!'
    
    def say(self, extra_message=None):
        
        if extra_message is None:
            return self.message
        else:
            return self.message + ' ' + extra_message