hrs = float(input("Enter Hours:"))

rate = float(input("Enter rate:"))

pay = 40 * rate

print(pay)

if hrs > 40:
    extra_hrs = hrs - 40

    rate_increase = rate * 1.5

    extra_pay = extra_hrs * rate_increase

    print(extra_pay)


