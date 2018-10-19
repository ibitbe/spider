import tushare as ts
import datetime

tushare_token = 'aa61aad2313a0d027f0369e3faffc0ea30cd8b1f7949c399ca502866'

ts.set_token(tushare_token)
pro = ts.pro_api()


def btc8():
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=1)

    today = today.strftime('%Y-%m-%d %H:%M:%S')
    yesterday = yesterday.strftime('%Y-%m-%d')

    btc8_df = pro.btc8(start_date=yesterday + ' 18:00:00', end_date=today, fields='title, url,content')

    f = open('e:\\btc.txt', 'w')
    head = '''---\nlayout: post\ntitle:  "今日快讯"\ndate:   ''' + today + '''\ncategories: blog\nauther: "Mr.Chang"\n---\n'''
    f.write(head)
    size = len(btc8_df)
    for i in range(0, 3):
        title = btc8_df['title'][i]
        url = btc8_df['url'][i]
        content = btc8_df['content'][i]
        txt = '[' + title + '](' + url + ')\n' + '>**' + content + '**\n\n\n'
        f.write(txt)
        pass

    for i in range(3, size):
        title = btc8_df['title'][i]
        url = btc8_df['url'][i]
        txt = '[' + title + '](' + url + ')\n\n'
        f.write(txt)
        pass

    f.close()
    pass


if __name__ == '__main__':
    btc8()

    pass
