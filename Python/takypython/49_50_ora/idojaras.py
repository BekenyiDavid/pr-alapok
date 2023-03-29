#napi homerseklet max min, march 22 - apr 20
# hany min es hany max van a listaban


napi_maximum = [14, 17, 21, 15, 16, 13, 8, 11, 12, 14, 16, 16, 14, 15, 13, 14, 16, 16, 14, 12, 12, 10, 11, 13, 15, 17, 19, 17, 19, 20]
napi_minimum = [8, 8, 9, 6, 7, 1, 0, 2, 3, 5, 4, 4, 3, 5, 4, 6, 8, 6, 4, 2, 1, -1, -1, 1, 3, 5, 7, 5, 7, 9]

def napi_maximum_fv():
    darab = 0
    for szam in napi_maximum:
        darab += 1
    print(darab)
napi_maximum_fv()

def napi_minimum_fv():
    darab = 0
    for szam in napi_minimum:
        darab += 1
    print(darab)
napi_minimum_fv()

def meleg():
    max = napi_maximum[0]
    for szam in napi_maximum:
	      if szam > max:
		        max = szam
    print(max)
meleg()

def hideg():
    min = napi_minimum[0]
    for szam in napi_minimum:
	      if szam < min:
		        min = szam
    print(min)
hideg()

def atlagmeleg():
    osszesen = 0
    for i in napi_maximum:
	      osszesen = osszesen + i

    print(f"oszzes meleg: {osszesen / len(napi_maximum)} C°")

atlagmeleg()

def atlaghideg():
    osszesen = 0
    for i in napi_minimum:
	      osszesen = osszesen + i
          
    print(f"oszzes meleg: {osszesen / len(napi_minimum)} C°")

atlaghideg()

