from django.shortcuts import render, redirect
from aloqa.forms import ContactForm
from django.contrib import messages

from django.http import JsonResponse
# def contact_views(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = ContactForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Xabar yuborildi!')
#             return redirect('home')
#     else:
#         form = ContactForm()
#
#     context = {
#         form: form,
#     }
#
#     return render(request, 'core/base.html', context)


def contact_views(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False, "error": form.errors}, status=400)
    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)
