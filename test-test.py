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
   
    
    def test_index(self):
        tester=app.test_client(self)
        response=tester.get('/',content_type='text.html')
        self.assertTrue(b'Not a Member', response.data)
if __name__=='__main__':
    unittest.main()