from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse_lazy
from .forms import RegisterForm
from .models import CustomUser


from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib import messages
from .models import CustomUser


class CustomLoginView(LoginView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        """Se o usuário já estiver autenticado, redireciona para o menu."""
        if request.user.is_authenticated:
            return redirect("menu")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("username")  
        senha = request.POST.get("password")

        if not email or not senha:
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect("login")

        # Verifica se o e-mail existe no banco
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            messages.error(request, "E-mail inexistente.")
            return redirect("login")

        user = authenticate(request, username=email, password=senha)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect("menu")  
        else:
            messages.error(request, "Senha inválida.")
            return redirect("login")


class CustomRegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        """Salva o usuário e envia e-mail de boas-vindas."""
        user = form.save(commit=False) 
        user.name = form.cleaned_data.get("name") 
        user.save()

        email_html = render_to_string(
            "email_template.html",  
            {
                "name": user.name,  
                "login_url": self.request.build_absolute_uri(reverse_lazy("login")),
            }
        )
        email_text = strip_tags(email_html)

        # Criar e enviar o e-mail
        email = EmailMultiAlternatives(
            subject="Bem-vindo ao Nosso Sistema!",
            body=email_text,
            from_email="seuemail@gmail.com",
            to=[user.email],
        )
        email.attach_alternative(email_html, "text/html")
        email.send()

        messages.success(self.request, "Registro realizado com sucesso! Agora você pode fazer login.")
        return super().form_valid(form)




class CustomLogoutView(LogoutView):
    """Faz logout e redireciona para login com mensagem de sucesso."""
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "Você saiu com sucesso.")
        return redirect("login")


class MenuView(TemplateView):
    """Tela principal após login."""
    template_name = "menu.html"
