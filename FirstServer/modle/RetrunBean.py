class returnBean(object):
    code=1024
    msg='success'
    data=[]
    # 定义构造方法
    def __init__(self, code, msg, data):
        self.code = code
        self.msg = msg
        self.data = data

    def convert_to_dict(obj):
        '''把Object对象转换成Dict对象'''
        dict = {}
        dict.update(obj.__dict__)
        return dict

