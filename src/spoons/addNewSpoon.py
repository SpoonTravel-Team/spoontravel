import webapp2
from spoons.model.Spoon import Spoon
from google.appengine.ext import db

class AddNewSpoon(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write("""
            <h1><center>Adding a new spoon</center></h1><br\>
            <form action="/addNewSpoon" method="post" enctype="multipart/form-data">
                <div>Comment: <textarea name="comment" rows="3" cols="60"></textarea></div>
                <div><label>Picture:</label></div>
                <div><input type="file" name="img"/></div>
                <div><input type="submit" value="Add my spoon"></div>
              </form>
              """)
                
    def post(self):        
        #Creating spoon
        spoon = Spoon()
        spoon.comment = self.request.get('comment')
        picture=self.request.get('img')
        spoon.image_blob = db.Blob(picture)
        spoon.put()
        
        #Responding
        self.response.out.write("""
            <center>You added a new spoon. Now mark the following message on your spoon : <br\>
            <b>Look at this spoon's travel on <i>http://thespoontravel.appspot.com</i>. SpoonNumber: %s</b>
            </center>
            """ % spoon.spoonNumber())