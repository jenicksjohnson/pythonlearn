import numpy as np
import matplotlib.pyplot as plt
#
# N=5
# menMeans=(20,32,34,20,25)
# womenMeans=(25,32,34,20,25)
# ind=np.arange(N)
# width=0.35
# p1=plt.bar(ind,menMeans,width)   # xposition=ind,yposition=men data,blankspace width =width
# p2=plt.bar(ind,womenMeans,width,bottom=menMeans)
# plt.ylabel("Scores")
# plt.xlabel("Scores by group and gender")
# plt.xticks(ind,('G1','G2','G3','G4','G5'))
# plt.legend((p1,p2),('Men','Women'))
# plt.show()
# # #
# # yticks= to set a y range
#
# menMeans=(20,32,34,20,25)
# womenMeans=(25,32,34,20,25)
# menstd=(2,3,4,1,2)
# womenstd=(3,5,2,3,3)
# ind=np.arange(len(menMeans))
# width=0.35
# p1=plt.bar(ind,menMeans,width,yerr=menstd)
# p2=plt.bar(ind,womenMeans,width,yerr=womenstd,bottom=menMeans)
# plt.ylabel("Scores")
# plt.xlabel("Scores by group and gender")
# plt.xticks(ind,('G1','G2','G3','G4','G5'))
# plt.yticks(np.arange(0,81,10))
# plt.legend((p1,p2),('Men','Women'))
# plt.show()
#
# bar plots side by side
# menMeans=(20,32,34,20,25)
# womenMeans=(25,32,34,20,25)
# menstd=(2,3,4,1,2)
# womenstd=(3,5,2,3,3)
# ind=np.arange(len(menMeans))
# width=0.35
# p1=plt.bar(ind-.20,menMeans,width,yerr=menstd)
# p2=plt.bar(ind+.15,womenMeans,width,yerr=womenstd)
# plt.ylabel("Scores")
# plt.xlabel("Scores by group and gender")
# plt.xticks(ind,('G1','G2','G3','G4','G5'))
# plt.yticks(np.arange(0,81,10))
# plt.legend((p1,p2),('Men','Women'))
# plt.show()
#
#Horizontal Bar-we use plt.barh
menMeans=(20,32,34,20,25)
womenMeans=(25,32,34,20,25)
menstd=(2,3,4,1,2)
womenstd=(3,5,2,3,3)
ind=np.arange(len(menMeans))
width=0.35
p1=plt.barh(ind-.15,menMeans,width,xerr=menstd)
p2=plt.barh(ind+.15,womenMeans,width,xerr=womenstd)
plt.xlabel("Scores")
plt.ylabel("Scores by group and gender")
plt.yticks(ind,('G1','G2','G3','G4','G5'))
plt.xticks(np.arange(0,81,10))
plt.legend((p1,p2),('Men','Women'))
plt.show()
