from django.shortcuts import render,reverse,redirect,HttpResponse
import copy
# Create your views here.
from Author_manager.models import *

def publish_home(request):
    return render(request, "publish_manager/publish_home.html")

def all_publishs(request):

    publshs = Publish.objects.all()
    print(publshs)

    return render(request, "publish_manager/all_publishs.html", locals())


def add_publish(request):
    '''
    实现作者添加
    请求为get时，返回添加叶片
    请求为post时，修改数据库记录
    :param request:
    :return:
    '''
    if request.method == "GET":
        return render(request, "publish_manager/add_publish.html")
    else:

        data = copy.deepcopy(request.POST).dict()
        del data['csrfmiddlewaretoken']

        Publish.objects.create(**data)
        return redirect(reverse('all_publishs'))

def del_publish(request, del_publish_id):
    Publish.objects.get(nid=del_publish_id).delete()
    return render(request, "publish_manager/all_publishs.html")

def edit_publish(request, edit_publish_id):



    if request.method == 'GET':
        now_publish = Publish.objects.get(nid=edit_publish_id)
        return render(request, "publish_manager/edit_publish.html",{"now_publish":now_publish})
    else:

        data = copy.deepcopy(request.POST).dict()
        del data['csrfmiddlewaretoken']

        Publish.objects.filter(nid=edit_publish_id).update(**data)
        return redirect(reverse('all_publishs'))



def find_publish(request):

    if request.method == "GET":
        return render(request, "publish_manager/publishinfo.html")
    else:
        find_con = copy.deepcopy(request.POST.dict())
        del find_con['csrfmiddlewaretoken']


        find_con_tmp = {}
        for key in find_con.keys():
            if not find_con[key]:
                pass
            else:
                find_con_tmp[key] = find_con[key]


        find_res = Publish.objects.filter(**find_con_tmp)


        return render(request, "author_manager/authorinfo.html", {"find_res": find_res})




