import re
#print(re.sub('[ad]','*','abc abcd abcdead'))

#print(re.sub('ab','*','abc adabc addba'))

#print(re.sub('[abc][1234]','*','a1+b2+c3+d4'))

#print(re.sub('A.B','*','A*B A#B ACB ACCB'))

#print(re.sub('AB+','*','ABB ABC ABBBBBC AC ABAAAA'))

#print(re.sub('AB{3,6}','*','ABB ABBB ABBBB ABBBBBBBBB'))

#print(re.sub('^ABC','*','ABCDEFG'))

#print(re.sub('ABC$',"*",'ABCDEFAB'))

#print(re.sub('31\+','*','AB+C 31+C'))

#print(re.sub('\d','*','3+14=17'))

#print(re.sub('\D','A','3+14=17'))

#print(re.sub('\w','*','This is a test. Or is it?'))

#print(re.sub('\W','*','This is a test. Or is it?'))

#print(re.sub('\s','*','This is a test. Or is it?'))

#print(re.sub('\S','*','This is a test. Or is it?'))

#print(re.sub('the(?=cat)','*','the dog and the cat'))

#print(re.sub(r'(?<=)the','*','Athens is the capital'))

#print(re.sub('(?<!\w)[Tt]he(?!\w)','*','The cat is on the lathe there'))

#print(re.sub('(?i)ab','*','ab AB'))

#print(re.search('ab','Here is an absolute string'))

#print(re.match('Here is an absolute string','Here is an absolute string'))
