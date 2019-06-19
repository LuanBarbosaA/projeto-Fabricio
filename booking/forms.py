from django import forms
from .models import Booking, Building, BookTime, Place
from django.contrib.auth.models import User
import pdb


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('responsible', 'time', 'place', 'name', 'start_date', 'end_date', 'engineering')
        '''widgets = {
            'start_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'end_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }'''

    '''def adc_time(self, time):
        for times in time:
            return times'''

    def save(self, user=None, commit=True):
        #pdb.set_trace()
        #user_instance = User.objects.get(id=self.user.id)
        #pdb.set_trace()
        time = self.cleaned_data['time']
        #time_instance = BookTime.objects.get(id=time[0].id)
        #time_instance = self.adc_time(time)
        '''times = BookTime.objects.filter(
            date_booking=time[0].date_booking,
            start_hour=time[0].start_hour,
            end_hour=time[0].end_hour
        )'''
        '''Booking.objects.create(
            responsible=self.cleaned_data['responsible'],
            time=time_instance,
            place=self.cleaned_data['place'],
            name=self.cleaned_data['name'],
            start_date=self.cleaned_data['start_date'],
            end_date=self.cleaned_data['end_date'],
            engineering=self.cleaned_data['engineering'],
            status=2,
            user=user
        )'''
        booking = Booking()
        booking.user = user
        booking.place = self.cleaned_data['place']

        #booking.time = time
        booking.start_date = self.cleaned_data['start_date']
        booking.end_date = self.cleaned_data['end_date']
        booking.responsible = self.cleaned_data['responsible']

        booking.name = self.cleaned_data['name']
        booking.status = 2
        booking.engineering = self.cleaned_data['engineering']

        if commit:
            booking.save()
            for times in time:
                #pdb.set_trace()
                ti = BookTime.objects.get(id=times.id)
                booking.time.add(ti)

        return booking


