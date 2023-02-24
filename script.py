#!/usr/bin/env python3
# Script to mask supplied keywords from target text files

import re

def load_the_keywords(file_keywords):
  """
  load the keywords from the keywords file. by default the name of the keywords file is assumed to be keywords.txt
  """
  list_of_loaded_keywords = []  # initialise a empty list which will eventually be loaded with the supplied keywords from the keywords file
  with open(file_keywords) as fp_keywords:
    for row_in_keywords_file in fp_keywords:
      list_of_loaded_keywords.append(str(row_in_keywords_file).strip())
    print(f"Keywords loaded from the {file_keywords} text file: {str(len(list_of_loaded_keywords))}\n")
    return list_of_loaded_keywords

def replace_keywords(list_of_loaded_keywords, redact_string, file_target):
  """
  get the list of loaded keywords from the text file and the file target and replace them.
  """
  # load the target text file in memory
  with open(file_target, "r") as fp_target:
    text_target = fp_target.read()

    for keyword in list_of_loaded_keywords:
      # replace the keywords one by one from the text loaded to the memory
      regex_pattern = re.compile(keyword, re.IGNORECASE)
      print(f"Replacing the keyword {keyword} in the file {file_target} ...")
      text_target = regex_pattern.sub(redact_string, text_target)
  
  # save the target file from the memory to the disk
  with open(file_target, "w") as fp_target:
    fp_target.write(text_target)
    print(f"{file_target} written to disk successfully.")

if __name__ == "__main__":
  redact_string = '[REDACTED]'
  file_target = 'target.txt'
  # load the keywords
  list_of_loaded_keywords = load_the_keywords('keywords.txt')

  # replace the loaded keywords from the file
  replace_keywords(list_of_loaded_keywords, redact_string, file_target)