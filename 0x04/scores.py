#!/usr/bin/python3
# a module that reads a txt file



def read_score(filename):
    total_score = 0
    count = 0
    scores_dict =  {}
    with open(filename, "r") as file:
        for line in file.readlines():
            clean_line = line.strip()
            if not clean_line:
                print(clean_line)
                continue
            else:
                name,score_str = clean_line.split (",")
                score = int(score_str)
                scores_dict[name] = score
                total_score += score
                count += 1
                if count > 0:
                    average = total_score / count
                else:
                    average = 0
    return  (scores_dict, average)


if __name__ == "__main__":
  result =  read_score("scores.txt")
  print(result)

