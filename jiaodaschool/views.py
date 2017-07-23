# -*- coding: utf-8 -*-

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Examine, Student, Score


class ExmIndexView(generic.ListView):
    model = Examine
    template_name = 'jiaodaschool/exm_index.html'
    context_object_name = 'all_exam_list'

def exm_detail(request, exm_id):
    examine = get_object_or_404(Examine, pk=exm_id)
    score_set_sorted = sorted(examine.score_set.all(), key=lambda x:x.score, reverse=True)
    dct_stu_order = {}
    idx = 0
    last_score = 800.00
    last_idx = 1
    for score in score_set_sorted:
        idx += 1
        if abs(float(score.score) - last_score) < 0.001:
            dct_stu_order[score] = last_idx
            last_score = float(score.score)
        else:
            dct_stu_order[score] = idx
            last_idx = idx
            last_score = float(score.score)

    context = {'examine': examine, 'dct_stu_order': dct_stu_order}
    return render(request, 'jiaodaschool/exm_detail.html', context)


# Create your views here.
def index(request):
    return HttpResponse("Hello, this page is jiaodaschool index page.")
