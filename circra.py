#!/usr/bin/python

import random
import pprint

class letter(object):
	letter = ""
	actualLetter= ""
	occurenceAtAll = 0.0
	occurenceTwice = 0.0

	occurencePerWord = 0.0
	occurenceAtStart = 0.0

	candidats = []
	candidatsAtAll = []
	candidatsTwice = []
	candidatsPerWord = []
	candidatsAtStart = []

    # The class "constructor" - It's actually an initializer ##read more about this 
	def __init__(self, letter, occurenceAtAll, occurenceTwice):
		self.letter = letter
		self.decipherLetter= ""
		self.actualLetter = 0
		self.occurenceAtAll = occurenceAtAll
		self.occurenceTwice = occurenceTwice

		self.occurencePerWord = 0.0
		self.occurenceAtStart = 0.0
		
		self.candidatsAtAll = []
		self.candidatsTwice = []
		self.candidatsPerWord = []
		self.candidatsAtStart = []

		self.candidats4Hits = []
		self.candidats3Hits = []
		self.candidats2Hits = []
		self.candidats1Hit = []

		self.lastCandidats=""

    # method to get the type of object  does NOT seem to work
	def __repr__(self):
		print "test"
		return "test"
    
    # method like java print object
	def __str__(self):
		return "letter: %s, occurenceAtAll: %f, occurence twice: %f, occurencePerWord: %f, occurenceAtStart: %f" % (self.letter, self.occurenceAtAll, self.occurenceTwice, self.occurencePerWord, self.occurenceAtStart) 

	def setLastCandidats(self, string):
		self.lastCandidats = string

	# calculates the same stuff a lot of time, but it works TO DO: make it better :)	
	def createCandidates(self, alphabet):
		for x in alphabet:
			counter=0
			z=0

			for y in self.candidatsAtAll:
				if y == x:
					counter+=1
				z+=1

			z=0
			for y in self.candidatsTwice: 
				if y == x:
					counter+=1
				z+=1
		
			z=0
			for y in self.candidatsAtStart:
				if y == x:
					counter+=1
				z+=1
		
			z=0
			for y in self.candidatsPerWord:
				if y == x:
					counter+=1
				z+=1


			if counter == 4:
				self.candidats4Hits.append(x)
			elif counter == 3:
				self.candidats3Hits.append(x)
			elif counter == 2:
				self.candidats2Hits.append(x)
			elif counter == 1:
				self.candidats1Hit.append(x)


### functions ###
def parseTextFileToString( file ):
	with open (file, "r") as myfile:
    		return (myfile.read().replace('\n', '')).lower()

def getStringFromArray( array ):
	return str(array).replace("[","").replace(",","").replace(" ","").replace("'","").replace("]","")

def encryptTextRandomly( text, alphabet ):
	key=alphabet[:]
	random.shuffle(key)

	cipher=dict(zip(alphabet,key))

	#print cipher

	#return [cipher[x] for x in text]   returns array, but we want string
	
	encryptedText=""
	for x in text:
		encryptedText+=cipher.get(x)
	
	return encryptedText

### functions to count chars ###
def countLetterOccurenceAtAll( text, alphabet ):
	amountCharsAtAll=len(text)
	letterOccurencesAtAll=[0.0]*len(alphabet)
	c1=0

	for x in alphabet:
		c2=text.count(x)
		letterOccurencesAtAll[c1]=(c2/(amountCharsAtAll*1.0))*100
		c1+=1

	return letterOccurencesAtAll

def countLetterOccurenceTwice( text, alphabet ):
	temp=""
	doubleLetters=""

	for x in text:
		if temp == "":
			temp = x
		else:
			if x == temp:
				doubleLetters+=x
		
		temp = x

	letterOccurencesTwice=[0]*len(alphabet)
	c=0
	for x in alphabet:
		letterOccurencesTwice[c]=(doubleLetters.count(x)/(len(doubleLetters)*1.0))*100
		c+=1

	return letterOccurencesTwice

