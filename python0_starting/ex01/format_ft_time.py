import time

# I use the time library to get the amount of seconds since January 1, 1970
# The round function refers here to simply the amount of number after the floating point (4 numbers, as the example in the subject)
epoch_seconds = round(time.time(), 4)

# I use here the .format function to add commas for each currency of the number (XXX,XXX,XXX,XXX.XXXXXXXX)
epoch_seconds_formatted = '{:,}'.format(epoch_seconds)

# Here is the format to get the value from scientif way (X.XXe-02 for example)
# The subject show only two numbers after the decimal, we use .2e format to do that
epoch_seconds_scientific = '{:.2e}'.format(epoch_seconds)

# I use .strftime function from time library to get the today date formatted by rules of the function
string_localtime = time.strftime("%b %d %Y", time.localtime())

# Asked output:
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
print("Seconds since January 1, 1970: " + epoch_seconds_formatted + " or " + epoch_seconds_scientific + " in scientific notation")
print(string_localtime)
