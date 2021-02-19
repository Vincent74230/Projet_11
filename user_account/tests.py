"""Test module of user_account app"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class IndexPageTest(TestCase):
    """Tests if redirect in case of none user"""
    def test_index_page_user_not_authenticated(self):
        response = self.client.get("user_account")
        self.assertEqual(response.status_code, 404)


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
                "password2": "Radeon74"
            },
        )
        self.assertRedirects(response, "/user_account/login", status_code=302, target_status_code=200)


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
        self.assertRedirects(response, "/user_account/login", status_code=302, target_status_code=200)
