import logging
from spiders.tools.proxyip import GetIP
logger = logging.getLogger(__name__)

class RandomProxyMiddleware(object):
    #动态设置ip代理
    def process_request(self, request, spider):
        get_ip = GetIP()
        request.meta["proxy"] = get_ip.get_random_ip()