from django.shortcuts import render,redirect
from django.urls import reverse

# Create your views here.

def start(request):
    if request.method=='POST':
        request.session['moves']=request.POST.get('moves')
        request.session['gold_num']=request.POST.get('gold_count')
    return redirect(reverse('index'))

def index(request):
    massage=''
    # request.session['gold_num']=0
    # request.session['moves']=0
    #return redirect(reverse('index'))
    if 'gold' not in request.session:
        request.session['moves']=0
        request.session['gold_num']=0
        request.session['gold']=0
        request.session['activities']=[]
    elif int(request.session['gold_num'])==request.session['gold'] and int(request.session['moves'])>=len(request.session['activities']):
        massage='You win!'
    elif int(request.session['moves'])<=len(request.session['activities']):
        massage='You lose!'

    context= {
        'forms':['Farm','Cave','House'],
        'Quest':'Quest',
        'moves':request.session['moves'],
        'goal':request.session['gold_num'],
        'gold':request.session['gold'],
        'activities':request.session['activities'],
        'massage':massage,
        'your_moves':len(request.session['activities'])
    }
    return render(request,'index.html',context)

import random 	 
import datetime

# using form method
# def process_money(request):
#     process=request.POST['process']
#     if process == 'Quest':
#         money=random.randint(0, 50)
#         if random.random()>0.5:
#             request.session['gold']+= money 
#             item=f'You completed a quest and earnd {money} gold. {datetime.datetime.now()}'
#             request.session['activities'].append([item,'green'])
#         else:
#             request.session['gold']-= money 
#             item=f'You faild a quest and lost {money} gold. {datetime.datetime.now()}'
#             request.session['activities'].append([item,'red'])

#     else:
#         money=random.randint(10, 20)
#         request.session['gold']+=money
#         item=f'You entered a {process} and earned {money} gold. {datetime.datetime.now()}'
#         request.session['activities'].append([item,'green'])
#     return redirect('/')

from datetime import datetime as dt

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

def process_money(request,process):

    if process == 'Quest':
        money=random.randint(0, 50)
        if random.random()>0.5:
            request.session['gold']+= money 
            item=f"You completed a quest and earnd {money} gold. {custom_strftime('%B {S}, %Y %I:%M %p' , dt.now())}"
            request.session['activities'].append([item,'green'])
        else:
            request.session['gold']-= money 
            item=f'You faild a quest and lost {money} gold. {custom_strftime("%B {S}, %Y %I:%M %p" , dt.now())}'
            request.session['activities'].append([item,'red'])
    else:
        money=random.randint(10, 20)
        request.session['gold']+=money
        item=f'You entered a {process} and earned {money} gold. {custom_strftime("%B {S}, %Y %I:%M %p" , dt.now())}'
        request.session['activities'].append([item,'green'])
    return redirect(reverse('index'))

def destroy(request):
    try:
        for key in list(request.session.keys()):
            if not key.startswith("_"): # skip keys set by the django system
                del request.session[key]
    except KeyError:
        pass
    return redirect(reverse('index'))