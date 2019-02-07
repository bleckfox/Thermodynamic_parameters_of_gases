import math

def air():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 29.438205
    n = -1
    weight = 28.9596308
    pr_ent = bs*log
    sum_ent = 0
    
    air_coef = [0, 230.1763, -1.610822, -5.9958719,
            22.942794, -24.559982, 12.976701, 
            -3.4848967, 0.3807486]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтропия = ' + str(S))
    print('Энтропия = ' + str(result))

#------------------------------------------------------
def atmo_nitrogen():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 28.15164
    n = -1
    weight = 28.15
    pr_ent = bs*log
    sum_ent = 0
    
    air_coef = [0, 223.2219, 13.197123, -37.241056, 
                63.327875, -56.654199, 28.408351, 
                -7.6067499, 0.84982197]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтропия = ' + str(S))
    print('Энтропия = ' + str(result))

#------------------------------------------------------
def nitrogen():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 28.298404
    n = -1
    weight = 28.016
    pr_ent = bs*log
    sum_ent = 0
    
    air_coef = [0, 223.9189, 12.689906, -36.209046, 
                61.787635, -55.105807, 27.471033, 
                -7.3015678, 0.8088504]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтропия = ' + str(S))
    print('Энтропия = ' + str(result))

#------------------------------------------------------

def oxygen():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 33.051759
    n = -1
    weight = 32
    pr_ent = bs*log
    sum_ent = 0
    
    air_coef = [0, 252.4995, -41.834166, 74.012048, 
                -68.340764, 36.342, -10.458144, 
                1.2628462, 0]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтропия = ' + str(S))
    print('Энтропия = ' + str(result))

#------------------------------------------------------

def carbone_dioxide():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 17.640049
    n = -1
    weight = 44.01
    pr_ent = bs*log
    sum_ent = 0
    
    air_coef = [0, 211.7171, 93.726944, -65.187329, 
                51.323515, -34.999006, 16.630372, 
                -4.5964181, 0.5471162]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтропия = ' + str(S))
    print('Энтропия = ' + str(result))

#------------------------------------------------------

def water_vapor():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 27.885805
    n = -1
    weight = 18.016
    pr_ent = bs*log
    sum_ent = 0
    
    air_coef = [-0.731476, 221.9783, 8.4430197, 
                5.9926485, -5.3640779, 3.4089868, 
                -1.29458, 0.1481876, 0]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтропия = ' + str(S))
    print('Энтропия = ' + str(result))

#------------------------------------------------------

def carbone_oxide():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 24.161791
    n = -1
    weight = 28.01
    pr_ent = bs*log
    sum_ent = 0
    
    air_coef = [0, 232.9405, 4.135004, -21.887391, 
                48.743499, -48.832394, 26.18109, 
                -7.3483677, 0.85143506]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтропия = ' + str(S))
    print('Энтропия = ' + str(result))

#------------------------------------------------------

def hydrogen():

    t = float (input('Enter temperature: '))
    T = t + 273.15
    tt = T/1000
    log = math.log(T/1000)
    bs = 40.01059
    n = -1
    weight = 2.016
    pr_ent = bs*log
    sum_ent = 0
    
    air_coef = [1.7412059, 179.3853, -23.707024, 
                9.6099679, 0.48559888, -2.1266412, 
                0.82772475, -0.11031765, 0]
    
    for i in range(len(air_coef)):
        ent = air_coef[i]*(tt**n)
        n = n + 1
        sum_ent+=ent
    S = sum_ent + pr_ent
    result = S/weight
    print('Молярная Энтропия = ' + str(S))
    print('Энтропия = ' + str(result))

#------------------------------------------------------

