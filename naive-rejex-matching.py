import re

collection = [
                'django_migrations.py',
                'django_admin_log.py',
                'main_generator.py',
                'migrations.py',
                'api_user.doc',
                'user_group.doc',
                'accounts.txt',
              ]

def naive_rejex_match( userinput , collection ):
  #convert userinput into regu_exp
  #like userinput = 'abc'
  #then conveted to regu_exp = '.*a.*b.*c'
  regu_exp = ".*" + ".*".join(userinput)  
  pattern = re.compile(regu_exp)
  suggestions = []
  for i in collection:
    if pattern.search(i):
      suggestions.append(i)
  return suggestions
if __name__ == "__main__":
  print naive_rejex_match("accounts",collection)
