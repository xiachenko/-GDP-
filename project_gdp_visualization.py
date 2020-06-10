#coding:utf-8
"""

�ۺ���Ŀ:������ʷ���ݻ������༰����ӻ�
���ߣ��ճ�
���ڣ�2020.6.1
"""

import csv
import math
import pygal
import pygal_maps_world.maps
wm = pygal_maps_world.maps.World()  #������Ҫʹ�õĿ�

def read_csv_as_nested_dict(filename, keyfield, separator, quote): #��ȡԭʼcsv�ļ������ݣ���ʽΪǶ���ֵ�
   
    result={}
    with open(filename,newline="")as csvfil        csvreader=csv.DictReader(csvfile,delimiter=separator,quotechar=quote)
        for row in csvreader:
            result[row[keyfield]]=row
    return result
   

pygal_countries = pygal.maps.world.COUNTRIES #��ȡpygal.maps.world�й��Ҵ�����Ϣ��Ϊ�ֵ��ʽ�������м�Ϊpygal�и������룬ֵΪ��Ӧ�ľ������(���齫����ʾ����Ļ���˽�����ʽ���������ݣ�
# print(pygal_countries)



def reconcile_countries_by_name(plot_countries, gdp_countries): #������������GDP���ݵĻ�ͼ����Ҵ����ֵ䣬�Լ�û������GDP���ݵĹ��Ҵ��뼯��
    
    set1 = set()
    dict1 = {}
    for k,v in gdp_countries.items():
        crusial = set(v.values())
        if len(crusial) == 5:
            set1.add(from_value_to_key(k))
    for key,value in plot_countries.items():
        if value not in set1:
            dict1[key] = value
    tuple1 = (dict1,set1)
    return tuple1


def from_value_to_key(value):            #ͨ������value_to_key,key_to_value������ʵ�ֹ��Ҵ�����д�����������ת��
    for k,v in pygal_countries.items():
        if v == value:
            return k

def from_key_to_value(key):              #ͬ��
    for k,v in pygal_countries.items():
        if k == key:
        


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    
    dict2 = {}
    set2 = set()
    for key,value in gdpinfo.items():
        if from_value_to_key(key) in plot_countries[0]:             #�����жϡ������ݵĹ�����Ϣ���Ĺ�����ļ���������һ���ж�
            if value[year] != "":                                   #�����������ݣ�������һ��������
                aeee = float(value[year])
                dict2[from_value_to_key(key)] = math.log(aeee)
            else:                                                   #��������ݣ��Ͱ����ŵ��ֵ���
                set2.add(from_value_to_key(key))
    tuple2 = (dict2,set2,plot_countries[1])
    return tuple2                               #����Ԫ��
    





def render_world_map(gdpinfo, plot_countries, year, map_file):

    dict3 = {}
    dict4 = {}
    list4 = list(gdpinfo[1])                      #������˳��������Ϊ�б����б����������ֵ��в���ֵ��1��
    list5 = list(gdpinfo[2])
    for values in list4:
        dict3[values] = "1"
    for i in list5:
        if i != None:                             #ɾ���ڶ��������еĿ�ֵ
            dict4[i] = "1"
    
    # worldmap_chart = pygal.maps.world.World()
    wm.title = 'ȫ��GDP�ֲ�ͼ'                      #���ݿ��ӻ��������
    wm.add('%s'%year,gdpinfo[0])
    wm.add('missing from world bank',dict3)
    wm.add('no data at this year',dict4)
    wm.render_to_file(map_file)
    # print(map_file)





# def test_render_world_map(year):  #���Ժ���
    # """
    # �Ը����ܺ������в���
    # """
    # gdpinfo = {
        # "gdpfile": "isp_gdp.csv",
        # "separator": ",",
        # "quote": '"',
        # "min_year": 1960,
        # "max_year": 2015,
        # "country_name": "Country Name",
        # "country_code": "Country Code"
    # } #���������ֵ�
  
   
   
    # pygal_countries = pygal.maps.world.COUNTRIES   # ��û�ͼ��pygal���Ҵ����ֵ�

    # # ����ʱ����1970��Ϊ�����Ժ����������ԣ������н�����ṩ��svg���жԱȣ�������ݿɽ��ļ���������
    # render_world_map(gdpinfo, pygal_countries, year, "isp_gdp_world_name_1970.svg")

   
    
pygal_countries = pygal.maps.world.COUNTRIES
print("��ӭʹ������GDP���ݿ��ӻ���ѯ")
print("----------------------")


year=input("���������ѯ�ľ������:")
# test_render_world_map(year)
bnb = read_csv_as_nested_dict("isp_gdp.csv","Country Name",",",'"')      #���к������в���
# print(love) 
aaa = reconcile_countries_by_name(pygal_countries,bnb)                 #���еڶ������������������Ϊ����alpha����������
bbb = build_map_dict_by_name(bnb,aaa,year)                             #���е��������������������Ϊ����beta����������
render_world_map(bbb,pygal_countries,year,"isp_gdp_world_name_%s.svg"%year)