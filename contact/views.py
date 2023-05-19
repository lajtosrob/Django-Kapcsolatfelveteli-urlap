from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nev = form.cleaned_data['nev']
            email = form.cleaned_data['email']
            tema = form.cleaned_data['tema']
            uzenet = form.cleaned_data['uzenet']
            
            print(f'{nev} ebben a témában küldött üzenetet: {tema}')

            """ Itt fog történni az email küldés. """

            return render(request, 'contact_response.html', {'nev': nev})
    
    return render(request, 'contact.html', {'form': form})