from django.shortcuts import render
from testApp import forms

# Create your views here.
def studentView(request):

    form = forms.StudentForm()

    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('data inserted')

    return render(request, 'testApp/register.html', {'form' : form})
