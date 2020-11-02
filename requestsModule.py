import requests # import requests mmodule
res = requests.get('https://automatetheboringstuff.com/files/rj.txt') # set variable and use rquests.get for data from a url
res.status_code # return a code of success or failure
len(res.text) # what is the text length
print(res.text[:500]) # print 500 characters of text (using a slice) from what is returned in the res object

res.raise_for_status() # raise an excpetion if download fails

playFile = open('RomeoAndJuliet.txt', 'wb') # create a new file object that can be written to
for chunk in res.iter_content(100000): # for loop breaking the text into chunks of 100000 bytes
    playFile.write(chunk) # while there are chunks left write text to the new file object

playFile.close() # save 
