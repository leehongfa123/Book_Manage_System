from django.shortcuts import render,reverse,redirect,HttpResponse
import copy
# Create your views here.
from Author_manager.models import *


def book_home(request):
    return render(request, "Book_manager/book_home.html")


def all_books(request):
    books = Book.objects.all()
    print(books)
    return render(request, "Book_manager/all_books.html", {"books":books})

def add_book(request):
    '''
    添加书籍
    :param request:
    :return:
    '''

    author_list = Author.objects.all()
    publish_list = Publish.objects.all()

    if request.method == 'GET':
        return render(request, "Book_manager/add_book.html",{"author_list":author_list,"publish_list":publish_list})
    else:


        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish')
        authors_id_list = request.POST.getlist('author')
        book = Book.objects.create(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
        book.author.add(*authors_id_list)
        return redirect(reverse('all_books'))

def del_book(request, del_book_id):

    Book.objects.filter(nid=del_book_id).delete()

    return redirect(reverse('all_books'))

def edit_book(request, edit_book_id):


    if request.method == 'GET':
        now_book = Book.objects.get(nid=edit_book_id)
        author_list = Author.objects.all()
        publish_list = Publish.objects.all()

        return render(request, "Book_manager/edit_book.html", {"now_book":now_book, "author_list":author_list, "publish_list":publish_list})
    else:

        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish')
        authors_id_list = request.POST.getlist('author')

        book =Book.objects.filter(nid= edit_book_id).update(title=title, price=price, pub_date=pub_date, publish_id=publish_id)
        Book.objects.get(nid=edit_book_id).author.set(authors_id_list)
        return redirect(reverse('all_books'))


def find_books(request):
    author_list = Author.objects.all()
    publish_list = Publish.objects.all()

    if request.method == "GET":
        return render(request, "Book_manager/booksinfo.html",{"author_list":author_list, "publish_list":publish_list})
    else:

        find_con = copy.deepcopy(request.POST.dict())
        del find_con['csrfmiddlewaretoken']


        book_con = {}
        author_id = None
        publish_id = None
        for key in find_con.keys():
            if not find_con[key]:
                pass
            elif key == 'publish':
                publish_id = int(find_con[key])
            elif key == 'author':
                author_id = int(find_con[key])
            else:
                book_con[key] = find_con[key]

        '''
        *************************************************
        
        下面是多表查询过程：
            1.首先通过作者，反向查询到所有书籍
            2.在通过出版社条件查询
            3.最后在通过书籍本身信息查询
        '''
        if author_id:
            author_con_res = Author.objects.get(nid=author_id).book_set.all()
        else:
            author_con_res = Book.objects.all()

        if publish_id:
            publish_con_res = author_con_res.filter(publish_id=publish_id)
        else:
            publish_con_res = author_con_res

        if book_con:
            find_res = publish_con_res.filter(**book_con)
        else:
            find_res = publish_con_res


        return render(request, "Book_manager/booksinfo.html", {"find_res": find_res,"author_list":author_list, "publish_list":publish_list})




