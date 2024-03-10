from django.http import HttpResponse
from random import randint, choice
import logging
from .models import CoinFlip
from django.shortcuts import render

logger = logging.getLogger(__name__)


def coin(request, amount_flips):
    result = choice(('Head', 'Tails'))
    logger.info(result)
    CoinFlip(side=result).save()
    last_results = CoinFlip.get_last_flips(amount_flips)
    context = {
        'current_flip': result,
        'last_results': last_results
    }
    return render(request, 'coin.html', context)


def dice(request):
    count = randint(1, 6)
    logger.debug(count)

    return HttpResponse(f'{count}')


def hundred(request):
    count = randint(1, 100)
    logger.debug(count)
    return HttpResponse(f'{count}')




# Create your views here.
