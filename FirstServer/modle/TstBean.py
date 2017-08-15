class tstbean(object):
    id=1024
    name='测试'
    email='123@126.com'
    memo='测试1'
    # 定义构造方法
    def __init__(self, id, name, email,memo):
        self.id = id
        self.name = name
        self.email = email
        self.memo = memo

    def convert_to_dict(obj):
        '''把Object对象转换成Dict对象'''
        dict = {}
        dict.update(obj.__dict__)
        return dict