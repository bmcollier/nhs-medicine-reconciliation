from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from medchecker.forms import LoginForm

def do_login(request):
    error_message = u""
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                    return HttpResponseRedirect(
                        reverse('home')
                        )

                else:
                    error_message = "This account is disabled."
            
        error_message = "Invalid login details provided."

    else:
        login_form = LoginForm()

    return render_to_response(
        'login.html',
        context_instance=RequestContext(
            request,
            {'login_form': login_form, 'error_message': error_message}
            )
        )