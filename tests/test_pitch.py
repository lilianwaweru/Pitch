from app.models import Pitch
from app import db



import unittest

class UserModelTest(unittest.TestCase):
def setUp(self):
    self.new_user = User(username = 'lilian',password = 'banana',email='test@mail.com')
    self.new_pitch = Pitch(id =12,title = 'Pitch',content = 'content',category = 'product',upvote = 0,downvote = 0)

def tearDown(self):
    User.query.delete()
    Pitch.query.delete()

def test_check_instance(self):
    self.assertEquals(self.new_pitch.pitch_title,'Pitch')
    self.assertEquals(self.new_pitch.content,'content')
    self.assertEquals(self.new_pitch.category,"product")
        

def test_save_pitch(self):
    self.new_pitch.save_pitch()
    self.assertTrue(len(Pitch.query.all())>0)

def test_get_pitch_by_is(self):
    self.new_pitch.save_pitch()
    got_pitch = Pitch.get_pitch(12345) 
    self.assertTrue(len(got_pitch) == 1)           
