import serpy
import json

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointSerializer(serpy.Serializer):
    x = serpy.Field()
    y = serpy.Field()
    mean = serpy.MethodField()

    def get_mean(self, obj):
        return (obj.x + obj.y)

p = Point(1, 2)
print p

p_dict = PointSerializer(p).data
print p_dict

p_txt = json.dumps(p_dict)
print p_txt

new_p = json.loads(p_txt)
print new_p

new_point = Point(**new_p)
print new_point
