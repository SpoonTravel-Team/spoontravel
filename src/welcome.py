import webapp2
from spoons.followSpoon import FollowSpoon
from spoons.addSpoonStep import AddSpoonStep
from spoons.addNewSpoon import AddNewSpoon
from spoons.model.Spoon import SpoonImage
from spoons.model.SpoonStep import SpoonStepImage

class Welcome(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('<h1><center>Welcome on SpoonTravel!</center></h1><br\>')
        self.response.out.write("""
            <center>
                <h3>Add a new Spoon</h3>
                <form action="/addNewSpoon" method="get">
                    <div><input type="submit" value="Add a new spoon"></div>
                </form>
            </center><br/>
              """)
        self.response.out.write("""
            <center>
                <h3>Follow a Spoon</h3>
                <form action="/followSpoon" method="post">
                    <div><input type="text" name="spoonNumber" ></input></div>
                    <div><input type="submit" value="Follow this spoon"></div>
                </form>
            </center><br/>
              """)
        self.response.out.write("""
            <center>
                <h3>Add a step to a spoon life</h3>
                <form action="/addSpoonStep" method="post">
                    <div><input type="text" name="spoonNumber" ></input></div>
                    <div><input type="submit" value="Add a step to this spoon life"></div>
                </form>
            </center><br/>
              """)

app = webapp2.WSGIApplication([('/', Welcome),
                              ('/followSpoon',FollowSpoon),
                              ('/addSpoonStep',AddSpoonStep),
                              ('/addNewSpoon',AddNewSpoon),
                              ('/spoonImage',SpoonImage),
                              ('/spoonStepImage',SpoonStepImage)],
                              debug=True)
