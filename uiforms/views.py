from django.db import models
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login, logout
from django.contrib.auth import login as userlogin
from django.contrib.auth import authenticate
from annoying.decorators import render_to
from django.views.generic import CreateView, UpdateView

from uiforms.forms import *

@render_to('index.html')
def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('dashboard'))
    return {}

@render_to('user_register.html')
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            userlogin(request, new_user)
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = UserRegisterForm()
    return {'form': form}

def user_login(request):
    return login(request, template_name='user_login.html')

def user_logoff(request):
    return logout(request, template_name='user_logoff.html', next_page=reverse('index'))

@render_to('dashboard.html')
def dashboard(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    uiforms = request.user.uiform_set.all()
    return {'uiforms': uiforms}

@render_to('uiform_detail.html')
def uiform_detail(request, pk):
    uiform = request.user.uiform_set.get(pk=pk)
    if request.is_ajax():
        field = uiform.fields().get(id=request.POST['id'])
        field.delete()
        return HttpResponse("success")
    return {'uiform': uiform}

class UIFormFieldCreateView(CreateView):
    context_object_name = 'UI Form Field'
    template_name = 'uiformfield_new.html'
    form_class = UIFormFieldForm

    def get_form_kwargs(self):
        kwargs = super(CreateView, self).get_form_kwargs()
        parent_uiform = self.request.user.uiform_set.get(pk=self.kwargs['pk'])
        kwargs['parent_uiform'] = parent_uiform
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['uiform'] = self.request.user.uiform_set.get(pk=self.kwargs['pk'])
        context['title_prefix'] = "New"
        return context

    def get_success_url(self):
        parent_uiform = self.request.user.uiform_set.get(pk=self.kwargs['pk'])
        return parent_uiform.get_absolute_url()

class UIFormFieldUpdateView(UpdateView):
    context_object_name = 'UI Form Field'
    template_name = 'uiformfield_new.html'
    form_class = UIFormFieldForm

    def get_object(self, **kwargs):
        field = self.request.user.uiform_set.get(pk=self.kwargs['formpk']).fields().get(pk=self.kwargs['fieldpk'])
        return field
    
    def get_form_kwargs(self):
        kwargs = super(UpdateView, self).get_form_kwargs()
        parent_uiform = self.request.user.uiform_set.get(pk=self.kwargs['formpk'])
        kwargs['parent_uiform'] = parent_uiform
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['uiform'] = self.request.user.uiform_set.get(pk=self.kwargs['formpk'])
        context['title_prefix'] = "Edit"
        return context

    def get_success_url(self):
        parent_uiform = self.request.user.uiform_set.get(pk=self.kwargs['formpk'])
        return parent_uiform.get_absolute_url()
    
