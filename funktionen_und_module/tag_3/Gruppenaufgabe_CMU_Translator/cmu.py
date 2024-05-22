import urllib.request
# http://www.speech.cs.cmu.edu/cgi-bin/cmudict
url = "http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict.0.7a"
data = urllib.request.urlopen(url)

cmu_dict = {}
for line in data:
    word, *phonetic = line.decode("utf-8").strip().split()
    cmu_dict[word] = phonetic

print(cmu_dict)
