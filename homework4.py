keys: list = ['Ten', 'Twenty', 'thirty']
values: list = [10, 20, 30]
dic: dict = dict(zip(keys, values))

print(dic)

dict1: dict = {'Ten': 10, 'Twenty': 20, 'thirty': 30}
dict2: dict = {'thirty': 30, 'fourty': 40, 'fifty': 50}
dict1.update(dict2)
print(dict1)