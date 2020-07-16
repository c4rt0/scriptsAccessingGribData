import pygrib

grbs = pygrib.open('download_area.grib')

grbs.seek(0)
for g in grbs:
    # Below example of accessing some data with use of the keys from a grib file
    # =================  Uncomment below  =================  :

    # accessingGribData = (g.name,g.stepType, g.paramId, g.level, g.levelType, g.time, g.centre, g.shortName, g.dataDate, g.packingType, g.gridType, g.centre, g.table2Version, g.indicatorOfParameter ) #g, g.level, g.time, 
    # print(accessingGribData)

    # ================= ================= =================  :

    msg = grbs[1] # get record number 1 (there's 2 more in this GRIB file)
    allKeys = msg.keys()
    print (allKeys)