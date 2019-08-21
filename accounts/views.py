from django.shortcuts import render
from django.template import Context, loader
import csv
from django.urls import reverse
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from accounts.models import CustomUser
from accounts.forms import UserCreateForm
from accounts.templatetags.custom_tags import if_allowed, if_bizzfuzz


class UserListView(ListView):
    model = CustomUser
    template_name = 'accounts/user_list.html'


class UserDetailedView(DetailView):
    model = CustomUser
    template_name = 'accounts/user_details.html'


class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserCreateForm
    template_name = 'accounts/create.html'

    def get_success_url(self):
        return reverse('accounts:user_list')


class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = UserCreateForm
    template_name = 'accounts/create.html'

    def get_success_url(self):
        return reverse('accounts:user_list')


class UserDeleteView(DeleteView):
    model = CustomUser

    def get_success_url(self):
        return reverse('accounts:user_list')


def generate_csv(request):
    users = CustomUser.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])
    output = []
    for user in users:
        output.append([
            user.username,
            user.birthday,
            if_allowed(user.birthday),
            user.random_field,
            if_bizzfuzz(user.random_field)
        ])
    writer.writerows(output)
    return response
