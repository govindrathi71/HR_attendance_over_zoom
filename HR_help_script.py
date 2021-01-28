
import sys
import pandas, re
participant=list()
i=0
k=0
DURATION_VAR=int(sys.argv[1])
print(DURATION_VAR)
with open("myfile.txt") as f_in:   
    for line in f_in:
        if (i%2==0):
            k=str(line)
            i+=1
        else:
            #print(k)
            participant.append((k.rstrip().lower() + ' ' + line.rstrip().lower()).split())
            i+=1
df = pandas.read_csv('test_project.csv')
#print(df)
zoom_party=list()
for ind in df.index:
    if(df['Duration (Minutes)'][ind]>DURATION_VAR):
        zoom_party.append((re.split('[- ]',df['Name (Original Name)'][ind].lower())))


#print(zoom_party)
#print(participant)
# for p in participant:
#     for word in p:
#         print(p)


for p in participant:
    desired_entry=list()
    for zoom_p in zoom_party:
        
        mx_match_sum=0
        match_sum=0
        for every_word in p:
            if every_word in zoom_p:
                match_sum+=1
        if(match_sum>mx_match_sum and match_sum!=0):
            mx_match_sum=match_sum
            if(mx_match_sum>1): desired_entry=p
    if(len(desired_entry)): 
        print(desired_entry, "ATTENDED")
    else:
        print(p, "****************")






        