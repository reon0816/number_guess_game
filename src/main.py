import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BACKGROUND_COLORS, FONT_PATH
from ui import draw_text, draw_buttons
from game_logic import start_game, process_guess
from map_data import MAP_DATA
from settings import GROUND_IMAGE, WATER_IMAGE

pygame.init()

# フォントの初期化
try:
    FONT = pygame.font.Font(FONT_PATH, 24)
    FONT_LARGE = pygame.font.Font(FONT_PATH, 36)
except FileNotFoundError:
    print(f"フォントファイルが見つかりません: {FONT_PATH}")
    sys.exit()

# ウィンドウ設定
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("数当てゲーム")

# ボタンデータ
BUTTONS = [
    {"rect": pygame.Rect(100, 150, 120, 50), "text": "やさしい", "level": (1, 50)},
    {"rect": pygame.Rect(420, 150, 120, 50), "text": "ふつう", "level": (1, 100)},
    {"rect": pygame.Rect(420, 280, 120, 50), "text": "むずかしい", "level": (-100, 100)},
    {"rect": pygame.Rect(100, 280, 120, 50), "text": "おに", "level": (-200, 200)},
]

def draw_map(screen):
    """マップを描画する関数"""
    for row_index, row in enumerate(MAP_DATA):
        for col_index, cell in enumerate(row):
            x, y = col_index * 32, row_index * 32  # 1セルのサイズは32x32ピクセル
            if cell == 1:  # 水
                screen.blit(WATER_IMAGE, (x, y))
            elif cell == 0:  # 地面
                screen.blit(GROUND_IMAGE, (x, y))

def main():
    state = {
        "game_state": "menu",
        "secret_number": None,
        "attempts": 0,
        "selected_difficulty": None,
        "feedback_text": "",
        "input_text": "",
    }

    input_box = pygame.Rect(150, 350, 300, 40)
    confirm_button = pygame.Rect(460, 350, 100, 40)
    back_button = pygame.Rect(260, 400, 120, 50)

    running = True
    while running:
        # 背景色の設定
        if state["selected_difficulty"] and state["game_state"] in ("game", "result"):
            screen.fill(BACKGROUND_COLORS[state["selected_difficulty"]])
        else:
            screen.fill(WHITE)
        
        # メニュー画面
        if state["game_state"] == "menu":
            draw_map(screen)  # ここでマップを描画
            draw_buttons(screen, BUTTONS)

        # 結果画面
        elif state["game_state"] == "result":
            draw_text(screen, "正解！ゲーム終了！", 200, 150, FONT_LARGE)
            pygame.draw.rect(screen, WHITE, back_button)
            draw_text(screen, "マップへ戻る", back_button.x + 10, back_button.y + 10)

        # ゲーム画面
        elif state["game_state"] == "game":
            draw_text(screen, f"難易度: {state['selected_difficulty']}", 10, 10)
            draw_text(screen, f"残り試行回数: {state['attempts']}", 10, 50)
            draw_text(screen, state["feedback_text"], 200, 200, FONT_LARGE)

            # 入力欄と確認ボタンの描画
            pygame.draw.rect(screen, WHITE, input_box)
            pygame.draw.rect(screen, WHITE, confirm_button)
            draw_text(screen, state["input_text"], input_box.x + 10, input_box.y + 5)
            draw_text(screen, "確認", confirm_button.x + 20, confirm_button.y + 5)

        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # メニュー画面でボタンが押された場合
                if state["game_state"] == "menu":
                    for button in BUTTONS:
                        if button["rect"].collidepoint(event.pos):
                            start_game(button, state)

                # 結果画面で戻るボタンが押された場合
                elif state["game_state"] == "result":
                    if back_button.collidepoint(event.pos):
                        state["game_state"] = "menu"
                        state["selected_difficulty"] = None

                # ゲーム画面で確認ボタンが押された場合
                elif state["game_state"] == "game":
                    if confirm_button.collidepoint(event.pos):
                        if state["input_text"].isdigit():
                            process_guess(state, int(state["input_text"]))
                            state["input_text"] = ""

            # キーボード入力処理
            elif event.type == pygame.KEYDOWN and state["game_state"] == "game":
                if event.key == pygame.K_BACKSPACE:
                    state["input_text"] = state["input_text"][:-1]
                elif event.unicode.isdigit():
                    state["input_text"] += event.unicode

        # ゲームオーバー処理
        if state["attempts"] == 0 and state["game_state"] == "game":
            state["feedback_text"] = "ゲームオーバー！"
            state["game_state"] = "result"

        # 画面更新
        pygame.display.flip()

if __name__ == "__main__":
    main()