from django.test import TestCase
from main.models import Vehicle

class VehicleModelTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            name='Test Vehicle',
            description='Test description',
            vehicle_type='SUV',
            year=2025,
            capacity=5,
            price_per_hour=30.00,
            rating=4.5,
            is_available=True
        )

    def test_vehicle_creation(self):
        
        self.assertEqual(self.vehicle.name, 'Test Vehicle')
        self.assertEqual(self.vehicle.vehicle_type, 'SUV')
        self.assertEqual(self.vehicle.price_per_hour, 30.00)

    def test_vehicle_str_method(self):
       
        self.assertEqual(str(self.vehicle), 'Test Vehicle')