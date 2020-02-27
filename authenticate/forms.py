from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].label =''
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].label =''
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].label =''
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)
    