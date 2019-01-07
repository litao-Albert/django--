"""
分页逻辑：
每页4条数据，每次查询5页，一次一共查询20条数据
第一页 0-4
第二页 5-8
第三页 9-12
第四页 13-16
第五页 17-20
以上得findindex=1
第六页带到第十页，findindex=2
当我findindex=1 查询得索引[0-20]
起始0 (findindex-1)*20
结束20 (findindex)*20
"""
# 分页逻辑代码
da_data= list(range(1,100))
one_page_num = 4 # 每页显示4条数据
one_time_num = 5 # 每次查询5页

while True:
    page = int(input("page>>>")) #输入页码
    # page=1 findindex=1 int(1/5)+1
    # page=2 findindex=1
    # page=3 findindex=1
    # page=4 findindex=1
    # page=5 findindex=1
    # page=6 findindex=2  int(6/5)+1
    # page=7 findindex=2
    if page/one_time_num>int(page/one_time_num):
        findindex = int(page/one_time_num)+1
    else:
        findindex = int(page/one_time_num)

    #第一次查询，每次查询5页，每页4条数据
    select_num = one_page_num * one_time_num #一次查询得总数居[1-20][21-40]....
    select_start = (findindex-1)*select_num #开始查询得索引
    select_end= findindex*select_num #结束查询得索引
    select_data = da_data[select_start:select_end]
    #上面是查询到了20条数据

    #下面进行20条数据得截取
    #findindex=1时
    # page=1 pageindex=1
    # page=2 pageindex=2
    # page=3 pageindex=3
    # page=4 pageindex=4
    # page=5 pageindex=5
    # findindex=2时
    # page=6 pageindex=1
    # page=7 pageindex=2
    # page=8 pageindex=3
    # page=9 pageindex=4
    # page=10 pageindex=5

    # 设置截取得索引位
    now_index = page-(findindex-1)*one_time_num
    # 设置单页得截取开始和结束
    page_start = (now_index-1)*one_page_num
    page_end = now_index*one_page_num
    #开始截取
    page_data = select_data[page_start:page_end]
    print("+"*100)
    print("page:%s\t"%page)
    print("select_data:%s\t"%select_data)
    print("page_data:%s\t"%page_data)
    print("+" * 100)








