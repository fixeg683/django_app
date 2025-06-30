from django.views.generic import ListView
from .models import Item

class MoviesView(ListView):
    model = Item
    template_name = "movies.html"
    context_object_name = "object_list"
    paginate_by = 10

    def get_queryset(self):
        return Item.objects.filter(category='M')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Manually assign image filenames for each movie in the desired order
        image_filenames = [
            "deep_cover.jpg",
            "diablo.jpg",
            "distant.jpg",
            "f1_the_movie.jpg",
            "fear_below.jpg",
            "mikaela.jpg",
            "shadow_force.jpg",
            "the_accountant2.jpg",
            "the_amateur.jpg",
            "warfare.jpg",
        ]
        for item, filename in zip(context['object_list'], image_filenames):
            item.image_filename = filename
        return context