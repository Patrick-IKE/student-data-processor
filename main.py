from working import *
with open("data1.csv", "r") as saved_file:
    stud_records = saved_file.readlines()
print(stud_records)
name_score = {}
total_score = 0
scores_list = []
for x in stud_records:
    audit = x.strip().split(",")
    full_name = audit[0] + audit[1]
    score = int(audit[2])
    total_score += score
    scores_list.append(score)
    name_score[full_name] = score

#average_score(scores_list)
print(total_score)
print(scores_list)
avg_score = average_score(scores_list)
print(avg_score)
low_name = min(name_score, key=name_score.get)
low_score = name_score[low_name]
print(low_score)
high_name = max(name_score, key=name_score.get)
high_score = name_score[high_name]
print(high_score)



print(f"{low_name} is the student with the lowest score {low_score}.")
print(f"{high_name} is the student with the highest score {high_score}.")
print(f"The total score for the student is {total_score}.")
print(f"The average score for the student is {avg_score}.")
print(name_score)
print(above_average(name_score))