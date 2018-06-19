# -*- coding: utf-8 -*-

import os, sqlite3


def get_score_in(low, high):
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	cursor.execute('select name from user where score between ? and ? order by score ASC',(low,high))
	l=cursor.fetchall()
	print('l:',l)
	cursor.close()
	conn.close()
	return  [x[0] for x in l]
#    ' 返回指定分数区间的名字，按分数从低到高排序 '
#----
#    pass
#----



# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')