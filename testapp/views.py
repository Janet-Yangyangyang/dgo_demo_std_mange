import json

from django.shortcuts import render, HttpResponse, redirect

from testapp.models import TestUser


# Create your views here.

def indx(request):
    return render(request, 'indx.html')


def info(request):
    return HttpResponse("Welcome to Janet's Demo")


def svt_cent(request):
    return HttpResponse("服务中心")


def prodls(request):
    title = "Products list"
    pls = ['SCMs', 'Customer_service_robots', 'AIAgents']
    time = [2019, 2021, 2025]
    prd_dic = {}
    prd_pack = []

    for i in range(len(pls)):
        prd_dic[pls[i]] = time[i]
        dc = {"prd": pls[i], 'ti': time[i]}
        prd_pack.append(dc)
    return render(
        request,
        'prodlist.html',
        {
            "title": title,
            "ls": pls,
            "tils": time,
            "pdic": prd_dic,
            "prd_pack": prd_pack
        }
    )


def usr_ls_orm(request):
    # create a new user
    # TestUser.objects.create(username='Jessica', pwd='123456')
    # TestUser.objects.filter(username='janet').delete()  # 删除数据库中重复的janet用户
    datalist = TestUser.objects.all()
    print('data_ls0:', datalist[0].username)                   # TestUser object (1)
    print('data_ls1:', datalist[0].__dict__)          # TestUser object (2)
    namelist = []
    for obj in datalist:
        # print(obj)              # TestUser object (1), TestUser object (2)
        # print(obj.username)     # janet, janet # 数据库里有两个重复的名字
        name = obj.username
        pwd = obj.pwd
        name_id = obj.id
        if name not in namelist:
            namelist.append(name)
        elif name in namelist:
            name_new = name+str(len(namelist))
            name.replace(name, name_new)
            TestUser.objects.filter(id=name_id).update(username=name_new)
            namelist.append(name_new)
            # return HttpResponse('已更新为：' + name_new)
        else:
            continue
    print('data_ls:', datalist)
    print('name_ls:', namelist)
    # res = str(namelist)
    return HttpResponse(datalist)




def prodadd(request):
    return render(request, 'prodadd.html')


def redir(request):
    url = "https://www.baidu.com"
    print(request.method)  # GET
    print(request.GET)  # <QueryDict: {}>
    print(request.POST)  # <QueryDict: {}>
    print(request.path)  # /test/baidu/
    print('environ info:', request.environ, '\n')
    print('accepted_types info:', request.accepted_types, '\n')
    print('encoding info:', request.encoding, '\n')
    # return redirect("https://www.baidu.com")
    return redirect(url)


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        print(request.POST)
        usr_nm = request.POST.get("username")
        pwd = request.POST.get("password")
        if usr_nm == "admin" and pwd == "123456":
            # return HttpResponse('login success')
            return redirect("/test/idx/")
        else:
            if usr_nm != "admin":
                return render(request, "login.html", {"error_msg": 404})
            # return HttpResponse('You\'re not authorized')
            if pwd != "123456":
                return render(request, "login.html", {"error_msg": 405})