def countLetterOccurenceAtStart( text, alphabet):
	startLetters=""
	foo=1

	for x in text:
		# start
		if foo:
			startLetters+=x
			global foo
			foo=0
		if x == " ":
			global foo
			foo=1

	letterOccurenceAtStart=[0]*len(alphabet)
	c=0
	for x in alphabet:
		letterOccurenceAtStart[c]=(startLetters.count(x)/(len(startLetters)*1.0))*100
		c+=1

	return letterOccurenceAtStart

def countLetterOccurencePerWord( text, alphabet):
	words = text.split()

	amountWords=len(words)
	amountCharsAtAll=len(text)

	letterOccurencesAtAllAbsoulte=[0.0]*len(alphabet)
	letterOccurencesPerWord=[0.0]*len(alphabet)

	c=0
	for x in alphabet:
		letterOccurencesAtAllAbsoulte[c]=text.count(x)*1.0
		c+=1

	c=0
	for x in alphabet:
		letterOccurencesPerWord[c]=(letterOccurencesAtAllAbsoulte[c]*1.0/amountWords)*100.0
		c+=1

	return letterOccurencesPerWord

# function to compare all occurences at all to figured out which is the blank,
# because it's the character with the biggest occurence.
def searchBlank(lettList):

	blankIs=""
	biggestAmountRightNow=0.0

	for x in letterList:
		if x.occurenceAtAll > biggestAmountRightNow:
			biggestAmountRightNow = x.occurenceAtAll
			blankIs= x.letter

	return blankIs

def setPhase2Occurences(letterList, arrayOccurenceAtStart, arrayOccurencePerWord):
	c=0
	for x in letterList:
		setattr(x, "occurenceAtStart", arrayOccurenceAtStart[c])
		setattr(x, "occurencePerWord", arrayOccurencePerWord[c])
		c+=1
		
	return letterList

### statistics ###
oneLetter={'6.89':'a','1.35':'b','1.91':'c','3.78':'d','10.03':'e',
		   '2.09':'f','1.71':'g','4.87':'h','5.30':'i','0.07':'j',
		   '0.59':'k','3.47':'l','1.82':'m','5.76':'n','6.52':'o',
		   '1.47':'p','0.09':'q','4.88':'r','5.21':'s','7.40':'t',
		   '2.23':'u','0.76':'v','1.96':'w','0.12':'x','1.51':'y',
		   '0.03':'z','18.12':' ',}

twoLetters={'0.27':'a','.027':'b','1.9':'c','0.83':'d','13.05':'e','4.17':'f','5.00':'g','0.0':'h','0.0':'i',
			'0.0':'j','0.0':'k','24.17':'l','1.11':'m','4.72':'n','11.39':'o','4.44':'p','0.00':'q','5.55':'r',
			'12.78':'s','10.28':'t','0.0':'u','0.0':'v','0.0':'w','0.0':'x','0.0':'y','0.0':'z','0.0':' ',}

letterAtStart={'12.62':'a','4.74':'b','3.41':'c','3.75':'d','1.53':'e','4.62':'f','1.76':'g','6.18':'h','5.49':'i',
				'0.14':'j','.38':'k','2.95':'l','3.29':'m','2.31':'n','8.28':'o','3.15':'p','0.25':'q','2.51':'r',
				'5.72':'s','16.66':'t','1.47':'u','0.55':'v','7.42':'w','0.00':'x','0.81':'y','0.00':'z','0.00':' ',}


letterPerWord={'38.03':'a','7.45':'b','10.53':'c','20.88':'d','55.41':'e','11.55':'f','9.44':'g','26.88':'h','29.22':'i',
				'0.38':'j','3.26':'k','19.17':'l','10.04':'m','31.79':'n','35.98':'o','8.14':'p','0.52':'q','26.94':'r',
				'28.76':'s','40.80':'t','12.33':'u','4.22':'v','10.83':'w','0.64':'x','8.32':'y','0.144':'z','100':' ',}


