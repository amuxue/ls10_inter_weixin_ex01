import json
import time

import requests


class TestInterface:
    corpid = "ww4dd1f1a0852a1941"
    secret = "J1OELKLGBZPsK5Sr4ghto5-bYZrerPwLPqFkjH1BGD8"

    def test_ex01(self):
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.secret}')
        self.token = r.json()["access_token"]
        print(self.token)
        self.userid="test_add_xql1"
        # 新增
        data_add={
            "access_token":self.token,
            "userid":self.userid,
            "name":"test_tainjia",
            "mobile":12212341234,
            "department":[2]
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}", data=json.dumps(data_add))
        print(r.text)
        time.sleep(1)
        # 查询
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={self.userid}")
        print(r.json())
        # 修改
        data_update={
                "access_token":self.token,
                "userid":self.userid,
                "name":"test_tianjia",
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",data=json.dumps(data_update))
        print(r.json())
        time.sleep(1)
        # 删除
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={self.userid}")
        print(r.json())

