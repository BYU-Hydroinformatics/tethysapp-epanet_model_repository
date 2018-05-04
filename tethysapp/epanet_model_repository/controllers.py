from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {'modelType': request.GET.get('modelType', '')}

    return render(request, 'epanet_model_repository/home.html', context)
