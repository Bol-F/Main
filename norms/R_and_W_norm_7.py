with open("csv_norm_7", "r") as file:
    lines = file.readlines()
updated_lines = []
for line in lines:
    name, grade = line.rsplit(" ", 1)
    grade = int(grade)
    if grade < 80:
        grade += 5
    updated_lines.append(f"{name} {grade}\n")

with open("csv_norm_7", "w") as file:
    file.writelines(updated_lines)