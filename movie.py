import tushare as ts
import datetime

today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')


def real_time_box_office():
    df = ts.realtime_boxoffice()
    f.write('# 实时票房\n\n')
    table_head = '|影片名|排名|实时票房(万)|累计票房(万)|上映天数|\n|-|-|-|-|-|\n'
    f.write(table_head)
    for i in range(len(df)):
        txt = '|' + df['MovieName'][i] + '|' + df['Irank'][i] + '|' + df['BoxOffice'][i] + '|' + \
              df['sumBoxOffice'][i] + '|' + df['movieDay'][i] + '|\n'
        f.write(txt)
        pass
    f.write('\n\n')
    pass


def today_box_office():
    df = ts.day_boxoffice()
    f.write('\n# 当日票房\n\n')
    table_head = '|影片名|排名|单日票房(万)|累计票房(万)|上映天数|\n|-|-|-|-|-|\n'
    f.write(table_head)
    for i in range(len(df)):
        txt = '|' + df['MovieName'][i] + '|' + df['IRank'][i] + '|' + df['BoxOffice'][i] + '|' + \
              df['SumBoxOffice'][i] + '|' + df['MovieDay'][i] + '|\n'
        f.write(txt)
        pass
    f.write('\n\n')
    pass


def month_box_office():
    df = ts.month_boxoffice()
    f.write('\n# 月度票房\n\n')
    table_head = '|影片名|排名|上映日期|单月票房(万)|口碑指数|\n|-|-|-|-|-|\n'
    f.write(table_head)
    for i in range(len(df)):
        txt = '|' + df['MovieName'][i] + '|' + df['Irank'][i] + '|' + df['releaseTime'][i] + '|' + \
              df['boxoffice'][i] + '|' + df['WomIndex'][i] + '|\n'
        f.write(txt)
        pass
    pass


if __name__ == '__main__':
    f = open('movie.txt', 'w')
    head = '''---\nlayout: post\ntitle: "电影票房"\ndate:   ''' + today[:10] + '''\ndescription: 最新的电影票房排行榜\n---\n'''
    f.write(head)

    real_time_box_office()

    today_box_office()

    month_box_office()

    f.close()
