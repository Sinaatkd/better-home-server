from django.urls import reverse_lazy
from django.views.generic import DeleteView

from user_contact_module.models import UserContact

class DeleteUserContactView(DeleteView):
    model = UserContact
    template_name = 'user_contact/user_contact_confirm_delete.html'
    success_url = reverse_lazy('users-list')