wordListEnglish="the be to of and a in that have i it for not on with he as you do at this but his by from they we say her she or an will my one all would there their what so up out if about who get which go me when make can like time no just him know take people into year your good some could them see other than then now look only come its over think also back after use two how our work first well way even new want because any these give day most us"


#letterdictTemplate{'':'a','':'b','':'c','':'d','':'e','':'f','':'g','':'h','':'i',
#					'':'j','':'k','':'l','':'m','':'n','':'o','':'p','':'q','':'r',
#					'':'s','':'t','':'u','':'v','':'w','':'x','':'y','':'z',' ':'',}
#


### the actual work flow

alphabet=[chr(x+97) for x in range(26)]
alphabet.append(" ")

# this will be handled later
#
#decryptFile=input("please enter path of file to decrypt?")
#decryptFile = "test"
#print "you typed", decryptFile


## let's start first we will parse the file and count occurenceAtAll and occurenceTwice
#textToDecrypt=parseTextFileToString("analyseEnglishPrepared.txt")
textToDecrypt=encryptTextRandomly(parseTextFileToString("analyseEnglishPrepared.txt"), alphabet)

# getting occurence phase 1
occurenceAtAll=countLetterOccurenceAtAll(textToDecrypt ,alphabet)
occurenceTwice=countLetterOccurenceTwice(textToDecrypt, alphabet)

# creating objects 
aL = letter("a",occurenceAtAll[0], occurenceTwice[0])
bL = letter("b",occurenceAtAll[1], occurenceTwice[1])
cL = letter("c",occurenceAtAll[2], occurenceTwice[2])
dL = letter("d",occurenceAtAll[3], occurenceTwice[3])
eL = letter("e",occurenceAtAll[4], occurenceTwice[4])
fL = letter("f",occurenceAtAll[5], occurenceTwice[5])
gL = letter("g",occurenceAtAll[6], occurenceTwice[6])
hL = letter("h",occurenceAtAll[7], occurenceTwice[7])
iL = letter("i",occurenceAtAll[8], occurenceTwice[8])
jL = letter("j",occurenceAtAll[9], occurenceTwice[9])
kL = letter("k",occurenceAtAll[0], occurenceTwice[10])
lL = letter("l",occurenceAtAll[11], occurenceTwice[11])
mL = letter("m",occurenceAtAll[12], occurenceTwice[12])
nL = letter("n",occurenceAtAll[13], occurenceTwice[13])
oL = letter("o",occurenceAtAll[14], occurenceTwice[14])
pL = letter("p",occurenceAtAll[15], occurenceTwice[15])
qL = letter("q",occurenceAtAll[16], occurenceTwice[16])
rL = letter("r",occurenceAtAll[17], occurenceTwice[17])
sL = letter("s",occurenceAtAll[18], occurenceTwice[18])
tL = letter("t",occurenceAtAll[19], occurenceTwice[19])
uL = letter("u",occurenceAtAll[20], occurenceTwice[20])
vL = letter("v",occurenceAtAll[21], occurenceTwice[21])
wL = letter("w",occurenceAtAll[22], occurenceTwice[22])
xL = letter("x",occurenceAtAll[23], occurenceTwice[23])
yL = letter("y",occurenceAtAll[24], occurenceTwice[24])
zL = letter("z",occurenceAtAll[25], occurenceTwice[25])
blank = letter(" ",occurenceAtAll[26], occurenceTwice[26])

# creating list
letterList=[aL,bL,cL,dL,eL,fL,gL,hL,iL,jL,kL,lL,mL,nL,oL,pL,qL,rL,sL,tL,uL,vL,wL,xL,yL,zL,blank]

# determine blank and setting it
blankSearch=searchBlank(letterList)

for x in letterList:
	if x.letter == blankSearch:
		x.actualLetter = 1
#### probably some checks here, cuz the "e" could fuck shit up.

# create decrypted text with real blanks
textToDecryptBlanksSolved=textToDecrypt.replace(blankSearch," ")

