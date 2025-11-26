from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Member
from django.db.models import Q

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  try:
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
      'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
  except Member.DoesNotExist:
    template = loader.get_template('404.html')
    return HttpResponse(template.render({}, request), status=404)

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render({}, request))

def myfirst(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render({}, request))

def custom_404(request, exception=None):
  template = loader.get_template('404.html')
  return HttpResponse(template.render({}, request), status=404)

def testing(request):
  template = loader.get_template('template.html')
  record_firstname = Member.objects.filter(firstname='Andres').values()
  record_AND_andres =Member.objects.filter(firstname='Andres', id=14).values()
  record_OR_andres = Member.objects.filter(Q(firstname='Andres') | Q(firstname='Sofia')).values()
  record_like_start = Member.objects.filter(firstname__startswith='An').values()
  record_like_end = Member.objects.filter(firstname__endswith='res').values()
  record_like_contains = Member.objects.filter(firstname__contains='re').values()
  record_range = Member.objects.filter(id__range=(2,4)).values()
  record_exact = Member.objects.filter(firstname='Andres').values()
  orderby_asc = Member.objects.order_by('firstname')
  orderby_desc = Member.objects.order_by('-firstname')
  context = {
    'record_firstname': record_firstname,
    'record_AND_andres': record_AND_andres,
    'record_OR_andres': record_OR_andres,
    'record_like_start': record_like_start,
    'record_like_end': record_like_end,
    'record_like_contains': record_like_contains,
    'record_range': record_range,
    'record_exact': record_exact,
    'orderby_asc': orderby_asc,
    'orderby_desc': orderby_desc,
  }
  return HttpResponse(template.render(context, request))