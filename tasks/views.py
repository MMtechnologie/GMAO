from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.html import escape

from tasks.models import Machine


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

    return redirect('home')
