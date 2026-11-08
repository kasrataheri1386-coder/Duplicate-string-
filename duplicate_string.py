def duplicate(n):
	if n[:len(n)//2]==n[len(n)//2:]:
		n=n[:len(n)//2]
		if len(n)!=0 and len(n)!=1:
			n=n[1:]
			return duplicate(n)
		else:
			return True
	else:
		return False
print(duplicate("allall"))
print (duplicate ("pop"))
print(duplicate("alilialili"))
	