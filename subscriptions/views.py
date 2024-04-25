from django.shortcuts import render
from django.conf import settings


from subscriptions.models import Packets
# from subscriptions.models import UserSubscriptions


def index(request):

    product = Packets.objects.all()
    context = {"product": product}
    return render(request, 'subscriptions/index.html', context)
