from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
from dashscope import ImageSynthesis
import os

prompt = "A high-tech laboratory at night under aurora borealis, moonlight gradient transitions from aurora blue (#E6F2FF) to cloudberry purple (#D8C4F7) to pure white. Central holographic display shows geometric cloudberry stem cells dividing with double helix DNA strands integrated, hidden crescent negative space visible in background glow. Scientific annotations in custom rounded sans-serif with molecular dot icons float like laboratory notes. Petri dish emits soft particle trails in polar ice blue and moss green (#5B8C7A), AR interface elements overlay with transparent carbon black (#1A1A1A) panels. Clean vector plant textures, micro-detail precision, moonlight healing atmosphere, flat design with subtle depth."


print('----sync call, please wait a moment----')
rsp = ImageSynthesis.call(api_key="sk-ff1925fb890c452f95ba18ec1b1074b4",
                          model="wanx2.1-t2i-turbo",
                          prompt=prompt,
                          n=1,
                          size='1024*1024')
print('response: %s' % rsp)
if rsp.status_code == HTTPStatus.OK:
    # 在当前目录下保存图片
    for result in rsp.output.results:
        file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
        with open('./%s' % file_name, 'wb+') as f:
            f.write(requests.get(result.url).content)
else:
    print('sync_call Failed, status_code: %s, code: %s, message: %s' %
          (rsp.status_code, rsp.code, rsp.message))