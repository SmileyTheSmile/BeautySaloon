from unittest import TestCase
from transactions import Transactions


class TestTransaction(TestCase):
    transactions = Transactions()
    def test_login(self):
        self.assertEqual(Transactions().authenticate("kdanil01", "password")[0], 0)
        self.assertEqual(Transactions().authenticate("kdanil01", "password1111")[0], 1)
        
    def test_load_all_cosmetologists(self):
        self.assertEqual(Transactions().load_all_cosmetologists()[0], 0)
        
    def test_load_all_appointments(self):
        self.assertEqual(Transactions().load_all_appointments()[0], 0)
        
    def test_add_coTransactionssmetologist(self):
        self.assertEqual(Transactions().add_cosmetologist()[0], 0)
        
    def test_load_all_clients(self):
        self.assertEqual(Transactions().load_all_clients()[0], 0)
        
    def test_create_appointment(self):
        self.assertEqual(Transactions().create_appointment()[0], 0)
        
    def test_register_client(self):
        self.assertEqual(Transactions().register_client()[0], 0)
        
    def test_create_cosmetologist(self):
        self.assertEqual(Transactions().create_cosmetologist()[0], 0)