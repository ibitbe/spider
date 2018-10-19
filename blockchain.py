import tushare as ts
import datetime

tushare_token = 'aa61aad2313a0d027f0369e3faffc0ea30cd8b1f7949c399ca502866'
today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)

today = today.strftime('%Y-%m-%d')
yesterday = yesterday.strftime('%Y-%m-%d')

ts.set_token(tushare_token)
pro = ts.pro_api()

btc8_df = pro.btc8(start_date=yesterday + ' 18:00:00', end_date=today + ' 18:00:00', fields='title, url')

f = open('e:\\btc.txt', 'w')
head = '''---\nlayout: post\ntitle:  "今日快讯"\ndate:   ''' + today + '''\ncategories: blog\nauther: "Mr.Chang"\n---\n'''
f.write(head)
for i in range(len(btc8_df)):
    title = btc8_df['title'][i]
    url = btc8_df['url'][i]
    txt = '[' + title + '](' + url + ')\n\n'
    f.write(txt)
    pass

f.close()
