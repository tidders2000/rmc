import unittest
from flask import Flask
from app import app

#ensure that index loads
class crowdtest(unittest.TestCase):
	def test_index(self):
		tester= app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)
#ensure that index load
