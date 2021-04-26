import unittest
from app import db
from app.models import Comment


class TestComment(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(comment='comment')
        db.session.add(self.new_comment)
        db.session.commit()

    def tearDown(self):
        Comment.query.delete()
        db.session.commit()

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment, 'comment')

    def tearDown(self):
        Comment.query.delete()
        db.session.commit()

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment, 'comment')