m, n = map(int, input().split())
books = list(map(int, input().split()))
books.sort(key=abs)

lastbook = books[len(books) - 1]
books.sort()

neg = []
pos = []

for book in books:

    if book < 0:
        neg.append(book)
    else:
        pos.append(book)

pos.sort(reverse=True)

negatives = [neg[i * n:(i + 1) * n] for i in range((len(neg) + n - 1) // n)]
positives = [pos[i * n:(i + 1) * n] for i in range((len(pos) + n - 1) // n)]

steps = 0

for negative in negatives:

    negative.sort(key=abs)
    farBook = negative[len(negative) - 1]
    if lastbook == farBook:
        steps += abs(farBook)
    else:
        steps += abs(farBook) * 2

for positive in positives:
    positive.sort(key=abs)
    farBook = positive[len(positive) - 1]
    if lastbook == farBook:
        steps += abs(farBook)
    else:
        steps += abs(farBook) * 2

print(steps)
