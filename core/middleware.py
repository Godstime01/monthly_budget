from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

class HasBudgetSession:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        

        # # if user has budget redirect to dashboard
        # if request.path == '/' and session_key:
        #     print('reach here====')
        #     return redirect('dashboard')

        response = self.get_response(request)
        return response
