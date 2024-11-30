import os

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .form import ContactForm, ContactModelForm, ProfileImage
from .models import Contact, userProfile
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView



class contactView(CreateView):
    form_class = ContactModelForm
    template_name = 'contact_moduels/contact_page.html'
    success_url = '/contact/'

def store_file(file):
    with open('temp/image.jpeg', "wp+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class Createuser(CreateView):
    model = userProfile
    template_name = 'contact_moduels/profile.html'
    fields = ['url_image']
    success_url = 'contact_moduels/profile_user.html'


class ProfileUser(ListView):

    model = userProfile
    template_name = 'contact_moduels/profile_user.html'
    context_object_name = 'profile'



# class profileUser(View):
#     def get(self, request):
#         form = ProfileImage()
#         return render(request, 'contact_moduels/profile_user.html',{
#             'forms': form
#         })
#
#     def post(self, request):
#         form = ProfileImage(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_file = request.FILES['url_image']
#             directory = '/temp'
#
#             file_path = os.path.join(directory, uploaded_file.name)
#             os.makedirs(directory, exist_ok=True)
#
#             with open(file_path, "wb+") as dest:
#                 for chunk in uploaded_file.chunks():
#                     dest.write(chunk)
#
#             new_image = Contact(image_adress=file_path)
#             new_image.save()
#
#             return render(request, 'contact_moduels/profile_user.html', {
#                 'forms': form,
#             })
#         else:
#             return render(request, 'contact_moduels/profile_user.html', {
#                 'forms': form,
#             })

    # def post(self, request):
    #     # print(request.FILES)
    #     # store_file(request.FILES['profile'])
    #     summit = ProfileImage(request.POST, request.FILES)
    #     store_file(request.FILES['profile'])
    #     return redirect('contact_moduels/profile_user.html')

# class contactView(FormView):
#     template_name = 'contact_moduels/contact_page.html'
#     form_class = ContactModelForm
#     success_url = '/contact/'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)






# class contactView(View):
#     def get(self, request):
#         contact_form=ContactModelForm()
#         return render(request, 'contact_moduels/contact_page.html',{
#             'contact_form': contact_form
#         })
#
#
#     def post(self, request):
#         contact_form=ContactModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('product_list')
#         return render(request, 'contact_moduels/contact_page.html',{
#             'contact_form': contact_form
#         })
#     # def post(self, request):
#     #     contact_form = ContactModelForm(request.Post)
#     #     if contact_form.is_valid():
#     #         contact_form.save()
#     #         return redirect('product_list')
#     #     return render(request, 'contact_moduels/contact_page.html',{
#     #         'contact_form': contact_form
#     #     })


# def contact(request):
#     if request.method == 'POST':
#         # contact_form = ContactForm(request.POST)
#         current_contact = Contact.objects.get(pk=1)
#         contact_form = ContactModelForm(request.POST, instance=current_contact)
#         if contact_form.is_valid():
#
#             contact_form.save()
#             return redirect(reverse('product_list'))
#     else:
#             # contact_form = ContactForm()
#             contact_form=ContactModelForm()
#
#     # return render(request,'contact_moduels/contact_page.html',
#     #               {})
#     return render(request,'contact_moduels/contact_page.html',
#                   {'contact_form': contact_form})
#     # if request.method== 'POST':
#     #     enter_email = request.POST['email']
#     #     if enter_email == '':
#     #         return render(request, 'contact_moduels/contact_page.html',
#     #                       )
#     #     # print(request.POST['fname'])
#     #     # print(request.POST['phone'])
#     #     # print(request.POST['subject'])
#     #     # print(request.POST['message'])
#     #     return redirect(reverse('product_list'))
#     # if request.method == 'POST':
#     #     contact_form = ContactForm(request.POST)
#     #     if contact_form.is_valid():
#     #         print(contact_form.cleaned_data)
#     #         contacts=Contact(
#     #             Title=contact_form.cleaned_data.get('Title'),
#     #             Fullname=contact_form.cleaned_data.get('fullname'),
#     #             Email=contact_form.cleaned_data.get('email'),
#     #             Phone=contact_form.cleaned_data.get('phone'),
#     #             Message=contact_form.cleaned_data.get('message')
#     #         )
#     #         contacts.save()
#     #         return redirect(reverse('product_list'))
#     # else:
#     #         contact_form = ContactForm()
#     #
#     # # return render(request,'contact_moduels/contact_page.html',
#     # #               {})
#     # return render(request,'contact_moduels/contact_page.html',
#     #               {'contact_form': contact_form })


