from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Quote
from .models import Author
from django.utils.translation import gettext_lazy as _

class UkrainianUserCreationForm(UserCreationForm):
    username = forms.CharField(label=_("Ім'я користувача"), help_text=_("Обов'язкове поле. Може містити не більше 150 символів. Дозволені лише букви, цифри та символи @/./+/-/_"))
    email = forms.EmailField(label=_("Email"), help_text=_("Обов'язкове поле."))
    password1 = forms.CharField(label=_("Пароль"), help_text=_("Ваш пароль не повинен бути схожим на особисту інформацію, містити менше 8 символів, не бути повністю числовим та не бути занадто простим."))
    password2 = forms.CharField(label=_("Підтвердження паролю"), help_text=_("Введіть той же пароль ще раз для підтвердження."))

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class AuthorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AuthorForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'tags']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_author(self):
        author = self.cleaned_data['author']
        if not self.user.is_authenticated and author:
            raise forms.ValidationError("Для додавання цитати автора потрібно бути зареєстрованим користувачем.")
        return author