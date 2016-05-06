groclist = []



def removelist(item):
	if item.lower() not in groclist:
		print "Item is not there."
	else:
		groclist.remove(item.lower())
	sortlist()
	print groclist

def sortlist():
	groclist.sort()
	return groclist

def addlist(item):
	if item.lower() in groclist:
		print "Item already exists."
	else:
		groclist.append(item.lower())
	sortlist()
	print groclist

def main():
	pass 

	
if __name__ == "__main__":
	main()



