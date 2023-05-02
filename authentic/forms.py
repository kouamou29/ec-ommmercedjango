from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from . models import AdressUser
from django import forms
from django.core.exceptions import ValidationError

class UserFormRegister(UserCreationForm):
    email = forms.EmailField(required=True)
    model = User
    class Meta(UserCreationForm.Meta):
        fields= ('username', 'email', 'password1', 'password2')
        


class AdressFormUser(ModelForm):
    class Meta:
        model = AdressUser
        fields =[ 'contry', 'city', 'adress', 'code_postal']
        
        widgets= {
            'contry': forms.Select(
                attrs={'class': 'py-3 px-6 w-full rounded-md border-solid border-2 border-sky-500'
                       , 'placeholder': ''}),
            'city': forms.TextInput(attrs={'class': 'py-3 px-6 w-full rounded-md border-solid border-2 border-sky-500'
                                , 'placehoder':'city'        }),
            'adress': forms.Textarea(attrs={'class': 'py-3 px-6 w-full rounded-md border-solid border-2 border-sky-500'
                                            ,'placehoder':'Adress' }),
            'code_postal': forms.TextInput(attrs={'class': 'py-3 px-6 w-full rounded-md border-solid border-2 border-sky-500',
                                                  'placehoder':'Code Postal' }),
            
        }
    """
    def clean(self):
        cleaned_data = super().clean()
        city         = cleaned_data.get('city')
        adress  = cleaned_data.get('adress')
            
        if len(city) < 7 or len(code_postal)  < 5 :
            mesg = 'le non du pays droit contenir 7 caratère et et votre de pays mininux 5 caratère '
            
            self.add_error('city', mesg)
            self.add_error('code_postal', mesg)
            return cleaned_data
    """
    def clean_city(self):
        city = self.cleaned_data['city']
        if len(city) < 7:
            raise forms.ValidationError('vous devez faire moins 7 caratère')    
        else:
            return city
      
    def clean_adress(self):
        adress = self.cleaned_data['adress']
        if len(adress) < 7:
            raise forms.ValidationError('vous devez faire moins 7 caratère')    
        else:    
            return adress
    
    def clean_code_postal(self):
        code_postal = self.cleaned_data['code_postal']
        if code_postal < 4:
            raise forms.ValidationError(' entez des chiffres 5')  
        else:    
            return code_postal
    
    
   