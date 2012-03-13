from google.appengine.ext import db
import webapp2
from google.appengine.api import images

class Spoon(db.Model):
    "Spoon model class"
    
    PROPERTIES = set(['creationDate','comment','image_blob'])
    
    creationDate = db.DateTimeProperty(auto_now_add=True)
    comment = db.StringProperty(multiline=True)
    initialOwner = db.StringProperty()
    image_blob = db.BlobProperty()
    
    def spoonNumber(self):
        return self.key().id()
    
class SpoonImage(webapp2.RequestHandler):
    def get(self):
        # Spoon
        spoon = db.get(self.request.get("img_id"))
        
        #Width
        try:
            width = int(self.request.get("width"))
        except ValueError :
            width = 0
        
        #Height
        try:
            height = int(self.request.get("height"))
        except ValueError :
            height = 0
        
        if spoon.image_blob:
            image = images.resize(spoon.image_blob, width, height)
                
            self.response.headers['Content-Type'] = "image/png"
            self.response.out.write(image)
        else:
            self.response.out.write("No image")