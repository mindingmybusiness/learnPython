#get user email address
email = input("Please input your email: ").strip()
#slice out username
user = email[:email.index("@"):1]
#slice out domain name
domain = email[email.index("@")+1:email.index(".com"):1]
#format message
output = "Your user name is {} and your domain name is {}"
output = output.format(user, domain)
#display output message
print(output)