## blank improven

#print textToDecrypt
print textToDecryptBlanksSolved

arrayOccurenceAtStart=countLetterOccurenceAtStart(textToDecryptBlanksSolved, alphabet)
arrayOccurencePerWord=countLetterOccurencePerWord(textToDecryptBlanksSolved, alphabet)

letterList = setPhase2Occurences(letterList, arrayOccurenceAtStart, arrayOccurencePerWord)


error = 1.5

c=0
for aa in letterList:

	c1=0
	for bb in oneLetter:
		
		if aa.occurenceAtAll+error > float(bb) and aa.occurenceAtAll-error < float(bb):
			letterList[c].candidatsAtAll.append(oneLetter.get(bb))
		c1+=1

	c1=0
	for cc in twoLetters:
		if aa.occurenceTwice+error > float(cc) and aa.occurenceTwice-error < float(cc):
			letterList[c].candidatsTwice.append(twoLetters.get(cc))
		c1+=1

	c1=0
	for dd in letterAtStart:
		if aa.occurenceAtStart+error > float(dd) and aa.occurenceAtStart-error < float(dd):
			letterList[c].candidatsAtStart.append(letterAtStart.get(dd))
		c1+=1

	c1=0
	for ee in letterPerWord: 
		if aa.occurencePerWord+error > float(ee) and aa.occurencePerWord-error < float(ee):
			letterList[c].candidatsPerWord.append(letterPerWord.get(ee))
		c1+=1

	c+=1


#for foo in letterList:
#	print foo.letter
#	print foo.occurenceAtAll, foo.occurenceTwice, foo.occurencePerWord, foo.occurenceAtStart
#	print foo.candidatsAtAll, foo.candidatsTwice, foo.candidatsPerWord, foo.candidatsAtStart
#	print "-----"

## works pretty well!  now just a ranking of all candidats afterwards we will create the permutations, which will then bruteforced and wordlist
# checked, if it hits anything the permutation a.k.a cipher will be printed after an example of the text.


for x in letterList:
	x.createCandidates(alphabet)

#	print x.letter
#	print x.candidats4Hits
#	print x.candidats3Hits
#	print x.candidats2Hits
#	print x.candidats1Hit
#	print "-----------"

#buildPermutationsFor4Hits(letterList, alphabet)

allPermutations=[]
	
OnePermutation={'a':'','b':'','c':'','d':'','e':'','f':'','g':'','h':'','i':'',
					'j':'','k':'','l':'','m':'','n':'','o':'','p':'','q':'','r':'',
					's':'','t':'','u':'','v':'','w':'','x':'','y':'','z':'',' ':'',}

tempPerm = OnePermutation.copy()
#print tempPerm


## first we put the stars in the permutation start, but only the once which occure once   ## here the q fucks up
tempCheck=""
gettingDoubles=""

for a in letterList:
	if len(a.candidats4Hits) == 1:# and a.candidats4Hits != :
		if tempCheck.count(a.candidats4Hits[0]) == 0:
			tempPerm[a.letter]=a.candidats4Hits[0]
			tempCheck+=a.candidats4Hits[0]
		else:
			gettingDoubles+=a.candidats4Hits[0]
			#print tempCheck.count(a.letter)
			#print tempCheck

# resetting double chars
for a in alphabet:
	if gettingDoubles.count(a) > 0:
		for b in alphabet:
			if tempPerm.get(b) == a:
				tempPerm[b] = ""

#print gettingDoubles
#print tempPerm

#allPermutations.append(tempPerm) FOR ALL DOUBLEHITS 4 
#####################################################################

# now the we iterate over the letters which have two letters at 4hits very unique!!!  ## here the c and m fuck shit up
# and copy the tempPerm for each occurence

amountDoubles=0
letterDoubles=""
for a in letterList:
		if len(a.candidats4Hits) == 2:
			amountDoubles+=1
			#print getStringFromArray(a.candidats4Hits)
			#print letterDoubles.count(str(a.candidats4Hits))
			if letterDoubles.count(getStringFromArray(a.candidats4Hits)) == 0:
				letterDoubles+=getStringFromArray(a.candidats4Hits)

