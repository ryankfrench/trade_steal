'''
Parameterset edit form
'''

from django import forms

from main.models import ParameterSet

from main.globals import AvatarModes

import  main

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
    
    good_count = forms.IntegerField(label='Number of Goods (2 or 3)',
                                    min_value=2,
                                    max_value=3,
                                    widget=forms.NumberInput(attrs={"v-model":"session.parameter_set.good_count",
                                                                    "step":"1",
                                                                    "max":"3",
                                                                    "min":"2"}))

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
    
    period_length_trade = forms.IntegerField(label='Move Length (seconds)',
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

    group_chat = forms.ChoiceField(label='Group Chat',
                                       choices=((True, 'Yes'), (False,'No' )),
                                       widget=forms.Select(attrs={"v-model":"session.parameter_set.group_chat",}))

    private_chat = forms.ChoiceField(label='Private Chat',
                                       choices=((True, 'Yes'), (False,'No' )),
                                       widget=forms.Select(attrs={"v-model":"session.parameter_set.private_chat",}))
    
    show_avatars = forms.ChoiceField(label='Show Avatars',
                                       choices=((True, 'Yes'), (False,'No' )),
                                       widget=forms.Select(attrs={"v-model":"session.parameter_set.show_avatars",}))
    
    avatar_assignment_mode = forms.ChoiceField(label='Avatar Assignment',
                                       choices=AvatarModes.choices,
                                       widget=forms.Select(attrs={"v-model":"session.parameter_set.avatar_assignment_mode",}))
    
    avatar_grid_row_count = forms.IntegerField(label='Avatar Grid Row Count',
                                                min_value=1,
                                                widget=forms.NumberInput(attrs={"v-model":"session.parameter_set.avatar_grid_row_count",
                                                                                "min":"1"}))
    
    avatar_grid_col_count = forms.IntegerField(label='Avatar Grid Column Count',
                                                min_value=1,
                                                widget=forms.NumberInput(attrs={"v-model":"session.parameter_set.avatar_grid_col_count",
                                                                                "min":"1"}))
    avatar_grid_text = forms.CharField(label='Avatar Grid Text',
                            widget=forms.TextInput(attrs={"v-model":"session.parameter_set.avatar_grid_text",
                                                          })) 

    show_instructions = forms.ChoiceField(label='Show Instructions',
                                       choices=((True, 'Yes'), (False,'No' )),
                                       widget=forms.Select(attrs={"v-model":"session.parameter_set.show_instructions",}))
    
    instruction_set = forms.ModelChoiceField(label='Instruction Set',
                                            empty_label=None,
                                            queryset=main.models.InstructionSet.objects.all(),
                                            widget=forms.Select(attrs={"v-model":"session.parameter_set.instruction_set.id"}))
    
    survey_required = forms.ChoiceField(label='Show Survey',
                                       choices=((True, 'Yes'), (False,'No' )),
                                       widget=forms.Select(attrs={"v-model":"session.parameter_set.survey_required",}))

    survey_link =  forms.CharField(label='Survey Link',
                                   required=False,
                                   widget=forms.TextInput(attrs={"v-model":"session.parameter_set.survey_link",}))
    
    prolific_mode = forms.ChoiceField(label='Prolific Mode',
                                       choices=((True, 'Yes'), (False,'No' )),
                                       widget=forms.Select(attrs={"v-model":"session.parameter_set.prolific_mode",}))

    post_forward_link =  forms.CharField(label='After Session, Forward Subjects to URL',
                                   required=False,
                                   widget=forms.TextInput(attrs={"v-model":"session.parameter_set.post_forward_link",}))

    test_mode = forms.ChoiceField(label='Test Mode',
                                       choices=((True, 'Yes'), (False,'No' )),
                                       widget=forms.Select(attrs={"v-model":"session.parameter_set.test_mode",}))

    class Meta:
        model=ParameterSet
        fields =['town_count','good_count', 'period_count', 'period_length_production' ,
                 'period_length_trade', 'break_period_frequency', 'allow_stealing' ,
                 'group_chat', 'private_chat', 'show_avatars', 'avatar_assignment_mode', 'avatar_grid_row_count', 
                 'avatar_grid_col_count', 'avatar_grid_text', 'show_instructions', 'instruction_set', 'survey_required', 
                 'survey_link', 'prolific_mode', 'post_forward_link', 'test_mode']
    

    def clean_survey_link(self):
        
        try:
           survey_link = self.data.get('survey_link')
           survey_required = self.data.get('survey_required')

           if survey_required == 'True' and not "http" in survey_link:
               raise forms.ValidationError('Invalid link')
            
        except ValueError:
            raise forms.ValidationError('Invalid Entry')

        return survey_link

    def clean_post_forward_link(self):
        
        try:
           post_forward_link = self.data.get('post_forward_link')
           prolific_mode = self.data.get('prolific_mode')

           if prolific_mode == 'True' and not "http" in post_forward_link:
               raise forms.ValidationError('Enter Prolific completion URL')
            
        except ValueError:
            raise forms.ValidationError('Invalid Entry')

        return post_forward_link
    
    def clean_prolific_mode(self):
        
        try:
           prolific_mode = self.data.get('prolific_mode')
           survey_required = self.data.get('survey_required')

           if prolific_mode == 'True' and survey_required == 'True':
               raise forms.ValidationError('Prolific mode is not compatible with a pre-survey')
            
        except ValueError:
            raise forms.ValidationError('Invalid Entry')

        return prolific_mode
