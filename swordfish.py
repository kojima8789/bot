while True:
    print('あなたはだれ？')
    name = input()
    if name != 'joe':
        continue
    print('こんにちはjoe。パスワードは何？（魚の名前）')
    password = input()
    if password == 'swordfish':
        break
print('認証しました。')
#

spam = 8

if spam == 1:
    print('hello')
elif spam == 2:
    print('howdy')
else:
    print('greeting!')