# if no doubles available we set to one, in order to got at least one array
if amountDoubles == 0:
	amountDoubles=1

for i in range(amountDoubles):
	allPermutations.append(tempPerm.copy()) # never forget to make a deep copy bro!!!!

for a in letterList:
	x = len(a.candidats4Hits)
	if x == 2:
		for i in range(x):
			unset2=1
			counter=0
			while unset2:
				if getStringFromArray(allPermutations[counter]).count(a.candidats4Hits[i]) == 1 and allPermutations[counter][a.letter] == "":
					allPermutations[counter][a.letter]=a.candidats4Hits[i]	
					unset2=0
				counter+=1	

#now we will fill the 3 Hits
# determining maximum chars for one letter at 3 Hits
maxAmount3Hits=0
for a in letterList:
	x=len(a.candidats3Hits)
	if x > maxAmount3Hits:
		maxAmount3Hits=x

#print allPermutations

for i in range(maxAmount3Hits):

	i+=1
	if i == 1:
		## first setting only the one candidats
		amountLetters3HC=0
		letters3HC=""

		for a in letterList:
			if len(a.candidats3Hits) == 1 and allPermutations[0][a.letter] == "": 
				amountLetters3HC+=1
				letters3HC+=a.candidats3Hits[0]
		
		counter=0
		for x in allPermutations:
			for a in letterList:
				if len(a.candidats3Hits) == 1 and allPermutations[counter][a.letter] == "" and letters3HC.count(a.candidats3Hits[0]) == 1:
					x[a.letter]=a.candidats3Hits[0] 
			counter+=1

		# now the doubles NOPE !!!
		# no now we set all actualLetter, and afterwards we iterate over each letter and if this is not already set, all the number 4 candidats, 
		# afterwards we got all permutations


for a in letterList:
	if allPermutations[0][a.letter] != "":
		a.actualLetter=1

## getting alreadySetChars
alreadySetChars=""
for a in letterList:
	if allPermutations[0][a.letter] != "":
		alreadySetChars+=allPermutations[0][a.letter]

#print alreadySetChars

for a in letterList:
	if not a.actualLetter:
		temp=getStringFromArray(a.candidats4Hits) + getStringFromArray(a.candidats3Hits) + getStringFromArray(a.candidats2Hits) + getStringFromArray(a.candidats1Hit )

		for x in alreadySetChars:
			temp=temp.replace(x, "")

		a.setLastCandidats(temp)

## concatenating all lastCandidats to determine if one char occures only one, that one is for sure right.
allLastCandidats=""
for a in letterList:
	allLastCandidats+=a.lastCandidats

for a in letterList:
	for x in a.lastCandidats:
		if allLastCandidats.count(x)==1:
			#print a.letter, x, a.lastCandidats
			for y in allPermutations:
				y[a.letter]=x
				a.lastCandidats=" "
				a.actualLetter=1	# this line costed 25 minutes, because you forgot !!! :D

	#print a.letter, a.lastCandidats 


# until now everything works pretty well, but i could improve the blank check, because for 5 % or so ;) it's determines the e instead of the blank.
# so to evaluate this, we could twice calculate the second phase and so we will know what really is the blank and the "e" ofcourse as well.

# now the big check, where every letter will be evaluated by it statistics. so we will pass the letterList to a function.
# which will set all it's candidats.


# so jetzt wirklich nur noch alle permutationen erstellen und advance brute forcen und anschliessend mit woerter buch abgleichen.
# alternativ koennte man hier einen switch einbauen, der direkt zu decrypted und per autocorrect function die restlichen cipher findet.


## now we will iterate over each character which will take all permuations and multiply each of them with there candidats amount and fill them.
## in the end we delete empty permutations in fact of already set letters. (describe more!)


