from django.test import Client, TestCase

from jobsboard.common.factories import UserFactory


class JobCreateViewTest(TestCase):

    # TODO: test_create_logged_in()

    def test_logged_out(self):
        '''
        This checks if a logged out user visiting
        the page for job creation is redirected to
        the login page.
        '''
        client = Client()
        response = client.get('/jobs/new/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/jobs/new/')

    def test_logged_in(self):
        '''
        This checks if a logged out user visiting
        the page for job creation is redirected to
        the login page.
        '''
        user = UserFactory()
        user.set_password('testpassword')
        user.save()

        client = Client()
        login_success = client.login(username=user.username,
                                     password='testpassword')
        assert(login_success)

        response = client.get('/jobs/new/', follow=True)
        assert(response.status_code == 200)
