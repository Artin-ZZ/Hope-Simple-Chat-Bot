# Import dependencies
import re
import time
import string
import random






# Random Unique Token Generator
def random_string(chars:str=string.ascii_uppercase + string.digits):
    result = f'{round(time.time() * 1000)}#'
    result += ''.join(random.choice(chars) for _ in range(16))
    return result

# Email Validator
def valid_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

# Id Unique GENERATOR
def randomChatId(chars: str = string.ascii_uppercase + string.digits):
    result = f"{round(time.time() * 1000)}"
    return result