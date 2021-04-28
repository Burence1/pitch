from app.models import User,Upvote,Downvote,Comment,Pitch
from app import db
import unittest

class TestUser(unittest.TestCase):
  def setUp(self):
      self.new_user = User(username = "burens", email ="burens@gmail.com", bio = "soft dev", profile_pic_path = "image_url", password = 'burens')
      db.session.add(self.new_user)
      db.session.commit()

  def tearDown(self):
      User.query.delete()
      db.session.commit()

  def test_check_instance_variables(self):
      self.assertEquals(self.new_user.username, 'burens')
      self.assertEquals(self.new_user.email, 'burens@gmail.com')
      self.assertEquals(self.new_user.bio, 'soft dev')
      self.assertEquals(self.new_user.profile_pic_path, 'image_url')
      self.assertTrue(self.new_user.password, 'burens')

  def test_password_setter(self):
      self.assertTrue(self.new_user.password_hash is not None)

  def test_no_access_password(self):
      with self.assertRaises(AttributeError):
            self.new_user.password

  def test_password_verification(self):
      self.assertTrue(self.new_user.verify_password('burens'))