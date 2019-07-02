from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Termin
from .forms import CreatTermin
from django.shortcuts import get_object_or_404


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('user_name')
            messages.success(request, f'Account created')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

def termin_list_view(request):
    return render(request, 'users/terminy.html', {
        'terminy': Termin.objects.filter(author=request.user)
    })

def termin_detail_view(request):
    return render(request, 'users/terminy.html', {
        'terminy': Termin.objects.filter(author=request.user)
    })

def termin_delete(request, pk):
    termin = get_object_or_404(Termin, pk=pk)
    if request.method == 'POST':
        termin.delete()
        return redirect(request, 'users/terminy.html')
    context = {
        't': termin
    }
    return redirect(request, 'users/terminy.html', context)

# def termin_delete(request, pk):
#     try:
#         termin = Termin.objects.get(pk=pk).delete()
#     except Termin.DoesNotExist:
#         print("no such object")
#         return redirect('users/terminy.html')
#     return redirect(request, 'users/terminy.html')

def termin_create_view(request):
    form_class = CreatTermin
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = CreatTermin(request.POST)
        if form.is_valid():
            termin = Termin(
                author = request.user,
                date = form.cleaned_data['date'],
                mobile_number = form.cleaned_data['mobile_number'],
                status = form.cleaned_data['status'],
                price = form.cleaned_data['price']
            )
            termin.save()
            return redirect('/terminy')
    return render(request, 'users/terminy_form.html', {
        'form': form
    })


def termin_update_view(request, pk):
    try:
        termin = Termin.objects.get(pk=pk, author=request.user)
    except Termin.DoesNotExist:
        print("no such object")
        return redirect('/terminy')
    return render(request, 'users/update_termin.html', {
        't': termin
    })

def termin_edit(request, pk):
    termin = get_object_or_404(Termin, pk=pk)
    if request.method == "POST":
        form = CreatTermin(request.POST, instance=termin)
        if form.is_valid():
                author=request.user,
                mobile_number=form.cleaned_data['mobile_number'],
                status=form.cleaned_data['status'],
                price=form.cleaned_data['price'],
                termin.save(),
                return redirect('/terminy')
    else:
        form = CreatTermin(instance=termin)
    return render(request, 'users/update_termin.html', {'form': form})


