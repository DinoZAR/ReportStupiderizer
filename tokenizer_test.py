# Now it will read an open-source thesaurus and organize its data into
# manageable chunks in memory

# Each entry will have the following format
# [word, [alternate, alternate2, alternate3, ...]]

masterThesaurus = []

file = open("th_en_US_v2.dat", "r")

doing = True

# Remove the first header
read = file.readline()

while doing:
    read = file.readline()
    print read
    
    if read == '':
        doing = False
    else:
        # Read the contents into my master thesaurus
        myList = []
        myWord, numWords = read.split('|')[0], int(read.split('|')[1])
        
        myList.append(myWord)
        
        newList = []
        
        for word in range(numWords):
            newWords = file.readline()
            newWords = newWords.split("|")
            newWords = newWords[1:]
            
            # Clean every one of its subwords for explanatory thingies
            for i in range(len(newWords)):
                newWords[i] = newWords[i].replace("(generic term)", "")
                newWords[i] = newWords[i].replace("(similar term)", "")
                newWords[i] = newWords[i].replace("(related term)", "")
                newWords[i] = newWords[i].strip()
                
                # After being cleaned, be added to the list
                newList.append(newWords[i])
            
        # Add the list of words to my new word entry
        myList.append(newList)
        
        # Append it to the master thesaurus
        masterThesaurus.append(myList)
        
print "Done!"