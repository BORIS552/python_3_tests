from collections import defaultdict

class Business:
  def __init__(self,name,location,id):
    self.name = name
    self.location = location
    self.id = id

class Chain:
  def __init__(self,name,freq):
    self.name = name
    self.freq = freq

def getChain(businessList,targetLocation):
  chainData = {}
  for item in businessList:
    name,location,id = item.name,item.location,item.id
    if location == targetLocation:
      if name+'-'+str(id) in chainData.keys():
        chainData[name+'-'+str(id)].freq+=1
      else:
        chainData[name+'-'+str(id)]=Chain(name,1)
  return [(v.name,v.freq) for v in sorted(chainData.values(),key = lambda x: (x.freq,x.name))]
  
    
if __name__=='__main__':
  businessList = list()
  for _ in range(5):
    businessList.append(Business('coke','india',1))
  for _ in range(3):
    businessList.append(Business('coke','italy',1))
  for _ in range(4):
    businessList.append(Business('pepsi','india',2))
  for _ in range(3):
    businessList.append(Business('pepsi','india',6))
  for _ in range(5):
    businessList.append(Business('dabur','india',3))
  for _ in range(5):
    businessList.append(Business('raw','india',4))
  for _ in range(4):
    businessList.append(Business('pepsi','argentina',2))
  print(getChain(businessList,'india'))
  print(getChain(businessList,'italy'))
  print(getChain(businessList,'argentina'))
