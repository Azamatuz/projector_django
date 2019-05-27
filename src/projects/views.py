from django.shortcuts import render
from django.db.models import Count, Sum
from .models import Project

# Create your views here.

def top_inst_view(request):
    obj = Project.objects.filter(province__contains='AB').values('institution') \
  .annotate(total_fund=Sum('fund')) \
  .order_by('-total_fund')
    context = {
        'data': obj,
        # Project.objects.filter(province__contains=prov),
        # 'province'    : province.values('sector').annotate(dcount=Count('sector')),
        # 'institution' : obj.institution,
        # 'leader'      : obj.leader,
        # 'fund'        : obj.fund,
        # 'date'        : obj.date,
        # 'keywords'    : obj.keywords,
        # 'sector'      : obj.sector,
        # 'discipline'  : obj.discipline,
        # 'year'        : obj.year
    }
    return render(request, 'province.html', context)
