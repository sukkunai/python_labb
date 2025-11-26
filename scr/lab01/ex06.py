def count_participants():
    n = int(input(""))

    offline = 0
    online = 0

    for _ in range(n):
        data = input().split()

        participation_format = data[-1] == "True"

        if participation_format:
            offline += 1
        else:
            online += 1

    print(f" {offline}", f" {online}", sep=" ")


count_participants()
