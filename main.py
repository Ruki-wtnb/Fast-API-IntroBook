
import bcrypt

# at creation first:
password = u"seCr3t"
hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

# first attempt:
password = u"seCrEt"
false_test = bcrypt.checkpw(password.encode('utf8'), hashed_password)
# -> False
print(false_test)

# second attempt:
password = u"seCr3t"
true_test = bcrypt.checkpw(password.encode('utf8'), hashed_password)
# -> True
print(true_test)