def avgyear(year, my_csv):
    """Esto es una función"""
    yearpop = {}
    for line in my_csv:
        myyear = line["year"]
        pop = float(line["pop"])
        if line["cases"] != "NA": 
            
     
            cases =float(line["cases"])
            yearpop[myyear] = yearpop.get(myyear, [0,0,0]) 
            
            yearpop[myyear][0] = yearpop[myyear][0] + pop
            yearpop[myyear][1] = yearpop[myyear][1] + cases
            yearpop[myyear][2] = yearpop[myyear][2] + 1
            
        for key in yearpop:
            if key == year:
                avg_cases = 100000*yearpop[key][2]/yearpop[key][1]
                return print (key, avg_cases)