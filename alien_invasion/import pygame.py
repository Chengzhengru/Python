import pygame
from button import Button

def test_button():
    """Test if the Button class works correctly."""
    pygame.init()
    # 创建一个屏幕
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Test Button")

    # 创建一个按钮实例
    test_button = Button(type('MockGame', (object,), {"screen": screen})(), "Play")

    running = True
    while running:
        # 填充背景
        screen.fill((230, 230, 230))  # 灰色背景
        # 绘制按钮
        test_button.draw_button()
        # 刷新屏幕
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

test_button()
