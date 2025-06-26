def city_in_year(h,y):
    city = list(h.keys())
    year = list(h.values())
    index = year.index(y)
    print('Oylmpic %d in %s' %(y,city[index]))

host = {'Tokyo':2020,'Beijing':2024,'Paris':2024 ,'Milan':2028}
year = int(input('Year Of Olympic : '))
year_list = list(host.values())
x = year_list.count(year)
if x > 0 :
    city_in_year(host,year)
else :
    print('No Olympic.')