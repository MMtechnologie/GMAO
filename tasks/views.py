from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.utils.html import escape
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate

from tasks.models import Machine
from tasks.models import Panne


# Create your views here.
@login_required(login_url="/login")
def index(request):
    context = {}
    context["machines"] = Machine.objects.order_by("name")

    return render(request, 'tasks/index.html', context=context)


def login_view(request):
    return render(request, 'registration/login.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm(request.POST)
    return render(request, 'registration/sign_up.html', {"form": form})

@login_required(login_url="/login")
def add_machine(request):
    machine_name = escape(request.POST.get("machine-name"))
    machine, created = Machine.objects.get_or_create(name=machine_name)
    if not created:
        return HttpResponse("La Machine existe déja")
    # print(request.POST)

    return redirect('machines')

@login_required(login_url="/login")
def add_panne(request):
    # panne_name = escape(request.POST.get("panne-name"))
    panne_description = escape(request.POST.get("panne-description"))

    # Récupération du nom de la machine en panne
    name_machine = escape(request.POST.get("panne-machine"))
    print(name_machine)
    # Vérification de l'existance de cette machine
    if name_machine is not None:
        try:
            machine = Machine.objects.get(name=name_machine)
            # Création d'une nouvelle instance de l'objet Panne en lui assignant l'instance de la machine
            panne = Panne.objects.create(machine=machine, description=panne_description, time=timezone.now)
            # Redirection vers une page de confirmation ou de détails
            return redirect('pannes')
        except Machine.DoesNotExist:
            # Retourner une erreur ou une réponse de validation
            return HttpResponse("La machine avec le nom spécifié n'existe pas.")
    else:
        # Retourner une erreur ou une réponse de validation
        return HttpResponse("Le nom de la machine n'a pas été spécifié.")

@login_required(login_url="/login")
def machine_list(request):
    machines = Machine.objects.all()
    return render(request, 'machine_list.html', {'machines': machines})

@login_required(login_url="/login")
def panne_list(request):
    pannes = Panne.objects.all()
    machines = Machine.objects.all()
    return render(request, 'panne_list.html', {'pannes': pannes, 'machines': machines})

@login_required(login_url="/login")
def delete_panne(request, pk):
    panne = get_object_or_404(Panne, pk=pk)
    if request.method == 'POST':
        panne.delete()
        return redirect('pannes')
    return render(request, 'delete_panne.html', {'panne': panne})

@login_required(login_url="/login")
def update_panne(request, pk):
    panne = get_object_or_404(Panne, id=pk)
    if request.method == 'POST':
        if panne.state == 'active':
            panne.state = 'resolved'
        else:
            panne.state = 'active'
        panne.save()
        return redirect('pannes')
    return render(request, 'update_panne.html', {'panne': panne})
