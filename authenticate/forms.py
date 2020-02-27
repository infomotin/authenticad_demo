from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class PasswordChangF(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
    # def __init__(self,*args,**kwargs):
    #     super(PasswordChangeForm,self).__init__(*args,**kwargs)
    #     self.fields['username'].widget.attrs['class']='form-control'
    #     #self.fields['username'].widget.attrs['helptext']=''
    #     self.fields['username'].label =''
    #     self.fields['username'].help_text =''
    #     self.fields['username'].widget.attrs['placeholder'] ='User Name'
    # password = forms.EmailField(label="",help_text="" ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email Address'}))
    # password1 = forms.CharField(label="",help_text="" ,max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your First Name'}))
    # password2 = forms.CharField(label="",help_text="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Last Name'}))
    

# inheritet UserChangeForm on EditForm 
class RegisterForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        # called Supper Class parrent class inherited with RegisterForm
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

    # changeing Form attre 
    email = forms.EmailField(label="",help_text="" ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email Address'}))
    first_name = forms.CharField(label="",help_text="" ,max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your First Name'}))
    last_name = forms.CharField(label="",help_text="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Last Name'}))
    
    # inheritet User Model 
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

# inheritet UserChangeForm on EditForm 
class EditForm(UserChangeForm):
    password = forms.EmailField(label="",help_text="" ,widget=forms.TextInput(attrs={'type':'hidden'}))
    def __init__(self,*args,**kwargs):
        # called Supper Class parrent class inherited with EditForm
        super(EditForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        #self.fields['username'].widget.attrs['helptext']=''
        self.fields['username'].label =''
        self.fields['username'].help_text =''
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
    email = forms.EmailField(label="",help_text="" ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email Address'}))
    first_name = forms.CharField(label="",help_text="" ,max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your First Name'}))
    last_name = forms.CharField(label="",help_text="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Last Name'}))

