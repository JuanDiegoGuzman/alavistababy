def avgweeks(weeks, my_csv):                    

    weekspop = {}
    for line in my_csv:
        myweeks = line["biweek"]
        pop = float(line["pop"])
        if line["cases"] != "NA": 
            cases =float(line["cases"])
            weekspop[myweeks] = weekspop.get(myweeks, [0,0,0]) 
            weekspop[myweeks][0] = weekspop[myweeks][0] + pop
            weekspop[myweeks][1] = weekspop[myweeks][1] + cases
            weekspop[myweeks][2] = weekspop[myweeks][2] + 1
            
            for key in weekspop.keys():
                if key == weeks:
                    avg_cases = 100000*weekspop[key][2]/weekspop[key][1]
                    return print (key, avg_cases)

   