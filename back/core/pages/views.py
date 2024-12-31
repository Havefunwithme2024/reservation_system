from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import ContactUs, Reservation
from .forms import ContactUsForm, ReservationForm

class IndexView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'pages/index.html'

    def get_success_url(self):
        return reverse_lazy('index_page')


class ReservationView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'pages/reservation.html'

    def get_success_url(self):
        return reverse_lazy('index_page')
