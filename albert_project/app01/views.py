from django.shortcuts import render
from app01.models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"index.html",locals())
def myArticle(request):
    return  render(request,"myArticle.html")
def myPicture(request):
    return render(request,"mypicture.html")
def base(request):
    return  render(request,'base.html')
def aboutMe(request):
    return render(request,"aboutMe.html")
def Article_source(request):
    return render(request,"Article_source.html")

def vuetest(request):
    return render(request,"vuetest.html")
def vue(request):
    if request.method == "GET":
        page = request.GET.get("page") #尝试获取page得值
        if not page: #如果没有page
            page = 1 #将page的值默认设置为1
        else:
            page = int(page) #如果有page测取他得值
        articles = Article.objects.all()  # 查询文章数据库中所有得数据
        paginator = Paginator(articles,3) # 数据列队，查询出来得数据每页显示三条数据
        pageDate = paginator.page(page) # 单页数据
        page_date = []
        for data in pageDate:
            # clssify = data.clssify.all() #多对多字段首先查询出所有对应的字段,查询出来是对象
            # if clssify:
            #     clssify =[i.label for i in clssify]
            # else:
            #     clssify = "" #如果查询出来的数据为空是不可以建json序列
            page_date.append(
                {
                    "title":data.title,
                    "author":data.author.name,
                    "time":data.time,
                    "description":data.description,
                    "picture":data.picture.name,

                    "classify":data.clssify.label,
                    "id":data.id

                }
            )
        print(data.picture.name)
        print(data.author.name)
        print(data.clssify.label)
        result = {
            "pageData":page_date
        }
        return JsonResponse(result)

def setpage(page,one_time_num,one_page_num,db):
    """
    分页函数
    :param page:
    :param one_time_num:
    :param one_page_num:
    :param db:
    :return:
    """
    db_data = db.objects.all()
    if page/one_time_num > int(page/one_time_num):
        findindex = int(page/one_time_num)+1
    else:
        findindex = int(page/one_time_num)

    # 第一次查询，每次查询5页，每页4条数据
    select_num = one_page_num*one_time_num  # 一次查询得总数居[1-20][21-40]....
    select_start = (findindex-1) * select_num  # 开始查询得索引
    select_end = findindex*select_num  # 结束查询得索引
    select_data = db_data[select_start:select_end]
    # 设置截取得索引位
    now_index = page-(findindex-1)*one_time_num
    # 设置单页得截取开始和结束
    page_start = (now_index-1)*one_page_num
    page_end = now_index*one_page_num
    # 开始截取
    page_data = select_data[page_start:page_end]
    result = {
        "page":page,
        "page_data":page_data
    }
    #数据得总条数
    count = db.objects.count()
    #总页数
    final_page = count/one_page_num   # 总条数除以每一页得总数据
    #考虑是否能整除
    if final_page!=int(final_page):#如果我得总页数不能整除
        final_page +=1
    final_page = int(final_page)

    # 判断页码数
    islast = False
    if page > final_page:
        islast = True
    if page in [1,2,3]:
        prange_start = 1
        prange_end = 6
    else:
        prange_start = page - 2
        prange_end = page + 3
    prange = list(range(prange_start,prange_end))

    result["count"] = count
    result["islast"] = islast
    result["prange"] = prange

    return  result
def vuesource(request):
    if request.method == "GET": #判断是不是get请求
        page = request.GET.get("page") #获取我当前page页码，这里获取下来得是字符串
        if page and int(page)>1:  # 如果我获取到page数据，并且page大于1，也就是2，3，4，5
            page = int(page)
        else:
            page = 1
        one_page_num = 4 #每页显示4条数据
        one_time_num = 5 #每次查询5页
        reslut_list = []
        page_data = setpage(page,one_page_num,one_time_num,Article)  #得到函数中得返回值result result中有一个page_data4条数据
        datas = page_data.get("page_data")  #通过字典获取key 得方法获取查询出来得前四条数据
        print(datas)
        for data in datas:
            print(data)
            reslut_list.append({
                "title":data.title,
                "description":data.description,
                "picture":data.picture.name,
                "author":data.author.name,
                "id":data.id,
                "time":data.time
            })
            page_data["page_data"] = reslut_list
            return  JsonResponse(page_data)
        else:
            return JsonResponse({"error":"no data"})










