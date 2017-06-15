from fractions import Fraction

def pdt_scalaire_test(x,y):
	ret = 0
	for i in range(len(x)):
		ret += x[i]*y[i]
	return ret

def somme_tuple(x,y):
	ret = []
	for i in range(len(x)):
		ret.append(x[i] + y[i])
	return tuple(ret)

def diff_tuple(x,y):
	ret = []
	for i in range(len(x)):
		ret.append(x[i] - y[i])
	return tuple(ret)

def pdt_tuple(L,x):
	ret = []
	for i in x:
		ret.append(i*L)
	return tuple(ret)

def norme(x,pdt):
	return pdt(x,x)

def tuple_to_ratio(liste):
	ret = []
	for t in liste:
		tmp = []
		for x in t:
			ratio = str(Fraction(x).limit_denominator())
			tmp.append(ratio)
		ret.append(tuple(tmp))
	print str(ret)

def is_ortho(liste, pdt):
	for i in range(1,len(liste)):
		if not pdt(liste[i-1],liste[i]) == 0: return False
	return True

def grammschmmidt(base,pdt):
	ret = [base[0]]
	for k in range(1,len(base)):
		tmp = base[k]
		for i in range(1,k+1):
			pdt_scal = pdt(base[k],ret[i-1])
			norm = norme(ret[i-1], pdt)
			tmp = somme_tuple(tmp,pdt_tuple(-1,pdt_tuple(pdt_scal/norm,base[0])))
		ret.append(tmp)
	tuple_to_ratio(ret)
	return ret

