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

    head = '''---\nlayout: post\ntitle: "区块链'''+today[:10]+'''日快讯"\ndate: ''' + today + '''\ndescription: 这里有你想了解的区块链新闻\n---\n'''
    f.write(head)

    size = len(btc8_df)
    for i in range(0, 3):
        title = btc8_df['title'][i]
        if '|' in title:
            continue
            pass
        url = btc8_df['url'][i]
        content = btc8_df['content'][i]
        txt = '[' + title + '](' + url + ')\n' + '>' + content + '\n\n\n'
        f.write(txt)
        pass

    for i in range(3, size):
        title = btc8_df['title'][i]
        if '|' in title:
            continue
            pass
        url = btc8_df['url'][i]
        txt = '[' + title + '](' + url + ')\n\n'
        f.write(txt)
        pass

    pass


if __name__ == '__main__':
    f = open('blockchain.txt', 'w')

    btc8()

    f.close()

    pass
