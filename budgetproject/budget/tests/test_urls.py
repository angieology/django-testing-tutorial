from django.test import SimpleTestCase #TestCase
# use SimpleTestCase anytime you don't need to interact with database 
from django.urls import reverse, resolve
from budget.views import project_list, project_detail, ProjectCreateView

""" 
django runs tests by looking for any files that start with 'test' 
and any class that start with 'test'
"""
class TestUrls(SimpleTestCase):
    def test_list_url_is_resolves(self):
        # reverse looks through all urls defined in your project for the url defined with the name and returns the actual url
        url = reverse('list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, project_list)

    def test_add_url_is_resolves(self):
        # reverse looks through all urls defined in your project for the url defined with the name and returns the actual url
        url = reverse('add')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    def test_detail_url_is_resolves(self):
        # reverse looks through all urls defined in your project for the url defined with the name and returns the actual url
        url = reverse('detail', args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, project_detail)