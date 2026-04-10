tally_score = 0
question1 = input("who is luke skywalkers father\n->")
if question1 == ("anikin skywalker"):
    print("correct")
    tally_score +=1
else:
    print("incorect")

question2 = input("what color is yoda\n->")
if question2 == ("green"):
    print("correct")
    tally_score +=1
else:
    print("incorrect")
question3 = input("what is the name of harry potters owl\n->")
if question3 == ("headwig"):
    print("correct")
    tally_score +=1
else:
    print("incorrect")
question4 = input("what is the name ron weaslys rat\n->")
if  question4 == ("peter pettigrew"):
    print("correct")
    tally_score +=1
else:
    print("incorrect")
question5 = input("what is the name of the snake language in harry potter\n->")
if question5 == ("parseltongue"):
    print("correct")
    tally_score +=1 
else:
    print("incorrect")


print("final score", + tally_score,"/5")


