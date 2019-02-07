import math

def air():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 0
    n = 0
    weight = 28.9596308
    pr_ent = bs*log
    sum_ent = 0
    air_coef = [-5.42*10**2, 2.9438265*10**4,-8.0541099*10**2,-3.9972481*10**3, 
            1.7207096*10**4, -1.9647986*10**4, 1.0813917*10**4, 
           -2.9870543*10**3, 3.3315502*10**2]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent+487.6
    result = S/weight
    print('Молярная Энтальпия = ' + str(S))
    print('Энтальпия = ' + str(result))

#----------------------------------------------------------

def atmo_nitrogen():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 0
    n = 0
    weight = 28.15
    pr_ent = bs*log
    sum_ent = 0
    air_coef = [40.1, 28151.964, 6598.5613, -24827.371,
                47495.9, -45323.358, 23673.626,
                -6520.071, 743.5942]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтальпия = ' + str(S))
    print('Энтальпия = ' + str(result))    
    
#-------------------------------------------------------------

def nitrogen():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 0
    n = 0
    weight = 28.016
    pr_ent = bs*log
    sum_ent = 0
    air_coef = [25.45, 28298.404, 6344.9526, -24139.364, 46340.725,
                -44084.647, 22892.528, -6258.4868, 707.7441]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтальпия = ' + str(S))
    print('Энтальпия = ' + str(result))

#-----------------------------------------------------------------    

def oxygen():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 0
    n = 0
    weight = 32
    pr_ent = bs*log
    sum_ent = 0
    air_coef = [-300.3, 33051.759, -20917.083, 49341.367,
                -51255.572, 29073.599, -8715.1202,
                1082.4395, 0]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтальпия = ' + str(S))
    print('Энтальпия = ' + str(result))

#-----------------------------------------------------------------

def carbone_dioxide():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 0
    n = 0
    weight = 44.01
    pr_ent = bs*log
    sum_ent = 0
    air_coef = [847.4, 17640.049, 46863.472, -43458.218,
                38492.636, -27999.206, 13858.643,
                -3939.7868, 478.72667]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтальпия = ' + str(S))
    print('Энтальпия = ' + str(result))

#------------------------------------------------------------------    

def water_vapor():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 731.476
    n = 0
    weight = 18.016
    pr_ent = bs*log
    sum_ent = 0
    air_coef = [2012.947, 27885.805, 4221.5098, 3995.099,
                -4023.058, 2727.2546, -1078.8167,
                169.87509, 0]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтальпия = ' + str(S))
    print('Энтальпия = ' + str(result))

#------------------------------------------------------------------    

def carbone_oxide():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 0
    n = 0
    weight = 28.01
    pr_ent = bs*log
    sum_ent = 0
    air_coef = [-32.54, 29161.791, 2067.502, -14591.594,
                36557.624, -39065.915, 21817.574,
                -6298.6014, 745.00568]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтальпия = ' + str(S))
    print('Энтальпия = ' + str(result))

#-------------------------------------------------------------------    

def hydrogen():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = -1741.2059
    n = 0
    weight = 2.016
    pr_ent = bs*log
    sum_ent = 0
    air_coef = [-4684.72, 40010.59, -11853.512, 6406.6451,
                364.19916, -1701.313, 689.77065,
                -94.557986, 0]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтальпия = ' + str(S))
    print('Энтальпия = ' + str(result))

#---------------------------------------------------------------------    
