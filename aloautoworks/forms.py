
from django import forms
from django.forms import ModelForm, TextInput
from django.forms.models import modelformset_factory


from .models import UserQueryData



class UserDataForm(ModelForm):
	class Meta:
		model = UserQueryData
		exclude=[]
	
		def clean(self):
			self.cleaned_data = super(UserDataForm, self).clean()
		
