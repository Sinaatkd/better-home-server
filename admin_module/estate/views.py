from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from django.urls import reverse_lazy
from django.shortcuts import redirect

from estate_module.models import Estate, EstateProperty, EstateRegion, EstateImage

from .forms import CreateEstateForm, UpdateEstateForm, CreateEstatePropertyForm, UpdateEstatePropertyForm, CreateUpdateEstateRegionForm, CreateUpdateEstateImageForm

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
    


class EstateDetailView(DetailView):
    model = Estate
    template_name = 'estate/estate_detail.html'
    

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


class EstatePropertyCreateView(CreateView):
    model = EstateProperty
    form_class = CreateEstatePropertyForm
    template_name = 'estate/properties/estate_property_form.html'
    success_url = reverse_lazy('estate-property-list')



class EstatePropertyUpdateView(UpdateView):
    model = EstateProperty
    form_class = UpdateEstatePropertyForm
    template_name = 'estate/properties/estate_property_form.html'
    success_url = reverse_lazy('estate-property-list')


class EstateRegionListView(ListView):
    model = EstateRegion
    paginate_by = 30
    template_name = 'estate/region/estate_region_list.html'


    def get_queryset(self):
        search = self.request.GET.get('search', '')
        object_list = self.model.objects.all().order_by('-id')
        if search:
            object_list = self.model.objects.filter(title__icontains=search).distinct().order_by('-id')
        return object_list


class EstateRegionDeleteView(DeleteView):
    model = EstateRegion
    template_name = 'estate/region/estate_region_confirm_delete.html'
    success_url = reverse_lazy('estate-region-list')


class EstateRegionCreateView(CreateView):
    model = EstateRegion
    form_class = CreateUpdateEstateRegionForm
    template_name = 'estate/region/estate_region_form.html'
    success_url = reverse_lazy('estate-region-list')



class EstateRegionUpdateView(UpdateView):
    model = EstateRegion
    form_class = CreateUpdateEstateRegionForm
    template_name = 'estate/region/estate_region_form.html'
    success_url = reverse_lazy('estate-region-list')


class EstateImageDeleteView(DeleteView):
    model = EstateImage
    template_name = 'estate/image/estate_image_confirm_delete.html'
    
    def get_success_url(self) -> str:
        estate_id = self.kwargs['estate_id']
        return reverse_lazy('estates-detail', args=(estate_id,))

class EstateImageCreateView(CreateView):
    model = EstateImage
    form_class = CreateUpdateEstateImageForm
    template_name = 'estate/image/estate_image_form.html'

    def form_valid(self, form):
        estate_id = self.kwargs['estate_id']
        obj = form.save(commit=False)
        obj.save()
        selected_estate = Estate.objects.filter(pk=estate_id).first()
        selected_estate.images.add(obj)
        selected_estate.save()
        return redirect(reverse_lazy('estates-detail', args=(estate_id,)))