from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    
    def test_indexroute(self):
        tester=app.test_client(self)
        response=tester.get('/',content_type='text.html')
        self.assertEqual(response.status_code, 200)
        
    def test_indexlog(self):
        tester=app.test_client(self)
        response=tester.post('/',data=dict(email='testuserfour@email.com', password='password'), follow_redirects=True)
        self.assertTrue(b'Home', response.data)
        
    def test_indexincorrect(self):
        tester=app.test_client(self)
        response=tester.post('/',data=dict(email='testuser@email.com', password='password'), follow_redirects=True)
        self.assertTrue(b'Not a Member', response.data)
   
    
    def test_index(self):
        tester=app.test_client(self)
        response=tester.get('/',content_type='text.html')
        self.assertTrue(b'Not a Member', response.data)
        
    def test_home(self):
        tester=app.test_client(self)
        response=tester.get('/home',data=dict(email='testuserfour@email.com', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_badges(self):
        tester=app.test_client(self)
        response=tester.get('/badges',data=dict(email='testuserfour@email.com', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_feedback(self):
        tester=app.test_client(self)
        response=tester.get('/feedback',data=dict(email='testuserfour@email.com', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_add_feedback(self):
        tester=app.test_client(self)
        response=tester.get('/add_feedback',data=dict(email='testuserfour@email.com', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_myprofile(self):
        tester=app.test_client(self)
        response=tester.get('/myprofile',data=dict(email='testuserfour@email.com', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        
if __name__=='__main__':
    unittest.main()