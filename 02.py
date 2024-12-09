def check_report(report, tolerance = False):
    sign = 1 if report[-1] > report[0] else -1
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not 1 <= sign * diff <= 3:
            if tolerance:
                return check_report(report[:i] + report[i + 1:]) or check_report(report[:i + 1] + report[i + 2:])
            else:
                return False
    return True

def main():
    with open("data/02.txt") as file:
        data = [[int(val) for val in line.split()] for line in file.readlines()]

    count = sum(check_report(report) for report in data)

    print(count)

    count_tolerance = sum(check_report(report, True) for report in data)

    print(count_tolerance)


if __name__ == "__main__":
    main()