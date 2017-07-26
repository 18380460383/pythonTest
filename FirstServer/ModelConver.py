class modleconver(object):

    def convert_to_builtin_type(obj):
        # 把MyObj对象转换成dict类型的对象
        # d = {'__class__': obj.__class__.__name__,
        #      '__module__': obj.__module__,
        #      }
        d={}
        d.update(obj.__dict__)
        return d
