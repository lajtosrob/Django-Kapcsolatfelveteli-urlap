from django import forms

temak = [('Egyéb', 'egyéb'), ('Reklamáció', 'reklamáció'), ('Megkeresés', 'megkeresés'), ("Tájékoztatás", 'tájékoztatás')]

class ContactForm(forms.Form):
    nev = forms.CharField(max_length=50, label="Név", widget=forms.TextInput(attrs={'placeholder': 'Az ön neve...'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'nev@mail.com...'}))
    tema = forms.ChoiceField(choices=temak, label="Téma")
    uzenet = forms.CharField(label="Üzenet", widget=forms.Textarea(attrs={'placeholder': 'Írjon nekünk...'}))
