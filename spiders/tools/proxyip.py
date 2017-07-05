import requests
import random
try:
    from spiders.models import ProxyIp
except Exception as e:
    import sys
    import os
    import django

    sys.path.append('../../../Charlotte')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'Charlotte.settings'
    django.setup()
    from spiders.models import ProxyIp

class GetIP(object):

    def validate(self, ip, port):
        #判断ip是否可用
        http_url = "http://www.baidu.com"
        proxy_url = "http://{0}:{1}".format(ip, port)
        try:
            proxy_dict = {
                "http":proxy_url,
            }
            response = requests.get(http_url, proxies=proxy_dict)
        except Exception as e:
            return False
        else:
            code = response.status_code
            if code >= 200 and code < 300:
                return True
            else:
                return False

    def delete_ip(self, ip):
        #从数据库中删除无效的ip
        ProxyIp.objects.get(ip = ip).delete()
        return True

    def judge_ip(self, ip, port):
        #判断ip是否可用
        http_url = "http://www.baidu.com"
        proxy_url = "http://{0}:{1}".format(ip, port)
        try:
            proxy_dict = {
                "http":proxy_url,
            }
            response = requests.get(http_url, proxies=proxy_dict)
        except Exception as e:
            print ("invalid ip and port")
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code >= 200 and code < 300:
                print ("effective ip")
                return True
            else:
                print  ("invalid ip and port")
                self.delete_ip(ip)
                return False

    def get_random_ip(self):
        #从数据库中随机获取一个可用的ip
        sample = random.sample(range(ProxyIp.objects.count()), 1)
        result = [ProxyIp.objects.all()[i] for i in sample]
        for ip_info in result:
            ip = ip_info.ip
            port = ip_info.port
            judge_re = self.judge_ip(ip, port)
            if judge_re:
                return "http://{0}:{1}".format(ip, port)
            else:
                return self.get_random_ip()

    def clean(self):
        #判断ip是否可用
        for ip_info in ProxyIp.objects.all():
            if not self.validate(ip_info.ip, ip_info.port):
                ip_info.delete()


if __name__ == "__main__":
    getip = GetIP()
    print(getip.clean())