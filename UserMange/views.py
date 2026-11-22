from django.shortcuts import render, HttpResponse, redirect

from UserMange.models import UserGroup, UserInfo

from django.utils import timezone


# Create your views here.


def user(request):
    return render(request, 'user.html', {"page_title": "User Management"})


def user_ls(request):
    users = UserInfo.objects.all()
    now = timezone.now()
    return render(
        request,
        'userls.html',
        {"users": users, "now": now, "page_title": "User List", "Username": "SuperAdmin"}
    )


def user_add(request):
    if request.method == "GET":
        return render(request, 'user_add.html', {"page_title": "Add User"})
    uname = request.POST.get("name")
    uag = request.POST.get("password")
    upw = request.POST.get("age")
    if not all([uname, uag, upw]):
        return HttpResponse("用户名、密码、年龄不能为空！")
    UserInfo.objects.create(uname=uname, pwd=upw, age=uag)
    # return redirect("http://127.0.0.1:8000/userm/usr/ls")
    '''
    假设当前：http://127.0.0.1:8000/userm/usr/ls/
    href写法	                    解析后的路径
    /usr/add/--根目录下绝对路径    /usr/add/
    usr/add/--当前直接拼	        /userm/usr/ls/usr/add/
    ../add/--和当前层平级	        /userm/usr/add/
    ./add/--当前链接后直接拼	    /userm/usr/ls/add/
    ../../add/--和上一级平级 	    /userm/add/
    '''
    return redirect("../ls/")


def user_del(request):
    usr_id = request.GET.get('nid')
    UserInfo.objects.filter(id=usr_id).delete()
    return redirect("../ls/")


def group_manage(request):
    grp_data = UserGroup.objects.all().order_by('id')
    return render(request, "group.html",
                  {"page_title": "Group Management", "username": "SuperAdmin", "grp_data": grp_data})


def group_add(request):
    if request.method == 'GET':
        return render(request, 'group_add.html', {"page_title": "Add Group"})
    gn = request.POST.get("gname_new")
    if not gn:
        return HttpResponse("组名不能为空！")
    UserGroup.objects.create(gname=gn)
    return redirect(request, "../")


def temp_view(request):
    return render(request, 'group.html', {"name": "张三", "age": 18, "gender": 1, "page_title": "Group List"})
