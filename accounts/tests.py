from django.test import TestCase
from .models import RecordModel

class RecordModelTest(TestCase):
    def setUp(self):
        self.record = RecordModel.objects.create(
            type='expense',
            category='food',
            sub_category='groceries',
            payment='credit card',
            amount=50.00,
            date='2023-05-07',
            time='12:00:00',
        )
    
    def test_record_model_str_method(self):
        expected_str = "{}. {} - {} - {} - {}".format(
            self.record.id,
            self.record.type,
            self.record.category,
            self.record.payment,
            self.record.amount
        )
        self.assertEqual(str(self.record), expected_str)
    
    def test_record_model_fields(self):
        self.assertEqual(self.record.type, 'expense')
        self.assertEqual(self.record.category, 'food')
        self.assertEqual(self.record.sub_category, 'groceries')
        self.assertEqual(self.record.payment, 'credit card')
        self.assertEqual(self.record.amount, 50.00)
        self.assertEqual(str(self.record.date), '2023-05-07')
        self.assertEqual(str(self.record.time), '12:00:00')