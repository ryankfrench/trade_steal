'''
paramters model form
'''
import pytz

from django import forms
from django.forms import ModelChoiceField

from main.models import Parameters

class ParametersForm(forms.ModelForm):
    '''
    paramters model form
    '''
    contact_email = forms.CharField(label='Contact Email Address',
                                    widget=forms.TextInput(attrs={"size":"125"}))

    site_url = forms.CharField(label='Site URL',
                               widget=forms.TextInput(attrs={"size":"125"}))

    experiment_time_zone = forms.ChoiceField(label="Study Timezone",
                                             choices=[(tz, tz) for tz in pytz.all_timezones])

    avatar_sprite_sheet = forms.CharField(label='Avatar Sprite Sheet',
                               widget=forms.TextInput(attrs={"size":"125"}))
    
    graph_sprite_sheet = forms.CharField(label='Graph Sprite Sheet',
                               widget=forms.TextInput(attrs={"size":"125"}))


    class Meta:
        model=Parameters
        fields = ('__all__')
