from django import forms
from django.core import validators
from django.contrib.auth.models import User
# from testapptwo.models import model_name(s)

# In the HTML don't forget to add csrf_token!!

# class Form_Name(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget = forms.Textarea)
#     botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

# class Form_From_Model(forms.ModelForm):
#     class Meta:
#         model = model_name

#         ##Several options for how to specify fields:

#         #Option 1
#         fields = '__all__'

#         #Option 2
#         exclude = ['field_one', 'field_two'] ##include but all specified

#         #Option 3
#         fields = ('field_one', 'field_two') ##include only specified