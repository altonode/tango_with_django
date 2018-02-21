from django import forms
from django.contrib.auth.models import User

from tango_with_django.rango.models import Page, Category, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=
                           Category._meta.get_field('name').max_length,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=
                               Category._meta.get_field('views').default)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=
                               Category._meta.get_field('likes').default)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)


    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model.
        model = Category
        fields = ('name',)
        

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=
                            Page._meta.get_field('title').max_length,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=
                         Page._meta.get_field('url').max_length,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=
                               Page._meta.get_field('views').default)


    class Meta:
        # Provide an association between the ModelForm and a model.
        model = Page
        # Exclude the category field to hide the foreign key.
        exclude = ('category',)

    def clean(self):
        # Obtain the submitted url from a validated form
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url present and doesn't start with http,
        # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),
                               help_text="Please enter a password.")
    username = forms.CharField(help_text="Please enter a username")
 

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        
class UserProfileForm(forms.ModelForm):
    website = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    
    class Meta:
        model = UserProfile
        exclude = ('user',)


class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'size':'50'}),
        error_messages={'required': 'Please key in query then click search button'},
        label='')
