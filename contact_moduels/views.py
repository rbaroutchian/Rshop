from django.shortcuts import render, redirect
from django.urls import reverse
from .form import ContactForm, ContactModelForm
from .models import Contact
def contact(request):
    if request.method == 'POST':
        # contact_form = ContactForm(request.POST)
        contact_form = ContactModelForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            contacts=Contact(
                Title=contact_form.cleaned_data.get('Title'),
                Fullname=contact_form.cleaned_data.get('fullname'),
                Email=contact_form.cleaned_data.get('email'),
                Phone=contact_form.cleaned_data.get('phone'),
                Message=contact_form.cleaned_data.get('message')
            )
            contacts.save()
            return redirect(reverse('product_list'))
    else:
            # contact_form = ContactForm()
            contact_form=ContactModelForm()

    # return render(request,'contact_moduels/contact_page.html',
    #               {})
    return render(request,'contact_moduels/contact_page.html',
                  {'contact_form': contact_form })
    # if request.method== 'POST':
    #     enter_email = request.POST['email']
    #     if enter_email == '':
    #         return render(request, 'contact_moduels/contact_page.html',
    #                       )
    #     # print(request.POST['fname'])
    #     # print(request.POST['phone'])
    #     # print(request.POST['subject'])
    #     # print(request.POST['message'])
    #     return redirect(reverse('product_list'))
    # if request.method == 'POST':
    #     contact_form = ContactForm(request.POST)
    #     if contact_form.is_valid():
    #         print(contact_form.cleaned_data)
    #         contacts=Contact(
    #             Title=contact_form.cleaned_data.get('Title'),
    #             Fullname=contact_form.cleaned_data.get('fullname'),
    #             Email=contact_form.cleaned_data.get('email'),
    #             Phone=contact_form.cleaned_data.get('phone'),
    #             Message=contact_form.cleaned_data.get('message')
    #         )
    #         contacts.save()
    #         return redirect(reverse('product_list'))
    # else:
    #         contact_form = ContactForm()
    #
    # # return render(request,'contact_moduels/contact_page.html',
    # #               {})
    # return render(request,'contact_moduels/contact_page.html',
    #               {'contact_form': contact_form })


