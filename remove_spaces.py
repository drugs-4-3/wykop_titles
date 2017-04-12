
clean_lines = []
with open("results.txt", "r") as f:
    lines = f.readlines()
    clean_lines = [l.strip() for l in lines if l.strip()]

with open("results_striped.txt", "w") as f:
    f.writelines('\n'.join(clean_lines))

print("Spaces removed succsesfully!")