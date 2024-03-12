from django.http import HttpResponse
from random import randint, choice
import logging
from .models import CoinFlip
from django.shortcuts import render

logger = logging.getLogger(__name__)


def coin(request, amount_flips):

    # logger.info(result)
    #
    results = [choice(('Head', 'Tails')) for _ in range(amount_flips)]
    context = {
        'title': 'Монетка',
        'results': results
    }
    return render(request, 'dice/result.html', context)


def dice(request, amount_flips):
    results = [randint(1, 6) for _ in range(amount_flips)]

    # logger.debug(count)
    context = {'title': 'Кости', 'results': results}
    return render(request, 'dice/result.html', context)


def hundred(request, amount_gens):
    results = [randint(1, 100) for _ in range(amount_gens)]
    # logger.debug(count)
    context = {'title': 'Волшебная сотня', 'results': results}
    return render(request, 'dice/result.html', context)

# Create your views here.
