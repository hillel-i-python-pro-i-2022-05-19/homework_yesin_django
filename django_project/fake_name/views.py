from django.http import HttpResponse

from .utils import list_fake


def generated(request, amount: int = 100):
    with_fake = list_fake(amount=amount)
    return HttpResponse(f'{with_fake}')
