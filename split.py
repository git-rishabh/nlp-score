import pickle
# with open("questions4.dump","rb") as f1:
# 	answers = pickle.load(f1)

# a1=dict()
# a2=dict()
# c=0
# length=len(answers)
# print length
# for i in answers.keys():
# 	if(c<=length/2):
# 		a1[i]=answers[i]
# 	else:
# 		a2[i]=answers[i]
# 	c=c+1

# print len(a1)
# print len(a2)
# with open("q1.dump","wb") as f2:
# 	pickle.dump(a1,f2)
# with open("q2.dump","wb") as f3:
# 	pickle.dump(a2,f3)
# 

with open("q1.dump","rb") as f2:
	q1=pickle.load(f2)
with open("q2.dump","rb") as f3:
	q2=pickle.load(f3)
q=[]

for i in q1.keys():
	q[i]=q1[i]
for i in q2.keys():
	q[i]=q2[i]

with open("questions4.dump","wb") as f:
	pickle.dump(q,f)

# 

with open("a1.dump","rb") as f2:
	a1=pickle.load(f2)
with open("a2.dump","rb") as f3:
	a2=pickle.load(f3)
a=[]

for i in a1.keys():
	a[i]=a1[i]
for i in a2.keys():
	a[i]=a2[i]

with open("answer_texts_by_question_id4.dump","wb") as f:
	pickle.dump(a,f)
