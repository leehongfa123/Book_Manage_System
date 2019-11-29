from django.shortcuts import render,reverse,redirect,HttpResponse
import copy
# Create your views here.
from Author_manager.models import *

def home(request):
    return render(request, "home.html")

def book(request):
    return render(request, "Book_manager/book_home.html")

def author(request):
    return render(request, "author_manager/author_home.html")

def all_authors(request):

    authors = Author.objects.all()
    author_details = Author_detail.objects.all()

    return render(request, "author_manager/all_authors.html", locals())

def add_author(request):
    '''
    实现作者添加
    请求为get时，返回添加叶片
    请求为post时，修改数据库记录
    :param request:
    :return:
    '''
    if request.method == "GET":
        return render(request, "author_manager/add_author.html")
    else:
        name = request.POST.get('name')
        age = request.POST.get('age')
        add = request.POST.get('add')
        tel = request.POST.get('tel')
        email = request.POST.get('email')

        # 先添加没有外键的详细信息表
        Author_detail.objects.create(addr=add, tel=tel)
        # 查找到对应的pk值
        detail_pk = Author_detail.objects.get(tel=tel).nid
        Author.objects.create(name=name, age=age, email=email, detail_id=detail_pk)
        return redirect(reverse('all_authors'))

def del_author(request, del_author_id):
    '''
    作者删除
    :param request:
    :param del_author_id:
    :return:
    '''

    Author.objects.get(nid=del_author_id).delete()

    return redirect(reverse('all_authors'))

    # return render(request, "book_home.html")


def edit_author(request, edit_author_id):
    '''
    作者信息编辑，也要分为get请求和post请求分别处理
    :param request:
    :param edit_author_id:
    :return:
    '''
    now_author = Author.objects.get(nid=edit_author_id)
    now_author_detail = now_author.detail
    if request.method == 'GET':

        return render(request, "author_manager/edit_author.html", locals())
    else:
        name = request.POST.get('name')
        print(name)
        age = request.POST.get('age')
        add = request.POST.get('add')
        tel = request.POST.get('tel')
        email = request.POST.get('email')



        # 根据接受到的数据，进行当前表的数据更新
        # 这里一定要注意：只有queryset类型的数据才可以调用update方法

        Author.objects.filter(nid=edit_author_id).update(name=name, age=age, email=email)
        Author_detail.objects.filter(pk = now_author.detail_id).update(addr=add, tel=tel)

        return redirect(reverse('all_authors'))

def find_author(request):

    if request.method == "GET":
        return render(request, "author_manager/authorinfo.html")
    else:


        find_con = copy.deepcopy(request.POST.dict())
        del find_con['csrfmiddlewaretoken']

        author_find_con_tep = {}
        author_detail_find_con_tep = {}

        for key in find_con.keys():
            if not find_con[key]:
                pass
            elif key in ['addr', 'tel']:
                author_detail_find_con_tep[key] = find_con[key]
            else:
                author_find_con_tep[key] = find_con[key]



        author_detail_find_res = Author_detail.objects.filter(**author_detail_find_con_tep)
        detaile_list = []
        for author_detail_item in author_detail_find_res:
            detaile_list.append(author_detail_item.nid)



        author_find_res = Author.objects.filter(**author_find_con_tep).filter(detail_id__in=detaile_list)

        return render(request, "author_manager/authorinfo.html", {"find_res": author_find_res})

def publish_home(request):
    return render(request, "publish_manager/publish_home.html")


