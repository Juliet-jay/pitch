import unittest
from app.models import Comment, User, Pitch
from app import db


class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_emma = User(
            username='emma', password='potato', email='emma@ms.com')
        self.new_pitch = Pitch(id=1, pitch_title='Test', pitch_content='This is a test pitch',
                               category="interview", user=self.user_emma)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()