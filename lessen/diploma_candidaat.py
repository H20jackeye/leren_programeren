# the candidate must have either a diploma or experience
hasdiploma = True
hasexperience = False

# the candidate must speak either English or German
MastersEnglish = False
MastersGerman = False

#is candidate fit for the job
fitforjob = (hasdiploma or hasexperience) and (MastersEnglish or MastersGerman)

if fitforjob:
    print('candidate is fit for the job')
else:
    print ('candidate is not fit for the job')
