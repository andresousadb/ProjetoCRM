from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from .models import Record
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a record

# class CreateRecordForm(forms.ModelForm):
#     class Meta:
#         model = Record
#         fields = ['nome', 'sobrenome', 'email', 'telefone', 'endereco', 'cidade', 'cep', 'sexo', 'status_civil',
#                   'dt_nascimento', 'convite', 'convidou']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Field('dt_nascimento', css_class='datepicker'),  # Adicionando a classe 'datepicker' ao campo de data de nascimento
#             # Outros campos do formulário
#             Submit('submit', 'Submit')
#         )

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'endereco', 'cidade', 'cep', 'sexo', 'status_civil',
                  'dt_nascimento', 'convite', 'convidou']


#Update a record

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'endereco', 'cidade', 'cep', 'sexo', 'status_civil',
                  'dt_nascimento', 'convite', 'convidou']
