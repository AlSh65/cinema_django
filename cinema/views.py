from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Cinema, Category
from .forms import ReviewForm


class CinemaViews(ListView):
    model = Cinema
    queryset = Cinema.objects.filter(draft=False)
    template_name = 'cinema/cinema.html'


class CinemaDetailView(DetailView):
    model = Cinema
    # template_name = 'cinema/cinema_detail.html'
    slug_field = 'url'



class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        cinema = Cinema.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.cinema_id = pk
            form.save()
        return redirect(cinema.get_absolute_url())
