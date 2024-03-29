import json
from .models import Item, List
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#
# def home(request):
#     return render_to_response("index.html",
#         None,
#         context_instance=RequestContext(request)
#     )
#

def home(request):
    return render_to_response("home.html",
        None,
        context_instance=RequestContext(request)
    )

def view_list(request, user_name, list_name):
#    import pdb; pdb.set_trace()
    user = get_or_create_user(user_name)
    list = get_or_create_list(user, list_name)

    user_lists = user.list_set.all().order_by('name')
    return render_to_response("list.html", {
            "list": list,
            "list_items": list.item_set.all(),
            "user_lists": user_lists
        }, context_instance=RequestContext(request))


def add_item(request, user_name, list_name, new_item):
    user = get_or_create_user(user_name)
    list = get_or_create_list(user, list_name)
    list.save()
    item = Item(name=new_item, order=list.item_set.count())
    item.list = list
    item.save()
    result = {"name": item.name, "pk": item.pk, "order": item.order}
    return HttpResponse(json.dumps(result))


@csrf_exempt
def move_item(request, pk, list_name, user_name):
    after = request.POST['order']
    item = Item.objects.get(pk=pk)
    item.move(after)
    result = {"name": item.name, "pk": item.pk, "order": item.order}
    return HttpResponse(json.dumps(result))


def remove_item(request, user_name, list_name, pk):
    item = Item.objects.get(pk=pk)
    if item:
        list = item.list
        item.delete()
        if list.item_set.count() == 0:
            list.delete()
        return HttpResponse(json.dumps({"status": "ok"}))
    else:
        return HttpResponse(json.dumps({"status": "fail"}))


@csrf_exempt
def update_item(request, user_name, list_name, pk):
    item = Item.objects.get(pk=pk)
    if Item:
        complete = request.POST['complete'] == "true"
        item.complete = complete
        item.save()
        return HttpResponse(json.dumps({"status": "ok"}))
    else:
        return HttpResponse(json.dumps({"status": "fail"}))


def clear_list(request, user_name, list_name):
    user = get_or_create_user(user_name)
    list = get_or_create_list(user, list_name)
    list.item_set.all().delete()
    list.delete()
    return HttpResponse(json.dumps({"status": "ok"}))


def get_or_create_user(user_name):
    user = User.objects.filter(username=user_name)
    if len(user) == 0:
        user = User.objects.create_user(user_name, 'test@test.com', 'xyzzy')
        user.save()
    else:
        user = user[0]
    return user


def get_or_create_list(user, list_name):
    existing_list = user.list_set.filter(name=list_name)
    if len(existing_list) == 1:
        list = existing_list[0]
    else:
        list = List(name=list_name)
        list.user = user
    return list
