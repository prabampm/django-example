from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

from webapp.models import Contact


class ListContactView(ListView):
    model = Contact

class CreateContactView(CreateView):
	model = Contact
	template_name = 'webapp/add_contact.html'
	def get_success_url(self):
		return reverse('contacts-list')

class ContacteditView(UpdateView):
	model = Contact
	fields = ['first_name','last_name','email']

	template_name = 'webapp/update_contact.html'
	def get_success_url(self):
		return reverse('contacts-list')

class ContactDelete(DeleteView):
	template_name = 'webapp/delete.html'
	model = Contact
	def get_success_url(self):
		return reverse('contacts-list')



# Create your views here.
