#!/usr/bin/env python3
from django.shortcuts import render, get_object_or_404
from .models import Puzzles
from django.http import HttpResponse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'puzzles/index.html'
    context_object_name = 'latest_puzzles_list'
    
    def get_queryset(self):
        """Return the last five published puzzles."""
        return Puzzles.objects.order_by('-puzzleid')[:10]

class DetailView(generic.DetailView):
    model = Puzzles
    template_name = 'puzzles/detail.html'

def index(request):
    latest_puzzles_list = Puzzles.objects.order_by('-puzzleid')[:5]
#    output = ', '.join([p.task for p in latest_puzzle_list])
    context = {'latest_puzzles_list': latest_puzzles_list}
    return render(request, "puzzles/index.html", context)
    
def detail(request, puzzleid):
    puzzle = get_object_or_404(Puzzles,pk=puzzleid)
    return render(request, 'puzzles/detail.html', {'puzzle': puzzle})
    
def results(request, puzzleid):
    response = "You're looking at the results of puzzle %s."
    return HttpResponse(response % puzzleid)

def vote(request, puzzleid):
    return HttpResponse("You're voting on puzzle %s." % puzzleid)
    
    
"""
class Puzzles(models.Model):
    puzzleid = models.AutoField(primary_key=True)
    puzzledata = models.ImageField()
    picture = models.ForeignKey(Pictures, models.DO_NOTHING, db_column='picture')
    groupid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='groupid')
    zone = models.IntegerField()
    complexity = models.ForeignKey(Complexity, models.DO_NOTHING, db_column='complexity')
    task = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    icon = models.ImageField()
"""