from django.http import HttpResponse
from PltyTest.models import Poll
from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import render_to_response,   get_object_or_404


def index(request):
        latest_poll_list = Poll.objects.all()
        t=loader.get_template('PltyTest/index.html')
        c=Context({'latest_poll_list': latest_poll_list})

        ###output=', '.join([p.question for p in latest_poll_list])
        return HttpResponse(t.render(c))

def detail(request,poll_id):
        p=get_object_or_404(Poll,pk=poll_id)
        return render_to_response('PltyTest/detail.html', {'poll':p}, context_instance=RequestContext(request))



def vote(request, poll_id):
        p=get_object_or_404(Poll,pk=poll_id)

        p.votes=request.POST['choice']
        p.save()

