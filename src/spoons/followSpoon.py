import webapp2

class FollowSpoon(webapp2.RequestHandler):
    
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('<h1><center>Following spoon '+self.request.get('spoonNumber')+'</center></h1><br\>')