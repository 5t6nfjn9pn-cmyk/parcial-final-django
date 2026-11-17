from django.shortcuts import render, redirect
from .forms import ProgramaForm
from .models import Programa


def crear_programa(request):
    if request.method == "POST":
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("crear_programa")
    else:
        form = ProgramaForm()
    programas = Programa.objects.all().order_by("id")
    return render(request, "myapp/programa_form.html", {"form": form, "programas": programas})
