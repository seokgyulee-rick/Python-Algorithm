wait_ppl = 1200202 + 1

month = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]
enterppl_per_hour = 25+15*5
enterppl_per_day = enterppl_per_hour * 12

day_per_year = 0
for i in month:
    day_per_year += i
print("day_per year " + str(day_per_year))

add_year = wait_ppl // (day_per_year * enterppl_per_day)
rest_ppl = wait_ppl % (day_per_year * enterppl_per_day)
print("rest_ppl : " + str(rest_ppl))
add_month = 0
for i in range(len(month)):
    if(rest_ppl - month[i]*enterppl_per_day > 0):
        rest_ppl -= month[i]*enterppl_per_day
    else:
        add_month = i
        break

add_day = rest_ppl//enterppl_per_day
rest_ppl = rest_ppl % enterppl_per_day

add_hour = rest_ppl//enterppl_per_hour
rest_ppl = rest_ppl % enterppl_per_hour

add_min = 0
if(rest_ppl > 25):
    add_min = ((rest_ppl-25) / 15)*10

print("year " + str(add_year) + " month " + str(add_month) +
      " day " + str(add_day) + " hour " + str(add_hour) + " min : " + str(add_min))
