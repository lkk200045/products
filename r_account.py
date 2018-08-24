p = []
with open("products.csv",'r',encoding='utf-8') as f:
	for item in f:
		if '商品,價格' in item:
			continue
		name, price = item.strip().split(',')
		p.append([name,price])
print(p)
