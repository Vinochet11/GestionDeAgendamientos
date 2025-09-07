from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from STK.models import Users
from STK.forms import UsersForm
from django.contrib import messages
from django.shortcuts import redirect

def renderTemplate(request):
    return render(request,'Registro.html')


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff
    
class UserList(LoginRequiredMixin,ListView):
    model = Users
    template_name = "core/users_list.html"
    context_object_name="items"
    paginate_by="10"

class UserDetail(LoginRequiredMixin,DetailView):
    model= Users
    template_name = "core/users_details.html"
    context_object_name = "item"

class UserCreate(StaffRequiredMixin,CreateView):
    model= Users
    form_class = UsersForm
    template_name="core/users_form.html"
    success_url=reverse_lazy("users_list")

    def form_valid(self, form):
        obj=form.save(commit=False)
        if not getattr(obj,"rol",None):
            obj.rol="user"
        if not getattr(obj,"status",None):
            obj.status="Activo"
        obj.save()
        messages.success(self.request,"Usuario Creado correctamente.")
        return redirect(self.success_url)
    
    def form_invalid(self, form):
        messages.error(self.request,f"Revisa el formulario:{form.errors}")
        return super().form_invalid(form)

class UserUpdate(StaffRequiredMixin,UpdateView):
    model=Users
    form_class=UsersForm
    template_name="core/users_form.html"
    success_url=reverse_lazy("users_list")

class UserDelete(LoginRequiredMixin,StaffRequiredMixin,DeleteView):
    model=Users
    template_name="core/users_confirms_delete.html"
    success_url=reverse_lazy("users_list")