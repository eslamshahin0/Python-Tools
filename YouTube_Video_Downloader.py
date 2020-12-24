from pafy import new
#if you don't have this lib you should install it from pip
#run <pip install pafy > then < pip install youtube.dl > 


vid_url=input('Enter your YouTube video URL : ')	#get url
DV = new(vid_url)
print ('\n',DV.title) 	#print video titel
VidQuality=DV.streams	#get avilable video qualites
SoundQuality=DV.audiostreams	#get avilable sound qualites
print('=================================================')
print('\nThe Avilable Video Qualites is : \n')
for i in range(len(VidQuality)):
    print(i+1,'- ',VidQuality[i])	#printing differnt avilable video qualites

print('\n\nThe Avilable Sounds Qualites is : \n')
for i in range(len(SoundQuality)):
    print(i+1,'- ',SoundQuality[i])	#printing differnt avilable audio qualites

print('\n================================================')
print('To Download Video press 1 , to download audio press 2 : ')
flag=int(input())
dwon=int (input ('\nChose quality to download : '))

if flag==1 :
    VidQuality[dwon-1].download()	#start downloading the video in the same path of script
elif flag==2:
    SoundQuality[dwon-1].download()	#start downloading the audio in the same path of script
else :
    print('Error')
    
