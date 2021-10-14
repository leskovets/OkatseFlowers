from django.shortcuts import render
from .models import Reviews


def reviews(request):
    review = Reviews.objects.all()
    data = {
        'title': 'Reviews',
        'reviews': review
    }
    return render(request, 'reviews/reviews.html', data)
