from django import forms
from mvapp.models import mshow
class stForm(forms.ModelForm):
    class Meta:
        model=mshow
        fields='__all__'