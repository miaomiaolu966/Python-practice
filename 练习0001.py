#第 0001 题： 做为 Apple Store App 独立开发者，你要搞
# 限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？
import uuid
"""
本模块提供不可变对象UUID (UUID类)和函数uuid1(), uuid3(), uuid4(), uuid5()来生成版本1，3，4和5UUIDs，
它们被指定在RFC 4122.
如果你想要唯一的 ID, 你可以调用uuid1
() or uuid4().请注意 uuid1()创建的UUID包含网络地址，
可能会有安全问题。uuid4()创建一个随机的UUID。
"""

uuids = []

for i in range(0,200):
    uuids.append(uuid.uuid4())
print(uuids)



