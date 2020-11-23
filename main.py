import pandas as pd
import random

START_IDX = 892


def generate_random_solution():
    submission_array = []
    for i in range(892, 1310):
        random_guess = random.randint(0, 1)
        submission_array.append([i, random_guess])
        submission_df = pd.DataFrame(submission_array, columns=[
                                     'PassengerId', 'Survived'])
    print(submission_df)
    submission_df.to_csv("./submissions/random-submission.csv", index=False)


def all_women_and_children_die(test):
    submission_array = []
    for index, row in test.iterrows():
        is_alive = 0
        if row['Sex'] == 'female' or row["Age"] <= 18:
            is_alive = 1
        submission_array.append([index + START_IDX, is_alive])
        submission_df = pd.DataFrame(submission_array, columns=[
            'PassengerId', 'Survived'])

    print(submission_df)
    submission_df.to_csv("./submissions/kill-women-child.csv", index=False)
    print(test['Sex'], test['Age'])


if __name__ == "__main__":
    test = pd.read_csv("./data/test.csv")
    train = pd.read_csv("./data/train.csv")

    # print(train)
    # print(test)
    all_women_and_children_die(test)
    # generate_random_solution()
