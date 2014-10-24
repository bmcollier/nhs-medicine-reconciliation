from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from core.forms import LoginForm, UnlockForm
from core.models import NfcUser

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
                        reverse('core_home')
                        )

                else:
                    error_message = "This account is disabled."
            
        error_message = "Invalid login details provided."

    else: # GET

        # HACK: Suitable for NFC demo only.
        # Check if the NFC token has been supplied as a URL parameter. If it 
        # has, authenticate using this.
        nfc_token = request.GET.get('nfc_token')
        if nfc_token is not None:
            user = authenticate(nfc_token=nfc_token)
            login(request, user)

            return HttpResponseRedirect(
                reverse('core_home')
                )

        else:
            login_form = LoginForm()

    return render_to_response(
        'login.html',
        context_instance=RequestContext(
            request,
            {'login_form': login_form, 'error_message': error_message}
            )
        )

def do_unlock(request, nfc_token):
    nfcuser = get_object_or_404(NfcUser, nfc_login_id=nfc_token)

    error_message = u""
    if request.method == 'POST':
        unlock_form = UnlockForm(request.POST)
        if unlock_form.is_valid():
            pin = request.POST['pin']
            user = authenticate(nfc_token=nfc_token, pin=pin)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    
                    return HttpResponseRedirect(
                        reverse('core_home')
                        )

                else:
                    error_message = "This account is disabled."
            
        error_message = "Invalid login details provided."

    else:
        unlock_form = UnlockForm()

    return render_to_response(
        'login.html',
        context_instance=RequestContext(
            request,
            {'unlock_form': unlock_form, 'error_message': error_message,
            'nfcuser': nfcuser}
            )
        )

@login_required
def do_logout(request):
    """Logs out user"""
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required
def home(request):

    return render_to_response(
        'home.html',
        context_instance=RequestContext(request,
            {'show_admin': settings.SHOW_ADMIN_ON_HOME}
            )
        )

@login_required
def dashboard(request):
    return render_to_response(
        'dashboard.html',
        context_instance=RequestContext(request,)
        )

@login_required
def user_settings(request):
    return render_to_response(
        'settings.html',
        context_instance=RequestContext(request,)
        )