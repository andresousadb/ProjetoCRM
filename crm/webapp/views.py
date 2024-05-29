from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages


# - Homepage

def home(request):
    return render(request, 'index.html')


# - Register a user

def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Voluntário criado(a) com sucesso!!")

            return redirect("my-login")

    context = {'form': form}

    return render(request, 'register.html', context=context)


# - Login a user

def my_login(request):
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'form': form}

    return render(request, 'my-login.html', context=context)


# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):
    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'dashboard.html', context=context)


# - Create a record


@login_required(login_url='my-login')
def create_record(request):
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.usuario = request.user
            new_record.save()
            messages.success(request, "Visitante Cadastrado")
            return redirect("dashboard")
    else:
        form = CreateRecordForm()

    context = {'form': form}
    return render(request, 'cadastro_visitantes.html', context=context)




# - Update a record

@login_required(login_url='my-login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()

            messages.success(request, "Alterado com Sucesso !")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'alterar_registros.html', context=context)


# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):
    all_records = Record.objects.get(id=pk)

    context = {'record': all_records}

    return render(request, 'visualizar.html', context=context)


# - Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Registro Apagado !")

    return redirect("dashboard")


# - User logout

def user_logout(request):
    auth.logout(request)

    messages.success(request, "Saiu com Sucesso!")

    return redirect("my-login")


def visitantes(request):
    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Visitante Cadastrado!")

            return redirect('')

    context = {'form': form}

    return render(request, 'cadastro_visitantes.html', context=context)
