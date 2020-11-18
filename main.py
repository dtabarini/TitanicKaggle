import pandas as pd
import random


def generate_random_solution():
    submission_array = []
    for i in range(892, 1310):
        random_guess = random.randint(0, 1)
        submission_array.append([i, random_guess])
        submission_df = pd.DataFrame(submission_array, columns=[
                                     'PassengerId', 'Survived'])
    print(submission_df)
    submission_df.to_csv("./submissions/random-submission.csv", index=False)
    return


if __name__ == "__main__":
    test = pd.read_csv("./data/test.csv")
    train = pd.read_csv("./data/train.csv")
    print(train)
    print(test)
    generate_random_solution()
