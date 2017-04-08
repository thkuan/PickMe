import random
import unicodecsv
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET, require_POST
from .models import Member, History

# Create your views here.
def index(request):
    return render(request, 'polls/home.html')

@require_POST
def draw(request):
    ALLON = False
    group_var = request.POST.get('group_name', 'ALL')
    if ALLON:
        if group_var == 'ALL':
            valid_members = Member.objects.filter(drawn=False)
        else :
            valid_members = Member.objects.filter(group_name=group_var, drawn=False)
    else:
        valid_members = Member.objects.filter(group_name='PM', drawn=False)

    # Draw the lucky one
    if not valid_members.exists():
        ## Raise 404 if no members are found given the group name
        ##raise Http404("No member in group '%s'" % group_var)
        lucky_member = []
        return render(request, 'polls/show.html',
            {'lucky_draw': lucky_member,}
        )
    else :
        #tmp = []
        #for obj in valid_members:
        #    tmp.append("<p>{0.employee_id} {0.ch_name} {0.name} ({0.group_name})</p>".format(obj))
        #return HttpResponse(
        #    tmp
        #)

        # Draw the lucky one
        lucky_member = random.choice(valid_members)
        
        # Update the lucky guy to avoid next pick
        Member.objects.filter(id=lucky_member.id).update(drawn=True)

        # Update history
        draw_history = History(member=lucky_member)
        draw_history.save()

    return render(request, 'polls/show.html',
        {'lucky_draw': lucky_member,}
    )

def history(request):
    recent_draws = History.objects.order_by('-time').all()[:10]
    return render(request, 'polls/history.html',
        {'recent_histories': recent_draws,}
    )

def reset(request):
    # <TODO> This fuction should be raised to admin level that avoid others clean database
    Member.objects.update(drawn=False)
    history_list = History.objects.all()
    if history_list.exists():
        history_list.delete()
    return render(request, 'polls/home.html')

'''
def add_csv(request):
    EASYGEN = True
    if EASYGEN:
        # <TODO> This fuction should be raised to adminlevel that avoid others insert to database
        with open('./data_utf8.csv', 'r') as fid:
            csv_reader = unicodecsv.DictReader(fid, encoding='utf-8-sig')
            members = [
                (row['grouping'], row['level'], row['employee_id'], row['ch_name'], row['en_name'], row['extension'], row['group_name'], row['drawn']) for row in csv_reader
            ]
        fid.close()
        for m in members:
            Member(name=m[4], ch_name=m[3], group_name=m[0], extension=m[5], department=m[6]).save()
        return render(request, 'polls/home.html')
    else:
        #return HttpResponse("Please contact admin!!")
        return render(request, 'polls/home.html')
'''

