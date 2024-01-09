def common_letters(string_one, string_two):
  letter_list = []
  for character in string_one:
    if character in string_two:
        if character not in letter_list:
          letter_list.append(character)
  return(letter_list)