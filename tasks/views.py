from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.html import escape

from tasks.models import Machine
from tasks.models import Panne


# Create your views here.
def index(request):
    context = {}
    context["machines"] = Machine.objects.order_by("name")

    return render(request, 'tasks/index.html', context=context)


def add_machine(request):
    machine_name = escape(request.POST.get("machine-name"))
    machine, created = Machine.objects.get_or_create(name=machine_name)
    if not created:
        return HttpResponse("La Machine existe déja")
    # print(request.POST)

    return redirect('machines')


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
            panne = Panne.objects.create(machine=machine, description=panne_description)
            # Redirection vers une page de confirmation ou de détails
            return redirect('pannes')
        except Machine.DoesNotExist:
            # Retourner une erreur ou une réponse de validation
            return HttpResponse("La machine avec le nom spécifié n'existe pas.")
    else:
        # Retourner une erreur ou une réponse de validation
        return HttpResponse("Le nom de la machine n'a pas été spécifié.")


def machine_list(request):
    machines = Machine.objects.all()
    return render(request, 'machine_list.html', {'machines': machines})


def panne_list(request):
    pannes = Panne.objects.all()
    machines = Machine.objects.all()
    return render(request, 'panne_list.html', {'pannes': pannes, 'machines': machines})
