# EasyShop---python

可用于KOOK机器人的轮子（使用了本地数据库Tinydb开发） 代码易读
使用教程：

## 0. 导入与基础

把EasyShop.py放进你的程序主文件夹

在文件使用

```python
from EasyShop import EasyShop
shop = EasyShop(商店文件保存路径)
```

## 1. 添加商品

```python
shop.AddGoods(name='测试',
              price=10,
              quantity=10)
```

参数：
name:商品名称
price:商品价格
quantity:商品数量

## 2. 删除商品

```python
shop.DeleteGoods(parameter='all或者不填',
                 number='00001')
```

参数：
parameter:填写all或者不填
number:商品编号,当初添加的时候会显示

## 3. 搜索商品

```python
shop.SearchGoods(number='00001')
```

参数:



number:商品编号,当初添加的时候会显示

## 4. 更新商品

```python
shop.UpdateGoods(number='00001',
                 new_good={'name': 'new'}
                 )
```

number:商品编号
new_good:要更新的东西

## 5.  附加功能 商品数量-1

```python
shop.ReduceQuantity(number='00001')
```

number:商品编号
