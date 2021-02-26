"""Test module of user_account app"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from search.models import NewsLetter


class IndexPageTest(TestCase):
    """Tests user_account index page"""

    def setUp(self):
        fake_user = User.objects.create_user(
            username="Vincent74", password="Openclassrooms1"
        )
        fake_user.save()

        user = User.objects.filter(username="Vincent74")
        user_id = user[0].id
        newsletter = NewsLetter(user_id, newsletter_registration=True)
        newsletter.save()

    def test_index_page_user_not_authenticated(self):
        '''tests if redirects none user'''
        response = self.client.get(reverse("user_account"))
        self.assertRedirects(
            response, "/", status_code=302, target_status_code=200
            )

    def test_index_page_user_authenticated(self):
        '''tests if index page displays with known user'''
        self.client.login(username='Vincent74', password='Openclassrooms1')
        response = self.client.get(reverse("user_account"))
        self.assertEqual(response.status_code, 200)

    def test_index_page_newsletter_unsubscribe(self):
        '''tests user unsubscribe from newsletter'''
        self.client.login(username='Vincent74', password='Openclassrooms1')

        response = self.client.post(reverse("user_account"), 
            {"newsletter" : "unsubscribe"})
        user_newsletter_registration = User.objects.filter(username='Vincent74')
        user_newsletter_registration = user_newsletter_registration[0].newsletter.newsletter_registration
        self.assertFalse(user_newsletter_registration)

    def test_index_page_newsletter_subscribe(self):
        '''tests user subscribe from newsletter'''
        self.client.login(username='Vincent74', password='Openclassrooms1')

        response = self.client.post(reverse("user_account"), 
            {"newsletter" : "subscribe"})
        #import code; code.interact(local=dict(globals(), **locals()))
        user_newsletter_registration = User.objects.filter(username='Vincent74')
        user_newsletter_registration = user_newsletter_registration[0].newsletter.newsletter_registration
        self.assertTrue(user_newsletter_registration)


class SignUpTest(TestCase):
    """Tests if sign_in page responds"""

    def test_sign_up(self):
        response = self.client.get("/user_account/sign_in")
        self.assertEqual(response.status_code, 200)

    def test_sign_in_post(self):
        """Tests if usercreationform is ok"""
        response = self.client.post(
            "/user_account/sign_in",
            {
                "username": "Vince74",
                "last_name": "NOWACZYK",
                "first_name": "Vincent",
                "email": "vince@gmail.com",
                "password1": "Radeon74",
                "password2": "Radeon74",
            },
        )
        self.assertRedirects(
            response, "/user_account/login", status_code=302, target_status_code=200
        )


class LoginTest(TestCase):
    """Tests if login works"""

    def setUp(self):
        fake_user = User.objects.create_user(
            username="Vincent74", password="Openclassrooms1"
        )
        fake_user.save()

    def test_login_post_wrong_password(self):
        response = self.client.post(
            "/user_account/login",
            {"username": "Vincent74", "password": "Openclassrooms"},
        )
        self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        response = self.client.post(
            "/user_account/login",
            {"username": "Vincent74", "password": "Openclassrooms1"},
        )
        self.assertRedirects(response, "/", status_code=302, target_status_code=200)

    def test_login_get(self):
        response = self.client.get("/user_account/login")
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.post(
            "/user_account/login",
            {"username": "Vincent74", "password": "Openclassrooms1"},
        )
        response = self.client.get("/user_account/logout")
        self.assertRedirects(
            response, "/user_account/login", status_code=302, target_status_code=200
        )
