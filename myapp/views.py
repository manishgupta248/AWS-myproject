from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView, DetailView
from .models import Notice
from .forms import NoticeForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def home(request):
    return render(request,'home.html',{})

# class index(TemplateView):
#     template_name = "frontend/index.html"
#     def get_context_data(self, **kwargs):
#         return ({'name':'Manish'})
    #_--------------------------------------------------------------------------
class NoticeListView(ListView):
    model = Notice
    template_name = "notices/notice-list.html"

class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = "create.html"

class NoticeUpdateView(LoginRequiredMixin, UpdateView):
    model = Notice
    fields =['subject', 'notice_date', 'notice_copy',]
    template_name = "create.html"

class NoticeDetailView(DetailView):
    model = Notice
    template_name = "notices/notice.html"

class NoticeDeleteView(LoginRequiredMixin, DeleteView):
    model = Notice
    template_name = "notices/notice-delete.html"
    success_url = reverse_lazy('notice_list')