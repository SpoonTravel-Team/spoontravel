from google.appengine.ext import db
import webapp2

class Spoon(db.Model):
    creationDate = db.DateTimeProperty(auto_now_add=True)
    comment = db.StringProperty(multiline=True)
    image_blob = db.BlobProperty()
    
    def spoonNumber(self):
        return self.key().id()
    
class SpoonImage(webapp2.RequestHandler):
    def get(self):
        spoon = db.get(self.request.get("img_id"))
        if spoon.image_blob:
            self.response.headers['Content-Type'] = "image/png"
            self.response.out.write(spoon.image_blob)
        else:
            self.response.out.write("No image")