from pydoc import cli
from django.test import TestCase, Client
from .models import Hero

class HeroTestCase(TestCase):
    def setUp(self) -> None:
        Hero.objects.create(name='Superman')
        Hero.objects.create(name='Batman')
        Hero.objects.create(name='Ironman')

    def test_hero_count(self):
        self.assertEqual(Hero.objects.all().count(), 3)

    def test_hero_id(self) -> None:
        client = Client()
        response = client.get('/hero/1/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('1', response.content.decode())
    
    def test_index(self):
        client = Client()
        
        first_response = client.get('/hero/')
        self.assertEqual(first_response.status_code, 200)
        self.assertIn('1', first_response.content.decode())
        
        second_response = client.get('/hero/')
        self.assertEqual(second_response.status_code, 200)
        self.assertIn('2', second_response.content.decode())