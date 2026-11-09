import re

with open("preproinsulin-seq.txt", "r") as file:
    raw_content = file.read()


cleaned_content = re.sub(r'ORIGIN|[0-9]+|//|\s+', '', raw_content)


cleaned_content = cleaned_content.lower()

with open("preproinsulin-seq-clean.txt", "w") as file:
    file.write(cleaned_content)

print(f"Cleaned sequence successfully saved!")
print(f"Total character count: {len(cleaned_content)}")


# Count char in preproinsulin file
with open("preproinsulin-seq-clean.txt", "r") as file:
    preproinsulin = file.read().strip()

# Extract amino acids 1 to 24 
lsinsulin = preproinsulin[0:24]

# Save the result 
with open("lsinsulin-seq-clean.txt", "w") as file:
    file.write(lsinsulin)

with open("lsinsulin-seq-clean.txt", "r") as file:
    saved_content = file.read().strip()

print(f"Saved sequence: {saved_content}")
print(f"Total character count: {len(saved_content)}")


with open("preproinsulin-seq-clean.txt", "r") as file:
    preproinsulin = file.read().strip()


binsulin = preproinsulin[24:54]

# Save the result
with open("binsulin-seq-clean.txt", "w") as file:
    file.write(binsulin)

with open("binsulin-seq-clean.txt", "r") as file:
    saved_content = file.read().strip()

print(f"Saved B-chain sequence: {saved_content}")
print(f"Total character count: {len(saved_content)}")

with open("preproinsulin-seq-clean.txt", "r") as file:
    preproinsulin = file.read().strip()


binsulin = preproinsulin[24:54]

# Save the result into binsulin-seq-clean.txt
with open("binsulin-seq-clean.txt", "w") as file:
    file.write(binsulin)

with open("binsulin-seq-clean.txt", "r") as file:
    saved_content = file.read().strip()

print(f"Saved B-chain sequence: {saved_content}")
print(f"Total character count: {len(saved_content)}")

with open("preproinsulin-seq-clean.txt", "r") as file:
    preproinsulin = file.read().strip()


cinsulin = preproinsulin[54:89]

with open("cinsulin-seq-clean.txt", "w") as file:
    file.write(cinsulin)

with open("cinsulin-seq-clean.txt", "r") as file:
    saved_content = file.read().strip()

print(f"Saved C-chain sequence: {saved_content}")
print(f"Total character count: {len(saved_content)}")


with open("preproinsulin-seq-clean.txt", "r") as file:
    preproinsulin = file.read().strip()


ainsulin = preproinsulin[89:110]

with open("ainsulin-seq-clean.txt", "w") as file:
    file.write(ainsulin)

with open("ainsulin-seq-clean.txt", "r") as file:
    saved_content = file.read().strip()

print(f"Saved A-chain sequence: {saved_content}")
print(f"Total character count: {len(saved_content)}")