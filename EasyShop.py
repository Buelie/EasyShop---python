from tinydb import TinyDB, Query


class EasyShop:
    def __init__(self, path):
        self.path = path

    # 添加商品  必填参数:商品名称,商品价格,商品数量  商品的编号会打印出来，请留意
    def AddGoods(self, name: str, price: int, quantity: int):
        db = TinyDB(f'{self.path}/shop.json')
        db_all = db.all()
        if len(db_all) == 0:
            db.insert({'name': name, 'number': '00001', 'price': price, 'quantity': quantity})
            print(f'商品名称:{name},商品编号:00001,商品价格:{price},商品数量:{quantity}')
        else:
            num = str(int(db_all[-1].get('number')) + 1)
            len_num = len(num)
            how_number = 5 - len_num
            new_number = how_number * '0' + num
            db.insert({'name': name, 'number': new_number, 'price': price, 'quantity': quantity})
            print(f'商品名称:{name},商品编号:{new_number},商品价格:{price},商品数量:{quantity}')

    # 删除商品  必填参数:parameter(填入all为删除所有商品,不填则删除指定编号的商品)
    def DeleteGoods(self, parameter='', number=''):
        db = TinyDB(f'{self.path}/shop.json')
        if parameter == 'all':
            db.truncate()
            print('全部商品已经清空')
        else:
            search = Query()
            dic = db.search(search['number'] == number)[0]
            print(f'编号为:{dic.get("number")}的商品已被删除')
            db.remove(search['number'] == number)

    # 查询商品,返回字典 必填参数:number(字符串类型)
    def SearchGoods(self, number: str):
        db = TinyDB(f'{self.path}/shop.json')
        search = Query()
        dic = db.search(search['number'] == number)[0]
        return dic

    # 更新商品 必填参数:number(字符串类型) new_good()
    def UpdateGoods(self, number: str, new_good: dict):
        db = TinyDB(f'{self.path}/shop.json')
        search = Query()
        db.update(new_good, search['number'] == number)
        print('更新成功')

    # 额外功能， 商品数量-1
    def ReduceQuantity(self, number: str):
        db = TinyDB(f'{self.path}/shop.json')
        search = Query()
        dic = db.search(search['number'] == number)[0].get('quantity')
        if dic <= 0:
            print('商品库存为0， 请选择补货或者删除')
        else:
            new_quantity = dic - 1
            db.update({'quantity': new_quantity}, search['number'] == number)
