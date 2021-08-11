import unittest
import main
import utils

#Unit Tests
class TestClasses(unittest.TestCase):
    '''This is a test for my classes. '''
    testcar = utils.Car('XXXX-0000')
    testdate = utils.Date('04/21/1998','00:00')

    def test_licensaplate(self,testcar):
        self.assertEqual(testcar.licensaplate,'XXXX-0000','Should be XXXX-0000')
    
    def test_getlastdigit(self,testcar):
        self.assertEqual(testcar.getlastdigit(),'0','Should be equal to 0')
    
    def test_dateandtime(self,testdate):
        self.assertEqual(testdate.date,'01/01/1999','Should be 01/01/1999')
        self.assertEqual(testdate.time,'00:00', 'Should be 00:00')

    def test_getweekday(self,testdate):
        self.assertEqual(testdate.getweekday(),2,'Should be 2 so it was a Tuesday :)')
    
    def test_is_in_between(self,testdate):
        self.assertFalse(testdate.is_in_between(),'Should be False because 00:00 is not within the restricted time ranges')


