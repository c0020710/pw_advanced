CORRECT_PASSWORD = 'a123456'
MAX_ATTEMPTS = 3

for attempt in range(1, MAX_ATTEMPTS + 1):
   password_attempt = input(f"Password (attempt {attempt} of {MAX_ATTEMPTS}): ")

   if password_attempt == CORRECT_PASSWORD:
       print("Logged in successfully")
       break  # Exit the loop if login is successful

   remaining_attempts = MAX_ATTEMPTS - attempt
   if remaining_attempts > 0:
       print(f"Incorrect password. {remaining_attempts} attempt(s) remaining")
   else:
       print("ACCOUNT LOCKED")