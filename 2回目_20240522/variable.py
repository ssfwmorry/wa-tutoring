# 代入

# イコール＝左のものに、右を代入します
a = 100 # aという名前の箱に入っているものは100です。
b = 1000

print(a)
print(100)
print('a')


'''
# これはエラー
100 = a
'''

'''
# 変数名には制限があります
a # アルファベットのみは宣言可能
11 # 数字は変数になり得ません
a1 # アルファベット➕数字は宣言可能
'''

# 変数名を使うことで、中身の値にラベルづけするイメージ
january = 1
april = 4

print('Januaryは' + str(january) + '月です')

# インデントは解釈される
#     print('a') # これはインデンテーションエラーとなる