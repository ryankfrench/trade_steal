'''
Parameterset edit form
'''

from django import forms

from main.models import ParameterSet

class ParameterSetForm(forms.ModelForm):
    '''
    Parameterset edit form
    '''
    town_count = forms.IntegerField(label='Number of Towns (3 max)',
                                    min_value=1,
                                    max_value=3,
                                    widget=forms.NumberInput(attrs={"v-model":"session.parameter_set.town_count",
                                                                    "step":"1",
                                                                    "max":"3",
                                                                    "min":"1"}))

    period_count = forms.IntegerField(label='Number of Periods',
                                      min_value=1,
                                      widget=forms.NumberInput(attrs={"v-model":"session.parameter_set.period_count",
                                                                      "step":"1",
                                                                      "min":"1"}))

    period_length_production = forms.IntegerField(label='Production Length (seconds)',
                                                  min_value=1,
                                                  widget=forms.NumberInput(attrs={"v-model":"session.parameter_set.period_length_production",
                                                                                  "step":"1",
                                                                                  "min":"1"}))
    
    period_length_trade = forms.IntegerField(label='Trade Length (seconds)',
                                             min_value=1,
                                             widget=forms.NumberInput(attrs={"v-model":"session.parameter_set.period_length_trade",
                                                                             "step":"1",
                                                                             "min":"1"}))

    break_period_frequency = forms.IntegerField(label='Break Period Frequency (periods)',
                                                min_value=2,
                                                widget=forms.NumberInput(attrs={"v-model":"session.parameter_set.break_period_frequency",
                                                                                "step":"1",
                                                                                "min":"1"}))

    allow_stealing = forms.ChoiceField(label='Allow Stealing',
                                       choices=((True, 'Yes'), (False,'No' )),
                                       widget=forms.Select(attrs={"v-model":"session.parameter_set.allow_stealing",}))
    
    good_a_label = forms.CharField(label='Good A Label',
                                     widget=forms.TextInput(attrs={"v-model":"session.parameter_set.good_a_label",
                                                                   "maxlength": "10"}))

    good_b_label = forms.CharField(label='Good B Label',
                                     widget=forms.TextInput(attrs={"v-model":"session.parameter_set.good_b_label",
                                                                   "maxlength": "10"}))
    
    good_c_label = forms.CharField(label='Good B Label',
                                     widget=forms.TextInput(attrs={"v-model":"session.parameter_set.good_b_label",
                                                                   "maxlength": "10"}))

    good_a_rgb_color = forms.CharField(label='Good A RGB Color',
                                         widget=forms.TextInput(attrs={"v-model":"session.parameter_set.good_a_rgb_color",
                                                                       "maxlength": "10"}))

    good_b_rgb_color = forms.CharField(label='Good B RGB Color',
                                         widget=forms.TextInput(attrs={"v-model":"session.parameter_set.good_b_rgb_color",
                                                                       "maxlength": "10"}))
    
    good_c_rgb_color = forms.CharField(label='Good C RGB Color',
                                         widget=forms.TextInput(attrs={"v-model":"session.parameter_set.good_b_rgb_color",
                                                                       "maxlength": "10"}))

    class Meta:
        model=ParameterSet
        fields =['town_count', 'period_count', 'period_length_production' , 'period_length_trade', 'break_period_frequency', 'allow_stealing',
                 'good_a_label', 'good_b_label', 'good_c_label', 'good_a_rgb_color', 'good_b_rgb_color', 'good_c_rgb_color']
