import re

MUL_PATTERN = re.compile("mul\(\d+,\d+\)")
DONT_PATTERN = re.compile("(don't\(\).+?)(?:do\(\)|$)")

def mul(x, y):
    return x * y

def main():
    with open("data/03.txt") as file:
        instruction = "".join(l[:-1] for l in file.readlines())

    matches = MUL_PATTERN.findall(instruction)
    total = sum(eval(m) for m in matches)

    print(total)

    do_instruction = DONT_PATTERN.sub("", instruction)
    matches = MUL_PATTERN.findall(do_instruction)
    do_total = sum(eval(m) for m in matches)

    print(do_total)

if __name__ == "__main__":
    main()