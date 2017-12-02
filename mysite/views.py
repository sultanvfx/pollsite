from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
import datetime
from django.contrib import auth
from . import utilities


# Create your views here.

def fn_landing_page(request):
    """
    This View is called when the user opens the Website for the first time.
    :param request:
    :return:
    """
    return render(request, 'landing.html')


def fn_login_page(request):
    """
    This View is called when the user clicks the Login button.
    :param request:
    :return:
    """
    return render(request, 'login.html')
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = auth.authenticate(username=username, password=password)
#     if user is not None:
#         auth.login(request, user)
#         # return HttpResponseRedirect('/role_login/')
#         return render(request, 'poll/login.html')
#     else:
#         # return HttpResponseRedirect('/login/')
#         return render(request, 'poll/incorrect_login.html')


def fn_auth_view(request):
    """
    This View is called after user enters her/his login credentials.
    If login credentials are correct as per LDAP, then welcome.html page is shown.
    :param request:
    :return:
    """
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        response = HttpResponseRedirect('/welcome/')
        response.set_cookie('last_connection_time', datetime.datetime.now())
        response.set_cookie('username', username)
        request.session['username'] = username
        return response
    else:
        return HttpResponseRedirect('/sorry/')


def fn_welcome_page(request):
    """
    This View is called when login credentials are correct.
    This Vew prepares the Page to display Questions & select their appropriate answers.
    :param request:
    :return:
    """

    if 'username' not in request.session:
        return HttpResponseRedirect('/session_expired/')

    print "---welcome------: %s" % request.session['username']
    # get current username
    username = request.user.username

    # get ldap user infor
    ldap_user_info_list = utilities.get_user_info_from_ldap()

    # build submit dictionary
    submit_dict = dict()
    submit_dict['username'] = username
    submit_dict['ldap_user_info_dict_list'] = ldap_user_info_list
    # submit_dict['questions_dict'] = get_questions()
    # print 'Forwarding Questions: %s' % submit_dict['questions_dict']
    return render(request, 'welcome.html', submit_dict)


def fn_sorry_page(request):
    return render(request, 'incorrect_login.html')


def fn_session_expired(request):
    return render(request, 'session_expired.html')


def fn_logout_page(request):
    try:
        print 'Session Logout for: %s' % request.session['username']
        del request.session['username']
    except:
        pass
    return render(request, 'logout.html')

