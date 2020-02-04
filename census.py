import openpyxl,os
#xu ly file excel
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet= wb.get_sheet_by_name('Population by Census Tract')
country=sheet['C2'].value
spop=0
scen=0
#tao o dia de lua
luu=open('dữ liệu lọc.txt','w')
#luu du lieu loc
for ob in sheet['A2':'D72866']:
    if country == ob[2].value:
        spop=spop+int(ob[3].value)
        scen=scen+int(ob[0].value)
    else:
        luu.write(country +' population: '+str(spop)+'\n')
        luu.write(country +' census tract: '+str(scen)+'\n')
        luu.write('------------\n')
        if ob[2].value==None:
            luu.close()
            break
        country=ob[2].value
        spop=0
        scen=0
        spop=spop+int(ob[3].value)
        scen=scen+int(ob[0].value)

