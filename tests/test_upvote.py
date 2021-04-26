from app.models import Upvote
import unittest
from app import db

class TestUpvote(unittest.TestCase):
  def setUp(self):
    self.new_upvote=Upvote(counter=counter)
    db.session.add(self.new_upvote)
    db.session.commit()

  def tearDown(self):
    Upvote.query.delete()
    db.session.commit()

  def test_save_upvote(self):
    self.new_upvote.save_upvotes()
    self.assertTrue(len(Upvote.query.all()) > 0)