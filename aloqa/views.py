from django.shortcuts import render, redirect
from aloqa.forms import ContactForm
from django.contrib import messages


def contact_views(request):
    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Xabar yuborildi!')
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        form: form,
    }

    return render(request, 'contact/contact.html', context)
