total_lambs=4
generous_give = 0
stingy_give = 2 #assume already give to the first two most junior henchman one each
generous_count=0
stingy_count = 2# already distributed to tywo most junior henchman
#print(range(total_lambs))
#counting recipients for generous giving, aka elements in geometric sequence
if total_lambs<4:
    print(0)
#elif total_lambs ==4:
    #print(1)

else:
    while generous_give<=total_lambs:
        #print('this is i',i)
        #print(generous_give)
        #print('this is gg',generous_give)
        generous_give+=pow(2,generous_count)
        #print(generous_give)
        generous_count+=1
        #if generous_give>total_lambs:
            #generous_count-=1
            #break
    #print(generous_count)

    #counting recipients for stingy giving, aka elements in fibonacci sequence
    give_1=1#for most junior henchman
    give_2=1#for second most junior henchman
    while stingy_give<=total_lambs:
        give_3=give_1+give_2#for immediate superior of 1 and 2
        #print(give_3)
        stingy_give=stingy_give+give_3
        give_1=give_2
        give_2=give_3
        stingy_count+=1
        #print(give_3)
        #print(stingy_give)
        #if stingy_give>total_lambs:
            #stingy_count-=1
            #break
    #print(generous_count)
    #print(stingy_count)
    print(stingy_count-generous_count)