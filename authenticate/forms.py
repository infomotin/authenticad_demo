from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        #self.fields['username'].widget.attrs['helptext']=''
        self.fields['username'].label =''
        self.fields['username'].help_text =''
        self.fields['username'].widget.attrs['placeholder'] ='User Name'

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder'] ='Enter Password'
        #self.fields['password1'].widget.attrs['helptext']=''
        self.fields['password1'].label =''
        self.fields['password1'].help_text =''

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder'] ='Confirm Password'
        #self.fields['password2'].widget.attrs['helptext']=''
        self.fields['password2'].label =''
        self.fields['password2'].help_text =''
    email = forms.EmailField(label="",help_text="" ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email Address'}))
    first_name = forms.CharField(label="",help_text="" ,max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your First Name'}))
    last_name = forms.CharField(label="",help_text="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Last Name'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)
    