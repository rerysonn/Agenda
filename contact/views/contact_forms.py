from django.shortcuts import render, redirect
from contact.forms import ContactForms


def create(request):
    if request.method == 'POST':
        form =  ContactForms(request.POST)

        context = {
        'form' : form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')


        return render(
            request, 
            'contact/create.html',
            context
        )

    context = {
        'form' : ContactForms()
    }

    return render(
        request, 
        'contact/create.html',
        context
    )