from app.models import Downvote
import unittest
from app import db


class TestDownvote(unittest.TestCase):
  def setUp(self):
    self.new_downvote = Downvote(counter=counter)
    db.session.add(self.new_downvote)
    db.session.commit()

  def tearDown(self):
    Downvote.query.delete()
    db.session.commit()

  def test_save_downvote(self):
    self.new_downvote.save_downvotes()
    self.assertTrue(len(Downvote.query.all()) > 0)
