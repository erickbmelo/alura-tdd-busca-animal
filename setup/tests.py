from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Edge('C:\Users\Erick\Documents\ALURA-TDD\msedgedriver.exe')