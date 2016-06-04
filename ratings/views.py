from django.shortcuts import render, redirect, get_object_or_404
from ratings.models import Rating
from ratings.forms import RatingForm


def home(request):

    """ Show the entry point to the ratings app
    :param request: Django request object
    :return: rendered homepage
    """
    form = RatingForm()
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save()
            rating.save()
            return redirect('rating_detail', pk=rating.pk)
        else:
            print form.errors

    return render(request, 'ratings/home.html', {'ratings': Rating.objects.all().order_by('-score'), 'form': form})


def rating_detail(request, pk):

    """Show detail for rating given the rating's primary key."""

    rating = get_object_or_404(Rating, pk=pk)

    return render(request, 'ratings/rating_detail.html', {'rating': rating})


def rating_edit(request, pk):

    """Allow user to edit rating."""

    rating = get_object_or_404(Rating, pk=pk)
    if request.method == "POST":
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('rating_detail', pk=rating.pk)
    else:
        form = RatingForm(instance=rating)

    return render(request, 'ratings/rating_edit.html', {'form': form})


def rating_delete(request, pk):

    """Allow user to delete rating."""

    rating = get_object_or_404(Rating, pk=pk)
    Rating.objects.filter(pk=pk).delete()

    return redirect('home')
