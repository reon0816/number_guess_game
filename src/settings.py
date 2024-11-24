import pygame
import sys

# 画面サイズと色の定義
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

# フォントパス
FONT_PATH = "assets/fonts/NotoSansJP-Regular.ttf"

# pygame の初期化（フォントや画像のロード前に必要）
pygame.init()

# フォント設定
try:
    FONT = pygame.font.Font(FONT_PATH, 24)
    FONT_LARGE = pygame.font.Font(FONT_PATH, 36)
except FileNotFoundError:
    print(f"フォントファイルが見つかりません: {FONT_PATH}")
    sys.exit()

# 難易度ごとの背景色
BACKGROUND_COLORS = {
    "やさしい": YELLOW,
    "ふつう": BLUE,
    "むずかしい": PURPLE,
    "おに": RED,
}

# マップ画像のロード
try:
    GROUND_IMAGE = pygame.image.load("assets/images/ground.png")
    WATER_IMAGE = pygame.image.load("assets/images/water.png")
    GROUND_IMAGE = pygame.transform.scale(GROUND_IMAGE, (32, 32))  # 1セル32x32
    WATER_IMAGE = pygame.transform.scale(WATER_IMAGE, (32, 32))
except FileNotFoundError as e:
    print(f"画像ファイルが見つかりません: {e}")
    sys.exit()

if __name__ == "__main__":
    try:
        print("GROUND_IMAGE:", GROUND_IMAGE)
        print("WATER_IMAGE:", WATER_IMAGE)
    except Exception as e:
        print(f"エラーが発生しました: {e}")