from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():  
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo
            email = EmailMessage(
                "La caffettiera: Nuevo mensaje de contacto", 
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@imbox.mailtrap.io",
                ["naranjohoyosvictormanuel@gmail.com"],
                reply_to= [email]
            )

            try:
                email.send()
                return redirect(reverse('contact') + "?Ok")
            except:
                return redirect(reverse('contact') + "?Fail")
            

    return render(request, "contact/contact.html", {'form':contact_form}) 