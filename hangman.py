import random

def hangman():
    ans = ["cat","book","soccer","baseball"]
    wrong = 0
    random_number = random.randint(0,3)
    word = ans[random_number]
    win = False
    stages = ["",
    "----    ",
    "|       ",
    "|   |   ",
    "|   o   ",
    "|  /|/  ",
    "|  / /  ",
    "|       ",
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    print("ハングマンへようこそ！")

    while wrong < len(stages) -1:
        print("\n")
        msg = "一文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))
hangman()