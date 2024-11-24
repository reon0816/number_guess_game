import random

def start_game(button, state):
    """ゲームを開始"""
    state["selected_difficulty"] = button["text"]
    state["secret_number"] = random.randint(*button["level"])
    state["attempts"] = 10
    state["feedback_text"] = ""
    state["input_text"] = ""
    state["game_state"] = "game"

def process_guess(state, guess):
    """プレイヤーの入力を処理"""
    if guess < state["secret_number"]:
        state["feedback_text"] = "もっと大きい数字だよ！"
    elif guess > state["secret_number"]:
        state["feedback_text"] = "もっと小さい数字だよ！"
    else:
        state["feedback_text"] = "正解！ゲーム終了！"
        state["game_state"] = "result"
    state["attempts"] -= 1