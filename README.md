# Charlotte

## 1. 数据库以及库安装：
### 1.1 安装数据库
安装mysql,默认用户名密码:root/root，对应配置修改Charlotte下的setting.py的DATABASES。
### 1.2 安装库
安装python3.5,然后进入工程根目录，执行: 
    pip install -r requirements.txt

windows依赖VS编译工具，单独[安装](http://landinghub.visualstudio.com/visual-cpp-build-tools)

### 1.3 数据表
工程根目录下执行： 

        python manage.py makemigrations
        python manage.py migrate


## 2.爬取IP代理数据
cd 到 spiders/ProxyIp目录，命令行下执行：

        scrapy crawl xici

cd 到 spiders/tools目录，清晰有效ip数据：

        python proxyip.py

## 3.爬取[宁波楼盘信息]()http://newhouse.cnnbfdc.com)下的心楼盘信息
cd 到 spiders/newhouse目录，命令行下执行：
        
        scrapy crawl nbnewhouse
        
## 4. 运行api服务
根目录下执行：
    
    python manage.py runserver
    
api接口如下：

1. 获取新楼盘列表：api/newhouses/?page=2&page_size=5

    ```
    {
    "data": [
        {
            "id": 768,
            "name": "宁波金融服务中心北区E栋二期",
            "project_state": "现房状态",
            "address": "东至鼎泰路北至和济街南至规划路西至规划路",
            "districts": "江东区",
            "created": "2017-05-06T02:46:55.063256Z"
        },
        {
            "id": 1024,
            "name": "嘉恒广场(西区)",
            "project_state": "现房状态",
            "address": "江东区东部新城混合住用区C2-1地块",
            "districts": "江东区",
            "created": "2017-05-06T02:46:55.063256Z"
        }
    ],
    "page": 2,
    "total": 799
}
    ```
    
2. 获取楼盘详情：api/newhouses/256/

    ```
   {
    "id": 256,
    "name": "万科云鹭湾Ⅱ-6地块二期",
    "supervision_bank": "中国建设银行股份有限公司宁波江北支行",
    "supervision_acount": "33101983736050512431",
    "project_state": "期房状态",
    "address": "",
    "dev_company": "宁波江北万科置业有限公司",
    "license_authority": "",
    "sale_permit": "商品房预售许可证",
    "license_key": "2016",
    "online_saleable_area": "24198.74",
    "online_saleable_flats": "450.00",
    "saleable_area": "372.24",
    "saleable_flats": "29.00",
    "sold_area": "23826.50",
    "sold_flats": "421.00",
    "residential_area": "0.00",
    "residential_flats": "0.00",
    "sold_residential_area": "21188.42",
    "sold_residential_flats": "214.00",
    "reserve_area": "0.00",
    "reserve_flats": "0.00",
    "saleable_parking_amount": "0.00",
    "saleable_garage_amount": "29.00",
    "sold_avg_price": "12234.12",
    "districts": "江北慈城",
    "contact_phone": "",
    "remark": "",
    "created": "2017-05-06T02:46:55.063256Z"
}
    ```

## 5. 搜索引擎

1. 启动ElasticSearch
2. 启动redis
3.  http://127.0.0.1:8000/search/
