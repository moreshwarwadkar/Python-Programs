# SIMPLIFIED FORM OF SLICING

s = 'I Am Billionaire'

print(s[0:3+1:1]) # OP : I Am

print(s[:3+1]) # OP : I Am


print(s[-1:-11-1:-1]) # OP : erianoilliB

print(s[:-11-1:-1]) # OP : erianoilliB


# We can ignore Ending Index when Ending Index is Last value or (minus) - length (variable).

print(s[2::1]) # Am Billionaire
print(s[-13::-1]) # mA I


# We can ignore Updation value, When Updation Value is 1.

print(s[2:4+1:1])
print(s[2:4+1:]) # OP : Am
