from django.http import HttpResponse
from random import randint, choice
import logging
from .models import CoinFlip
from django.shortcuts import render
from .forms import DiceForm

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

def result(request):

    func={"Coin": coin, "Dice": dice, "Hundred": hundred}

    if request.method == 'POST':
        form = DiceForm(request.POST)
        if form.is_valid():
            method = form.cleaned_data['method']
            count = form.cleaned_data['count']
        #METHOD_CHOICES = (('Coin', 'Монета'), ('Dice', 'Кубик'), ('Hunnred', 'Случайное число до 100'))
            return func[method](request, count)
    else:
        form = DiceForm()
    return render(request, 'dice/result.html', {'form':form})

