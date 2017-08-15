from FirstServer.modle import TstBean
class returnBean(object):
    code=1024
    msg='success'
    data=[]
    data=TstBean.tstbean(123,'测试','126.com','ma');
    # 定义构造方法
    def __init__(self, code, msg,tst):
        self.code = code
        self.msg = msg
        self.data=tst

    def convert_to_dict(obj):
        '''把Object对象转换成Dict对象'''
        dict = {}
        dict.update(obj.__dict__)
        return dict

