products = []
while True :
	goods = input('請輸入商品名稱:')
	if goods =='' or goods == 'end':
		break
	else :
		price = input('請輸入價格:')
		products.append([goods ,price])

for i in range(len(products)) :
	print(products[i])