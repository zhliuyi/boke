from django.http import HttpResponse
# return  HttpResponse('hello word')
from django.template import Template,Context
from django.shortcuts import render
from Article.models import *

from django.core.paginator import Paginator

def index(request):
    '''

   查询6条数据
   查询推荐的7条数据
   查询点击率排行榜的12条数据
    '''
    article=Article.objects.order_by("-date")[:6]
    recommend_article=Article.objects.order_by("-click")[:12]
    click_article=Article.objects.order_by("-click")[:12]
    # for i in article:
        # print(i.type)#Article.Type.None
        # print(i.type.first)
        # print(i.description)
    # print(article.date)
    return render(request,'index.html',locals())
def about(request):
    return render(request,'about.html')
def listpic(request):
    return render(request,'listpic.html')
def newslistpic(request,page=1):
    page=int(page)
    article=Article.objects.order_by("-date")
    paginator=Paginator(article,6)#每页显示6条数据
    page_obj=paginator.page(page)
    #获取当前页
    current_page=page_obj.number
    start=current_page-3
    if start<1:
        start=0
    end=current_page+2
    if end>paginator.num_pages:
        end=paginator.num_pages
    if start==0:
        end=5
    if end==paginator.num_pages:
        start=paginator.num_pages-5
    page_range=paginator.page_range[start:end]
    # print(article)
    return render(request,'newslistpic.html',locals())
def base(request):
    return render(request,'base.html')

def addarticle(request):
    for x in range(100):
        article=Article()
        article.title="title_%s"%x
        article.content="content_%s"%x
        article.description="description_%s"%x
        article.author=Author.objects.get(id=1)
        article.save()
        article.type.add(Type.objects.get(id=1))
        article.save()
    return HttpResponse('增加数据')
def articledetails(request,id):
    id=int(id)
    article=Article.objects.get(id=id)
    # print(article)
    paginator=Paginator(article,5)

    return render(request,'articledetails.html',locals())


def fytest(request):
    article=Article.objects.all().order_by("-date")
    print(article)
    return HttpResponse('分页测试')