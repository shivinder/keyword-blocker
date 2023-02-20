#!/usr/bin/env python3
# Script to mask supplied keywords from target text files

import argparse
import re

# load the keywords from the keywords file. by default the name of the keywords file is assumed to be keywords.txt
file_keywords = 'keywords.txt'
list_keywords = []  # initialise a empty list which will eventually be loaded with the supplied keywords from the keywords file
with open(file_keywords) as fp_keywords:
  for row_in_keywords_file in fp_keywords:
    list_keywords.append(str(row_in_keywords_file).strip())
  print(f"{count(list_keywords)} keywords loaded from {file_keywords}.")

# load the target text file in write mode
file_target = 'target.txt'
with open(file_target, "w") as fp_target:
  text_target=fp_target.read()

  for i in keywords:
    if re.search(r'\b{}\b'.format(i),text_target):
      print i