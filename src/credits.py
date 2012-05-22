from BaseHandler import BaseHandler

class Credits(BaseHandler):
            
    def get(self):
        context = {}
        self.render_response('credits.html', **context)
        