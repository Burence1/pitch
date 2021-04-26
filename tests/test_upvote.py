from app.models import Upvote
import unittest
from app import db

class TestUpvote(unittest.TestCase):
  def setUp(self):
    self.new_upvote=Upvote(counter=1,user_id=1,pitch_id=1)
    db.session.add(self.new_upvote)
    db.session.commit()