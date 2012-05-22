from BaseHandler import BaseHandler

class About(BaseHandler):
            
    def get(self):
        context = {}
        self.render_response('about.html', **context)
        