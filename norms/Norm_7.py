with open("students.txt", "r") as f:
    content = f.read()

updated_lines = []
lines = content.split("\n")

for i in lines:
    if "-" in i:
        name, score_str = i.split("-")
        score = int(score_str)
        if score < 80:
            score += 5
        updated_lines.append(f"{name} - {score}")
    else:
        updated_lines.append(i)

with open("students.txt", "w") as f:
    f.write("\n".join(updated_lines))