def generatePermutations(permutationsArray, obj):
	
	newPermutations = [[0 for xa in range(len(obj.lastCandidats))] for xa in range(len(permutationsArray))]
	
	for xa in range(len(permutationsArray)):
		for ya in range(len(obj.lastCandidats)):
			newPermutations[xa][ya] =  permutationsArray[xa].copy()
			newPermutations[xa][ya][obj.letter]=obj.lastCandidats[ya]

	return newPermutations

def generatePermutations2(permutationsArray, obj):
	

	#print "generatePermutations2-Function: \n", permutationsArray

	newPermutations = [[0 for xa in range(len(obj.lastCandidats))*len(permutationsArray[0])] for xa in range(len(permutationsArray))]

	#print obj.lastCandidats

	for x in range(len(permutationsArray)):
		counter=0	

		for z in range(len(permutationsArray[0])):

			counter2=0
			for y in range(len(obj.lastCandidats)):

				if str(permutationsArray[x][z]).count(obj.lastCandidats[counter2]) < 2 and permutationsArray[x][z] != 0:
					newPermutations[x][counter] = permutationsArray[x][z].copy()		# AGAIN NEVER FORGET THE COPY DUDE....self
					newPermutations[x][counter][obj.letter]=obj.lastCandidats[counter2]
					#print counter
					#print newPermutations[x][counter]


				counter+=1
				counter2+=1

			# hier jetzt noch die setFunktion rein, und dann war es das bujaka :D
			# Hier drinnen stimmt das noch alles, aber was ich uebergebe ist shice.... maaaahh

	return newPermutations

#check=1
#bla=0
#for ab in letterList:
#	if not ab.actualLetter:
#		if check:
#			print ab.letter, " FIRST ONE "
#			bla=generatePermutations(allPermutations, ab)	
#			check=0
#		else:
#			bla=generatePermutations2(bla, ab)
#			print ab.letter
#
#print bla

#search first letter which is not set
c=0
result=0
for ab in letterList:
	if not ab.actualLetter:
		#print ab.letter
		result=c
		break
	c+=1

def generateRestOfPossibilities (letterList, permutations):

	#print "start recursive"
#	#for x in letterList:
#	#	print x
#
	#print "....."
	#print permutations
	#"__________________________________________________________________________________________"	

	counter=0
	for ab in letterList:
		if not ab.actualLetter:
			counter+=1

	
	if counter > 1:
		for ab in letterList:
			if not ab.actualLetter:
				ab.actualLetter=1
				return generateRestOfPossibilities( letterList, generatePermutations2(permutations, ab) )
	else:
		for ab in letterList:
			if not ab.actualLetter:
				ab.actualLetter=1
				return generatePermutations2(permutations, ab)		
	
	#ab.actualLetter=1
			
	#return generateRestOfPossibilities(letterList, generatePermutations2(permutations, ab))

#print bla
#print len(bla)
#print len(bla[0])
#print len(bla[1])#

bla=generatePermutations(allPermutations, letterList[result])
letterList[result].actualLetter=1

#pprint.pprint(allPermutations)
#print "-----"
#print bla

#hallo=generateRestOfPossibilities(letterList, bla)
#
#print("ffef")
#print len(hallo)
#print len(hallo[0])
#print len(hallo[1])
#
#
## now bruteforce the shit out of it :)
#
#amountCiphers=0
#for i in range(len(hallo[0])):
#	if hallo[0][i] != 0:
#		print hallo[0][i]
#		amountCiphers+=1
#
#for i in range(len(hallo[1])):
#	if hallo[1][i] != 0:
#		print hallo[1][i]
#		amountCiphers+=1
#
#print amountCiphers
#print len(hallo[0])+len(hallo[1])



# check for all chars
#print aL
#print bL
#print cL
#print dL
#print eL
#print fL
#print gL
#print hL
#print iL
#print jL
#print kL
#print lL
#print mL
#print oL
#print pL
#print qL
#print rL
#print sL
#print tL
#print uL
#print vL
#print wL
#print xL
#print yL
#print zL
