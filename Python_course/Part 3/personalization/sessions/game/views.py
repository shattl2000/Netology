from random import randint

from django.conf import settings
from django.shortcuts import render, redirect

from .forms import GameForm
from .models import Player, Game


def get_player(request):
    player_id = request.session.get('player_id', None)
    if player_id:
        player = Player.objects.get(id=player_id)
        # players = Player.objects.filter(id=player_id)
        # if players.exists():
        #     player = players.last()
        # else:
        #     player = Player.objects.create()
        #     request.session['player_id'] = player.id
    else:
        player = Player.objects.create()
        request.session['player_id'] = player.id
    return player


def get_current_game(player):
    current_game = Game.objects.filter(player1=player).filter(is_over=True).\
            filter(player1_result_viewed=False).last()
    if current_game is not None:
        current_game.player1_result_viewed = True
        current_game.save()
    if current_game is None:
        current_game = Game.objects.filter(player1=player).filter(is_over=False).last()
    if current_game is None:
        current_game = Game.objects.filter(player2=player).filter(is_over=False).last()
    if current_game is None:
        current_game = Game.objects.filter(player2=None).filter(is_over=False).last()
        if current_game is not None:
            current_game.player2 = player
            current_game.save()
    if current_game is None:
        current_game = Game.objects.create(player1=player)
    return current_game


def game(request):
    player = get_player(request)
    current_game = get_current_game(player)
    is_first_player = True if player == current_game.player1 else False
    context = {}

    if not current_game.is_over:
        if is_first_player:
            if not current_game.correct_value:
                current_game.correct_value = randint(settings.GAME_MIN_VALUE, settings.GAME_MAX_VALUE)
                current_game.save()
            context.update({
                'is_first_player': is_first_player,
                'correct_value': current_game.correct_value,
            })
        else:
            current_value = None
            if request.method == 'POST':
                form = GameForm(request.POST)
                if form.is_valid():
                    current_value = form.cleaned_data['value']
            else:
                form = GameForm()
            # if form.is_valid():
            #     current_value = form.cleaned_data['value']
            context.update({'form': form,
                            'current_value': current_value})

            if current_value is not None:
                if current_value == current_game.correct_value:
                    current_game.is_over = True
                    current_game.is_value_found = True
                    current_game.player2_result_viewed = True
                    current_game.save()
                else:
                    if current_game.current_attempt + 1 > settings.GAME_MAX_ATTEMPTS:
                        current_game.is_over = True
                        current_game.is_value_found = False
                        current_game.player2_result_viewed = True
                        current_game.save()
                    else:
                        current_game.current_attempt += 1
                        current_game.save()
                        values_comparison = 'Загаданное число больше' if current_value < current_game.correct_value\
                            else 'Загаданное число меньше'
                        context['values_comparison'] = values_comparison
    context.update({
        'is_first_player': is_first_player,
        'game_is_over': current_game.is_over,
        'is_value_found': current_game.is_value_found,
        'attempts': current_game.current_attempt,
        'correct_value': current_game.correct_value
    })

    return render(request, 'game.html', context)
