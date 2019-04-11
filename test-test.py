import unittest
from flask_testing import TestCase
from app import app, connection

class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        connection.cursor()
        #db.session.add(User("admin", "ad@min.com", "admin"))
        #db.session.add(
        #    BlogPost("Test post", "This is a test. Only a test.", "admin"))
        #db.session.commit()

    def tearDown(self):
        connection.cursor()
        

class FlaskTestCase(BaseTestCase):
    
    def test_indexroute(self):
        response=self.client.get('/',content_type='text.html')
        self.assertEqual(response.status_code, 200)
        
    def test_indexlog(self):
        response=self.client.post('/',data=dict(email='testuserfour@email.com', password='password'), follow_redirects=True)
        self.assertTrue(b'Home', response.data)
        
    def test_indexincorrect(self):
        response=self.client.post('/',data=dict(email='testuser@email.com', password='password'), follow_redirects=True)
        self.assertTrue(b'Not a Member', response.data)
   
    
    def test_index(self):
        response=self.client.get('/',content_type='text.html')
        self.assertTrue(b'Not a Member', response.data)
        
    def test_home(self):
        response=self.client.get('/home',data=dict(email='testuserfour@email.com', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_badges(self):
        response=self.client.get('/badges',data=dict(email='testuserfour@email.com', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_feedback(self):
        response=self.client.get('/feedback',data=dict(email='testuserfour@email.com', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_add_feedback(self):
        response=self.client.get('/add_feedback',data=dict(email='testuserfour@email.com', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_myprofile(self):
        response=self.client.get('/myprofile',data=dict(email='testuserfour@email.com', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        
if __name__=='__main__':
    unittest.main()