import pickle
from Question import Question
from loc_score import *

with open("mid_so_answer_texts_by_question_id4.dump","rb") as f1:
	answers = pickle.load(f1)

# print len(answers)
# for i in answers.keys():
# 	print len(answers[i])
# print len(answers[0])
nlp_score_list=dict()
with open("mid_so_questions4.dump","rb") as f2:
	questions = pickle.load(f2)
print "Dump Read ..."
f=open("mid_so_nlp_score.txt","wb")

for ques_id in questions.keys():
	print ques_id,
	tot_score=0
	try:
		ans_list=answers[ques_id]
		score = nlp_score(ans_list[0])
		if(score!=-1):
			tot_score = score
	except:
		pass
	final_score=tot_score
	nlp_score_list[ques_id]=final_score
	print final_score
	# with open("nlp_score_list.dump","wb") as f3:
	# 	pickle.dump(nlp_score_list,f3)
	f.write(ques_id+" "+str(final_score)+"\n")


f.close()
