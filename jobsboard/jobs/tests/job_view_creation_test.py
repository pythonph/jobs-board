from django.test import Client, TestCase


class JobCreateViewTest(TestCase):

    def test_logged_out(self):
        '''
        This checks if a logged out user visiting
        the page for job creation is redirected to
        the login page.
        '''
        client = Client()
        response = client.get('/jobs/new/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/jobs/new/')
