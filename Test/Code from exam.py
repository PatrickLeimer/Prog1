class WordMaster:

    def __init__(self, answer, maxAttempts):
        self.answer = answer
        self.maxAtt = maxAttempts
        self.gameCount = 0

    def guess(self, usrguess):
        if self.maxAtt == self.gameCount:
            print("You have exceeded the maximum number of attempts. Game over!")
            return []
        if usrguess == self.answer:
            print("Congratulations! You guessed the word correctly.")
            return []
        else:
            self.gameCount += 1
            list = []
            j = 0
            for char in usrguess:
                if char == self.answer[j]:
                    list.append("Green")
                elif char in self.answer:
                    list.append("Yellow")
                else:
                    list.append("Gray")
                j += 1
            return list

game = WordMaster('apple', 5)
print(game.guess('grape'))

listI = [1, 2, 3, 4, 2, 3, 5, 6, 7, 1]
def longest_increasing_sequence(sequence):
    seq = sequence
    count, high_count = 1, 0

    for i in range(len(seq)):
        if (i + 1) == len(seq):
            break  # break the loop
        elif seq[i] < seq[i + 1]:
            count += 1
        else:
            if count > high_count:
                high_count = count
                count = 1
            else:
                count = 1
    return high_count

print(longest_increasing_sequence(listI))