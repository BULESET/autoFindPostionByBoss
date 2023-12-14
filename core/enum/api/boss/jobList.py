# @Time :       1.11.23 2:00 下午
# @Author :     sunyong
# @Email :      sunyong@avic-intl.cn
# @File :       jobList.py
# @Project :    PositionRecommend
# @Description:


from enum import Enum


class JobList(Enum):
    header = {
        "Host": "",
        "traceid": "B3F6E5EF-C544-467C-B081-A037B819F259",
        "accept": "application/json, text/plain, */*",
        "x-requested-with": "XMLHttpRequest",
        "zp_token": "V1QNsjGOD921tgXdNgxxURKS6w5T7fww~~",
        "token": "ZGBBW4dEJc6rnJJ",
        "sec-ch-ua-platform": "macOS",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "accept-language": "zh-CN,zh;q=0.9",
        "referer": "https://www.zhipin.com/web/geek/job?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&city=101010100&degree=202,203",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Cookie": "lastCity=101010100; wd_guid=5e62ab42-59ce-475f-9c0d-4298bc5b9ec0; historyState=state; _bl_uid=Ryl2Cl891R1vItma2gLF884l146y; collection_pop_window=1; YD00951578218230%3AWM_NI=UkXU2S6%2BwbIBbNstetDi1Nl%2FhU19a4rJj2WJ7ZBjPY144LLeyWXLQUaRmaf0Q6kMiboQERwSEkpQe61rrtG83dTrU2MgCIpfL3IydUjWOAjpy2Rsiqy7dVxMFjcdK3lXWEU%3D; YD00951578218230%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea7dc39a1e8add8d87eb0868eb6c85e838b8a83c563f78d98b1c950819bfdb5c72af0fea7c3b92a97b598b6b159f6f5b983cc4aa292bd95e88088b7ffafef25ac8bffdae440b296a6d3d642f5868e8bd353f3ecfcadcf6fbb8998add45fa38ea382e53c93eaa5aeec6aad8f8bb3f65987b5c0b2e83ef3aebe95c634f1bc9c93d83a8fb98daaf36e90ed879ae75faa8981a2e97cbbee9e94ec7bbbe9acb7fb4786b6ad85ca39b08899a6d837e2a3; YD00951578218230%3AWM_TID=r177pWFxOpxBQUARRVbBn4GWKdSCRnTS; gdxidpyhxdE=5uIXqY0ldWBIQCXxTms6onnaiY3eLT38lO%2BeAXbVhwUDMJqSUOUNZsP%5CPzlgdXtLhwjlAYx%2FBonKDBfEVe4rD%5CU%5CiyhIK8QnUqaxo1uVbHSu6Z9kWjN2lAUK1fcJVJr8Zf9WviYaaq6%5C%2ByJrNovy3zPctcgnuiEQtIUIaPL%2Fe8Oy9u4f%3A1698832822818; __zp_seo_uuid__=6c56c172-c911-42a7-aa26-2db156e8b9a9; __g=-; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2Fbeijing%2F&s=1&g=&s=3&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1698817379,1698823764,1698827705,1698889422; boss_login_mode=app; wt2=DcUJ3zth9AQVCgUHieESI9TlwcFOop7-KcPKya02frZzgEtkH21AVcORFj97Id46FH2Bkv7burWevfWuiOnLHGA~~; wbg=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1698889816; __zp_stoken__=e8dbeKQoNIDFFBQNVfndTI2xuVlU6bSp%2BJwYYExdtMVwLeiBSeDxdJGtbKF4DIGldQS5SMWB1NTw%2FR0M8eDlvWCoeDncUTToYfWNpc0l7Jl0sSU1NQWMeJ0p9dRdbDgNNAxdgTmAORUByBkY%3D; __c=1698889422; __a=32415874.1691473438.1698827704.1698889422.180.16.13.114; geek_zp_token=V1QNsjGOD921tgXdNgxxURKS6w5T7fww~~"
    }
    path = "/wapi/zpgeek/search/joblist.json"
    method = "GET"
    body = "https://hxapi-pet.hang-xin.cn"


class HttpHostType(object):
    """获取文件MineType"""

    @staticmethod
    def getHeader(env):
        member = JobList.__members__.get(env.lower())
        return member.value


if __name__ == '__main__':
    pass
    x = 4
    name = (lambda x: x + 1)(x)
    print(name)

    # H = HttpHostType()
    # print(H.get_type(env='test1'))
