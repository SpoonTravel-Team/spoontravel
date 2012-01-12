import webapp2

class MainPage(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('<h1><center>Welcome on SpoonTravel!</center></h1>')

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
