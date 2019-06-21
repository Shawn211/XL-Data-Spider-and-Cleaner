# coding = utf-8
import re


def main():
    file = 'ÇåÏ´Êý¾Ý.txt'
    with open(file, 'r') as f:
        t = f.read()
        temps = re.findall(r'\[(.*)\]', t)

    results = 'results.txt'
    with open(results, 'w') as f:
        for temp in temps:
            f.write('\n' + temp)


if __name__ == '__main__':
    main()
