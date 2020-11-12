from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
#from testappthree.forms import Form_Name(s)
#from testappthree.models import Model_Name(s)

#Remember to add LOGIN_URL = "/app_name/user_login" to settings.py if you are adding login

# Create your views here.

# def index(request):
#     return render(request, 'testappthree/index.html')

# def formview(request):
#     form = Form_Name()
#     if request.method == 'POST':
#         form = Form_Name(request.POST)

#         if form.is_valid():
#             form.save(commit = True)
#             return index(request)
#         else:
#             print('Error')

#     return render(request, 'testappthree/form_page.html', {'form':form})

# def modelview(request):
#     example_data = Model_Name.objects.all()
#     context_dict = {'data_list':example_data}
#     return render(request, 'testappthree/model_page.html', context = context_dict)