from django import forms
from .models import Booking, Building, BookTime, Place
from django.contrib.auth.models import User
import pdb


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('responsible', 'time', 'place', 'name', 'start_date', 'end_date', 'engineering')

    def save(self, user=None, commit=True):
        time = self.cleaned_data['time']
        booking = Booking()
        booking.user = user
        booking.place = self.cleaned_data['place']
        booking.start_date = self.cleaned_data['start_date']
        booking.end_date = self.cleaned_data['end_date']
        booking.responsible = self.cleaned_data['responsible']
        booking.name = self.cleaned_data['name']
        booking.status = 2
        booking.engineering = self.cleaned_data['engineering']

        if commit:
            booking.save()
            for times in time:
                ti = BookTime.objects.get(id=times.id)
                booking.time.add(ti)

        return booking


