from django.shortcuts import render

from subscriptions.models import Packets


def index(request):

    product = Packets.objects.all()
    context = {"product": product}
    return render(request, 'subscriptions/index.html', context)
