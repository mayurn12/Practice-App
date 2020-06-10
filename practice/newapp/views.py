from django.shortcuts import render, redirect
from .forms import formNew
from django.contrib.auth.decorators import login_required
from newapp.models import FormModel
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

def home(request):
    return render(request,'newapp/home.html')


#Create Functionality
@login_required
def addname(request):
    form = formNew(request.POST or None)
        
    if form.is_valid():
        form.save()
        return redirect('namelist')

    return render(request,"newapp/addname.html",{'form':form})

class CreateName(CreateView):
    model = FormModel;
    fields=['first_name','last_name','email','phone']
    template_name = 'newapp/addname.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

#List view Functonality
@login_required
def namelist(request):
    name = FormModel.objects.all()
    name_name = request.GET.get('name_name')
    if name_name != '' and name_name is not None:
        name = name.filter(first_name__icontains=name_name)
    return render(request,'newapp/namelist.html',{'name':name})

#Details Functonality
@login_required
def detailsview(request,id):
    names = FormModel.objects.get(id=id)
    return render(request,"newapp/details.html",{"names":names})

class DetailsNameView(DetailView):
    model = FormModel
    template_name = 'newapp/details.html'
    context_object_name = 'names'

#Upadate Functonality
@login_required
def updatename(request,id):
    name = FormModel.objects.get(id=id)
    form = formNew(request.POST or None, instance=name)

    if form.is_valid():
        form.save()
        return redirect ('namelist')
    return render(request,'newapp/addname.html',{'form':form,'name':name})
#delete Functonality
@login_required
def deletename(request,id):
    name = FormModel.objects.get(id=id)

    if request.method == 'POST':
        name.delete()
        return redirect('namelist')
    return render(request,'newapp/delete.html',{'name':name})
