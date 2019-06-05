from django.shortcuts import render
from django.db.models import Count, Sum
from .models import Project

# Create your views here.

def prov_list(request):

    prov_list = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK']
    print(prov_list)
    print("Hello its here")
    context = {
    'data': prov_list
    }
    return render(request,'tabs.html', context)


def top_inst_view(request):
    prov_list = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK']
  #   obj = Project.objects.filter(province__contains="AB").values('institution') \
  # .annotate(total_fund=Sum('fund')) \
  # .order_by('-total_fund')
    AB = Project.objects.filter(province__contains="AB").values('institution') \
  .annotate(total_fund=Sum('fund')) \
  .order_by('-total_fund')
    AB_projects = Project.objects.filter(province__exact='AB').values_list('province').annotate(Count('province'))[0][1] 
    AB_fund = Project.objects.values('fund').annotate(total_fund=Sum('fund'))
   
    context = {
        'AB': AB,
        'AB_projects': AB_projects,
        'AB_fund': AB_fund,
        'list': prov_list,
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
