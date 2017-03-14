# Day 4

from day0 import *





def check_name(str, check):
    """return string of five most common letters in str"""
    if len(str) < 5:
        return False
    # break ties alphabetically, need to get frequency of all letters to do so
    freq = sorted(collections.Counter(str).most_common(), key=lambda x: (-x[1], x[0]))
    # take five most common
    freq = freq[0:5]
    #print(freq)
    result = ''
    for pair in freq:
        result += pair[0]
    return result == check


def decrypt(s, num):
    """part 2: caesar decrypt: move letters of s forward by num"""
    l = [ord(i) for i in s]
    #print("List: ")
    #print(l)
    result =''
    for i in l:
        if chr(i) == '-':
            result += ' '
        else:
            result += chr((i + num - ord('a')) % 26 + ord('a'))
    return result

def run():
    data = parse(4)
    answer = 0

    for line in data:
        # get checksum group
        groups = re.findall(r'(.*)-(\d+)\[(.*)\]', line)
        #print(groups)
        name = groups[0][0]

        sector_id = int(groups[0][1])
        check = groups[0][2]

        name1 = name.replace('-', '')
        if check_name(name1, check):
            #print("Real room. Adding sector id " + str(sector_id))
            answer += sector_id

        print(decrypt(name, sector_id) + " " + str(sector_id))

    return answer


if __name__ == "__main__":
    answer = run()
    print("Answer: " + str(answer))