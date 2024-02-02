#BMI 程式
weight = input('請輸入體重(KG):')
height = input('請輸入身高(cm):')
weight = int(weight)
height = int(height)
height = height / 100
BMI = weight / (height * height)
print(BMI)
if BMI < 18.5: 
	print('體重過輕')
elif BMI >= 18.5 and BMI < 24: 
	print('健康體重')
elif BMI >= 24: 
	print('體重過重')