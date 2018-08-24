products = []
while True :
	goods = input('請輸入商品名稱:')
	if goods =='' or goods == 'end':
		break
	else :
		price = input('請輸入價格:')
		products.append([goods ,price])

with open("products.csv",'w',encoding='utf-8') as f:
	f.write('商品,價格\n')
	for i in products:
		f.write(i[0] + ',' + i[1]  + '\n')