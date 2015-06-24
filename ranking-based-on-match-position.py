import re

colletion = [
              'django_migrations.py',
                'django_admin_log.py',
                'main_generator.py',
                'migrations.py',
                'api_user.doc',
                'user_group.doc',
                'accounts.txt',
            ]

def ranking_based(userinput,colletion):
  reg_exp = ".*" + ".*".join(userinput)
  pattern = re.compile(reg_exp)
  suggestions = []
  for item in colletion:
    #sort the suggestion list in Alphabet order by using built-in function 
    #sorted()
    #'_' is just a variable name and it's conventional in python to use _
    #for throwaway variables, It's just indicate that the loop variable isn't actually used
    if pattern.search(item):
      suggestions.append((pattern.search(item).start(),item))
  return [x for _,x in sorted(suggestions)]

if __name__ == "__main__":
  print ranking_based('mig',colletion)