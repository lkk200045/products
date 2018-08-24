products = []
while True :
	goods = input('請輸入商品名稱:')
	if goods =='' or goods == 'end':
		break
	else :
		price = input('請輸入價格:')
		products.append([goods ,price])

for i in products:
	#每一個i裡的0是商品名1是價格
	print('商品名:',i[0] , '價格', i[1])

