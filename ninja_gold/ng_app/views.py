from django.shortcuts import render, redirect, HttpResponse
from time import strftime, localtime
import random


# Create your views here.
def index(request):
    date = strftime("%B %d, %Y", localtime())
    time = strftime("%I:%M:%S %p", localtime())
    if 'moves' not in request.session:
        request.session['moves'] = 0
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = ''
    request.session['moves'] -= 1
    if 'farm' in request.GET:
        farm_wage =  random.randrange(10,21)
        request.session['gold'] += farm_wage
        request.session['activity'] += f"By the sweat of your brow and stench of manure, you earned {farm_wage} gold. {date} {time} \n"
    if 'house' in request.GET:
        house_wage = random.randrange(2,6)
        request.session['gold'] += house_wage
        request.session['activity'] += f"You scrub your neighbors' floors until your knuckles bleed and earned {house_wage} gold. {date} {time} \n"
    if 'cave' in request.GET:
        cave_wage = random.randrange(5,11)
        request.session['gold'] += cave_wage
        request.session['activity'] += f"You bravely venture into the goblin's cave and find a few coins worth {cave_wage} gold. {date} {time} \n"
    if 'casino' in request.GET:
        coin = random.randrange(1,5)
        casino_wage = random.randrange(0,51)
        if coin == 2:
            request.session['gold'] += casino_wage
            request.session['activity'] += f"You actually chose the correct number in roulette! You win {casino_wage} gold! {date} {time} \n"
        else:
            request.session['gold'] -= casino_wage
            request.session['activity'] += f"Your luck is terrible at the craps table and you lost {casino_wage} gold! {date} {time} \n"
    return render(request, 'index.html')

def start_game(request):
    request.session.flush()
    moves = int(request.POST['moves'])
    winning_amount = int(request.POST['winning_amount'])
    request.session['moves'] = moves +1
    request.session['winning_amount'] = winning_amount
    return redirect('/')

def new_game(request):
    request.session.flush()
    return redirect('/')