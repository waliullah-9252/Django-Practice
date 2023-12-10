from django import forms
import datetime
from django.core import validators

# Create your forms here.


class ExampleForm(forms.Form):
    # name = forms.CharField()
    # comment = forms.CharField(widget= forms.Textarea)
    # comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    # email = forms.EmailField()
    # agree = forms.BooleanField()
    # data = forms.DateField()
    # birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    # decimal = forms.DecimalField()
    # email_address = forms.EmailField(required=False)
    # message = forms.CharField(max_length=10)
    # email_address = forms.EmailField(label='Please enter your email address')
    # first_name = forms.CharField(initial='Enter your first name')
    # agree = forms.BooleanField(initial=True)
    # today = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [
        ('black', 'Black'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
    ]
    # favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    # favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    # favorite_color = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    # favorite_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    # title = forms.CharField() 
    # description = forms.CharField()
    # first_name = forms.CharField(max_length = 200)  
    # last_name = forms.CharField(max_length = 200)  
    # roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")  
    # password = forms.CharField(widget = forms.PasswordInput()) 

    # file = forms.FileField()

    # duration = forms.DurationField()
    # time = forms.TimeField(widget=forms.NumberInput(attrs={'type': 'datetime-local'}))

    # name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your name'}))
    # email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Type your name'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type your name'}))
    # confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type your name'}))

    # def clean(self):
    #     clean_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     valpass = self.cleaned_data['password']
    #     valconpass = self.cleaned_data['confirm_password']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('your name is al least 10 characters')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('your email address must be .com use')
    #     if valpass != valconpass:
    #         raise forms.ValidationError('your password does not match')
    
    name = forms.CharField(widget = forms.TextInput, validators=[validators.MinLengthValidator(10, message= 'Enter your name at least 10 characters'), validators.MaxLengthValidator(30, message='Enter your name at most 30 characters')])

    email = forms.CharField(widget = forms.EmailInput, validators=[validators.EmailValidator(message='Enter your valid email address')])

    password = forms.CharField(widget= forms.PasswordInput, validators=[validators.MinLengthValidator(8, message='Enter your valid password at least 8 characters'), validators.MaxLengthValidator(30, message='Enter your valid password at most 30 characters')])

