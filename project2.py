def setCheck(db, candidateMap):
    for currentSet in db:
        #goes through and looks at each elements
        #need to find a way to do the element pairings
        #set multiplier?
        for element in currentSet:
            #element contains all the letters in order
            if element in candidateMap.keys():
                candidateMap[element]=candidateMap[element]+1
            else:
                candidateMap[element]=1


def createCandidate(db):
    #creates the set of all items
    result = set(x for l in db for x in l)
    dblist=list(result)
    print(dblist)
    return dblist

def setMultiply(db,elements,count):
      ckplus1=[]
      for f0element in elements:
          for ithset in db:
              f0element=set(f0element)
              ithset=set(ithset)
              res = ithset.union(f0element)
              #EXTRA CREDIT
              #for element in ithset:
                  #check map as specified in class

              #Option for full credit with

              if len(res) == count+1:
                  checkDuplicateSet(ckplus1,res)

      return ckplus1

    #form of c[{...},{...},...]
    #form of result {...}
def checkDuplicateSet(c, result):
    duplicate = False
    for element in c:
        if element == result:
            duplicate = True

    if duplicate == False:
        c.append(result)
def main():
    transDatabase = [['a','c','e'],['b','c','e'],['a','b','c','e'],['b','e','d']]
    frequencyList=[]
    candidateList=[]
    removeList=[]
    maxSetLength=0
    #creates list of
    uElement=createCandidate(transDatabase)
    for currentSet in transDatabase:
         if(len(currentSet)>maxSetLength):
             maxSetLength = len(currentSet)

    for index in range (maxSetLength):
        frequencyList.append(set())
        #number of sets
        setNum=len(frequencyList)
    #generate C(1) and F(1)
    candidateMap={}


    #I am trying to create the correct number of maps
    i=1
    while i <= setNum:
        candidateMap[i]={}
        setCheck(transDatabase, candidateMap[i])
        mult=setMultiply(transDatabase,uElement,i)
        #prints out all the possible sets
        print(mult)
        i=i+1


    # for i in range(setNum):
    #     candidateMap[i]={}
    #     print(candidateMap[i])

    for currentSet in transDatabase:
        for element in currentSet:
    #        print(element)
            if element in candidateMap.keys():
                candidateMap[element]=candidateMap[element]+1
            else:
                candidateMap[element]=1


    #  f1={i:candidateMap[i] for i in candidateMap if candidateMap[i]!=1}
    #  k1set=f1.keys()
    #     for element in k1set:
    #         prints all elements in the set
    #         print(element)
    # frequencyList.append(f1) #frequentList[0] are the single frequent items
    # print(frequencyList)
    # removeList.append({i:candidateMap[i] for i in candidateMap if candidateMap[i]==1})
        #Call the function that does
     #c = multiplySet(f_k,f_0,3)#use a variable instead of 3 for project
main()
