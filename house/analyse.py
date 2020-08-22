import pandas as pd
from matplotlib import pyplot as plt


"""
相同登记人:名字+证件尾号 相同的认为是同一个人
登记比:登记人数/套数
刚需比:刚需家庭/登记数
核验率:核验通过人数/登记数
首次登记:此前未有登记记录的
新客率:首次登记的/登记数
登记人平均登记次数:登记者的总登记次数/登记数
清盘率:首开售出/套数[暂无数据]

价格-时间

登记比-时间
登记比-价格
登记比-刚需比
登记比-登记人平均登记次数
登记比-新客率


核验率-登记人平均登记次数
核验率-价格
核验率-时间
核验率-登记比

刚需比-价格
刚需比-时间

新客率-价格
新客率-时间
新客率-刚需比



"""


def analyse():
    houses, house_person_mapping, house_people = get_data()
    house_people['register_datetime'] = pd.to_datetime(house_people['register_time'], format='%Y-%m-%d')
    house_people['register_month'] = house_people['register_time'].map(lambda x: x[:7])
    house_people.set_index('register_time')
    house_people['is_verify'] = house_people['register_status'].map(lambda x: '核验通过' if x == '核验通过' else '核验未通过')
    register_status_by_month = pd.pivot_table(house_people, values='id', index='register_month', columns='is_verify',
                                    aggfunc='count', fill_value=0, margins=False)
    register_status_by_month['verify_rate'] = group_by_month['核验通过'] / (register_status_by_month['核验通过'] + register_status_by_month['核验未通过'])
    register_status_by_month.plot(kind='bar')
    pass


def get_data():
    houses = pd.read_csv('data/houses.csv')
    house_person_mapping = pd.read_csv('data/house_person_mapping.csv')
    house_people = pd.read_csv('data/house_people.csv')

    return houses, house_person_mapping, house_people


def main():
    analyse()


if __name__ == '__main__':
    main()

