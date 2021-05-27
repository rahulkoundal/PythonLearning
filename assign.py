actual_hrs = float(input("Enter Hours:"))

rate = float(input("Enter rate:"))


def computepay(actual_hrs, rate):
    if actual_hrs > 40:
        extra_hours = actual_hrs - 40
        cal_pay = extra_hours * 1.5 * rate + 40 * rate
        return cal_pay
    else:
        cal_pay = actual_hrs * rate
        return cal_pay


pay = computepay(actual_hrs, rate)

print(pay)


