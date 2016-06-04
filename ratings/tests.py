"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Rating
from forms import RatingForm
from django.core.urlresolvers import reverse


def create_and_save_rating():

    """Creates a new rating and saves it in the database."""

    form_data = {'score': 9, 'beer_name': "Test Beer", 'brewer_name': "Test Co", 'notes': "Test Notes"}
    form = RatingForm(data=form_data)
    rating = form.save()

    return rating


class RatingTests(TestCase):

    def test_homepage(self):

        """Test that homepage URL is working."""

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_form_data_is_valid(self):

        """Test that rating form is working."""

        form_data = {'score': 9, 'beer_name': "Test Beer", 'brewer_name': "Test Co", 'notes': "Test Notes"}
        form = RatingForm(data=form_data)
        self.assertTrue(form.is_valid())
        rating = form.save()
        self.assertEqual(rating.score, 9)
        self.assertEqual(rating.beer_name, "Test Beer")
        self.assertEqual(rating.brewer_name, "Test Co")
        self.assertEqual(rating.notes, "Test Notes")

    def test_form_fails_with_invalid_data(self):

        """Test that form will fail if given invalid data."""

        form_data = {'score': 11, 'beer_name': "Test Beer", 'brewer_name': "Test Co", 'notes': "Test Notes"}
        form = RatingForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_show_rating_detail(self):

        """Test that rating detail page is working."""

        rating = create_and_save_rating()
        response = self.client.post(reverse('rating_detail', args=(rating.pk,)))
        self.assertContains(response, 'Current Rating')
        self.assertContains(response, rating.beer_name)

    def test_edit_rating(self):

        """Test that edit rating feature is working by checking database values before and after edit of beer name."""

        rating = create_and_save_rating()
        rating_in_db = Rating.objects.filter(pk=rating.pk).exists()
        self.assertEqual(rating.beer_name, "Test Beer")

        response = self.client.post(reverse('rating_edit', args=(rating.pk,)))

        form_data = {'score': 9, 'beer_name': "Testing Edit", 'brewer_name': "Test Co", 'notes': "Test Notes"}
        form = RatingForm(data=form_data)
        self.assertTrue(form.is_valid())
        rating = form.save()

        self.assertEqual(rating_in_db, True)
        self.assertEqual(rating.beer_name, "Testing Edit")
        self.assertEqual(response.status_code, 200)

    def test_delete_rating(self):

        """Test that delete rating feature is working by checking database before and after deleting."""

        rating = create_and_save_rating()
        rating_in_db = Rating.objects.filter(pk=rating.pk).exists()
        response = self.client.post(reverse('rating_delete', args=(rating.pk,)))
        rating_not_in_db = Rating.objects.filter(pk=rating.pk).exists()

        self.assertEqual(rating_in_db, True)
        self.assertEqual(rating_not_in_db, False)
        self.assertEqual(response.status_code, 302)
