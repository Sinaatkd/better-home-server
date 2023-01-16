from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, CreateView

from user_contact_module.models import UserContact

from .forms import CreateUserContactForm

class DeleteUserContactView(DeleteView):
    model = UserContact
    template_name = 'user_contact/user_contact_confirm_delete.html'
    success_url = reverse_lazy('users-list')


class CreateUserContactView(CreateView):
    model = UserContact
    form_class = CreateUserContactForm
    template_name = 'user_contact/user_contact_form.html'

    def form_valid(self, form):
        consultant_id = self.kwargs['consultant_id']
        
        obj = form.save(commit=False)
        obj.consultant_id = consultant_id
        obj.save()
        return redirect(reverse('user-detail', args=(consultant_id,)))