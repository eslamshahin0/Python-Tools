from pafy import new
vid_url=input('Enter your YouTube video URL : ')
DV = new(vid_url)
print ('\n',DV.title)
VidQuality=DV.streams
SoundQuality=DV.audiostreams
print('=================================================')
print('\nThe Avilable Video Qualites is : \n')
for i in range(len(VidQuality)):
    print(i+1,'- ',VidQuality[i])

print('\n\nThe Avilable Sounds Qualites is : \n')
for i in range(len(SoundQuality)):
    print(i+1,'- ',SoundQuality[i])

print('\n================================================')
print('To Download Video press 1 , to download audio press 2 : ')
flag=int(input())
dwon=int (input ('\nChose quality to download : '))

if flag==1 :
    VidQuality[dwon-1].download()
elif flag==2:
    SoundQuality[dwon-1].download()
else :
    print('Error')
    
