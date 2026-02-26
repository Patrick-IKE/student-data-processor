def lower_score(name_score):
    low_name = min(name_score, key=name_score.get)
    low_score = name_score[low_name]
    return low_score

def higher_score(name_score):
    high_name = max(name_score, key=name_score.get)
    high_score = name_score[high_name]
    return high_score

def average_score(score_list):
    avg = sum(score_list)/len(score_list)
    return f"{avg:.2f}"

def total_score(scores_list):
    total = 0
    for x in scores_list:
        total += x
    return total

def above_average(name_score):
    ag = name_score.values()
    ag = sum(ag)/len(ag)
    ag = f"{ag:.2f}"
    above_average_pupils = []
    for name, score in name_score.items():
        if score > float(ag):
            above_average_pupils.append((name, score))
    return above_average_pupils

def most_occurring():
    pass
