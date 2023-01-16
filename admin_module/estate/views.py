from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from django.urls import reverse_lazy

from estate_module.models import Estate, EstateProperty

from .forms import CreateEstateForm, UpdateEstateForm

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


class EstateUpdateView(UpdateView):
    model = Estate
    form_class = UpdateEstateForm
    template_name = 'estate/estate_form.html'
    success_url = reverse_lazy('estates-list')


class EstatePropertyListView(ListView):
    model = EstateProperty
    template_name = 'estate/properties/estate_property_list.html'
    paginate_by = 30


    def get_queryset(self):
        search = self.request.GET.get('search', '')
        object_list = self.model.objects.all().order_by('-id')
        if search:
            object_list = self.model.objects.filter(title__icontains=search).distinct().order_by('-id')
        return object_list


class EstatePropertyDeleteView(DeleteView):
    model = EstateProperty
    template_name = 'estate/properties/estate_property_confirm_delete.html'
    success_url = reverse_lazy('estate-property-list')
