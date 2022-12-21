from django.views.generic import ListView, DeleteView, CreateView

from django.urls import reverse_lazy

from estate_module.models import Estate

from .forms import CreateEstateForm

class EstateListView(ListView):
    model = Estate
    paginate_by = 30
    template_name = 'estate/estate_list.html'


    def get_queryset(self):
        search = self.request.GET.get('search', '')
        object_list = self.model.objects.all().order_by('-id')
        if search:
            object_list = self.model.objects.filter(title__icontains=search).distinct().order_by('-id')
        return object_list


class EstateDeleteView(DeleteView):
    model = Estate
    template_name = 'estate/estate_confirm_delete.html'
    success_url = reverse_lazy('estates-list')
    

class EstateCreateView(CreateView):
    model = Estate
    form_class = CreateEstateForm
    template_name = 'estate/estate_form.html'
    success_url = reverse_lazy('estates-list')

