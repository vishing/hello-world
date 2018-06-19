# _*_ coding:utf-8 _*_

def calc(*numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum

nums=[1,2,3]
print('test')
print(calc(nums))