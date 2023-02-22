import psycopg2

test_plot1 = 'MULTIPOLYGON(((-91.434 33.442,-91.435 33.444,-91.438 33.444,-91.438 33.442,-91.434 33.442)))'               #basic (intersects only with soil) test poly
#test_plot1 = 'MULTIPOLYGON(((-91.255888 33.441481,-91.265441 33.443522,-91.257276 33.449727,-91.255888 33.441481)))'     #combined(intersects with both soil and 0% clay structures(water, bpi) test poly
#test_plot1 = 'MULTIPOLYGON(((-91.368310 33.429357, -91.355492 33.429561, -91.362840 33.419519,-91.368310 33.429357)))'   #test poly fully on water

#db connection
conn = psycopg2.connect(
    host="localhost",
    port="5435",
    database="mukey_test",
    user="postgres",
    password="25111999")

#area calculation of the test poly
def test_poly_area():
    cursor = conn.cursor()
    postgreSQL_select_Query = f""" 
    SELECT ST_Area(ST_GeomFromText('SRID=4326;{test_plot1}'))
    """
    
    cursor.execute(postgreSQL_select_Query)
    plot_area = cursor.fetchall()

    return plot_area[0][0]

#area calculation of intersection water(bpi)-test poly
def water_mu_area():
    cursor = conn.cursor()
    postgreSQL_select_Query = f""" 
    SELECT sum(ST_Area(ST_Intersection(geometry,ST_GeomFromText('SRID=4326;{test_plot1}'))))
    FROM mukey_test_bound
    WHERE musym IN ('W','BPI') AND ST_Intersects(geometry,ST_GeomFromText('SRID=4326;{test_plot1}'))
    """
    
    cursor.execute(postgreSQL_select_Query)
    water_area = cursor.fetchall()
    if water_area[0][0]:
        return water_area[0][0]
    else:
        return 0

#extraction of necessary spatial data (mukey, intersection areas for each mukey)
def spatial_data_extractor():
    cursor = conn.cursor()
    postgreSQL_select_Query = f"""
    SELECT mukey, 
    (SELECT ST_Area(ST_Intersection(geometry,ST_GeomFromText('SRID=4326;{test_plot1}'))))
    AS area
    FROM mukey_test_bound
    WHERE ST_Intersects(geometry,ST_GeomFromText('SRID=4326;{test_plot1}'))
    """

    cursor.execute(postgreSQL_select_Query)
    spatial_records = cursor.fetchall()

    return spatial_records

#tabular data extraction (mukey, clay%)
def tabular_data_extractor(mukey_tup):
    cursor = conn.cursor()
    if len(mukey_tup)==1:
        postgreSQL_select_Query = f"""
        select * 
        from mukey_test_clay
        where mukey like '{mukey_tup[0]}'
        """
    else:
        postgreSQL_select_Query = f"""
        select * 
        from mukey_test_clay
        where mukey in {mukey_tup}
        """

    cursor.execute(postgreSQL_select_Query)
    spatial_records = cursor.fetchall()
    mukey_clay_dict = {}
    for item in spatial_records:
        mukey_clay_dict[item[0]]=item[1]
    return mukey_clay_dict

#main func. returns average clay% per test poly, or 'WATER' if test poly fully in water
def calculator():
    spatial_data = spatial_data_extractor()
    mukey_list = []
    plot_area = test_poly_area()
    water_area = water_mu_area()
    for item in spatial_data:
        mukey_list.append(item[0])

    tabular_data = tabular_data_extractor(tuple(mukey_list))
    clay_prc = 0

    if plot_area == water_area: #check if test field fully in water
        return 'WATER'
    else:
        for item in spatial_data:
            clay_prc += (item[1]/(plot_area - water_area))*tabular_data[item[0]] #calculation of average clay% by formula
        return round(clay_prc, 2)                                                #avg_clay% = sum ( intersection_area[i] * clay%[i] / (test_plot_area - area_covered_by_water_or_BPI) )

print (calculator())

