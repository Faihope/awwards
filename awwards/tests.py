from django.test import TestCase
from .models import Profile,Project

# Create your tests here.
#setup method
def setUp(self):
    self.projects=Project(title='mytitle',description='description',screenshot1='s1',screenshot2='s2',screenshot3='s3',link='link')