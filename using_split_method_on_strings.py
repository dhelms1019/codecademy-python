authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# Split string by commas
author_names = authors.split(',')

# Create list of only authors' last names
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])

print(author_names)
print("\n")
print(author_last_names)