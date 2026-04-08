from django import forms


class ContactForm(forms.Form):
    parent_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:border-transparent",
            "placeholder": "Your name",
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:border-transparent",
            "placeholder": "your@email.com",
        }),
    )
    phone = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:border-transparent",
            "placeholder": "(604) 555-0123",
        }),
    )
    child_name = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:border-transparent",
            "placeholder": "Child's name",
        }),
    )
    child_age = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:border-transparent",
            "placeholder": "e.g. 3 years old",
        }),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-400 focus:border-transparent",
            "placeholder": "Tell us about your interest in our daycare...",
            "rows": 5,
        }),
    )
    # Honeypot field for spam protection
    website = forms.CharField(required=False, widget=forms.HiddenInput())
