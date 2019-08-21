from django import forms
from accounts.models import CustomUser


YEARS = [x for x in range(1940, 2019)]


class UserCreateForm(forms.ModelForm):

    birthday = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = CustomUser
        fields = ('username', 'birthday')
        help_texts = {
            'username': None,
        }
