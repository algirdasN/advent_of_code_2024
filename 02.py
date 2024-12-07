import numpy as np

def check_report(report, tolerance = False):
    sign = np.sign(report[-1] - report[0])
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not 1 <= sign * diff <= 3:
            if tolerance:
                return any(
                    check_report(report[:j] + report[j + 1:]) for j in range(len(report))
                )
            else:
                return False
    else:
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