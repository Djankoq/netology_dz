good = ""
goods = []
shop = ""
shops = []

while good.lower() != "выход":
    good = input("Введите наименование товара, который необходимо купить, для выхода введите 'Выход'\n")
    if good.lower() != "выход":
        goods.append(good)

while shop.lower() != "выход":
    shop = input("Введите наименование магазина, для выхода введите 'Выход'\n")
    if shop.lower() != "выход":
        shops.append(shop)

print(shops)
print(goods)
sums = {}
for shp in shops:
    sum = 0
    for gd in goods:
        print(f"Сколько стоит {gd} в {shp}?")
        a = int(input())
        sum += a

    sums[shp] = sum

sorted_sum = sorted(sums.items(), key=lambda item: item[1])

print(f"Дешевле всего покупка обойдется в {sorted_sum[0][0]}, сумма - {sorted_sum[0][1]}")

