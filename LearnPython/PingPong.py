import pygame  # khai báo thư viện pygame

# khai báo thư viện system (dùng để sử dụng 1 số lệnh quản lí cửa sổ)
import sys

pygame.init()  # khởi tạo () cho phép kích hoạt và sử dụng các hàm của pygame

FPS = 60  # tốc độ khung hình trên 1s 

# tạo cửa sổ game (700*500) đơn vị tính pixel
WIDTH = 700  # chiều rộng
HEIGHT = 500  # chiều cao

# tạo ra cửa sổ , biến WINDOW để lưu cửa sổ
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("PingPong")  # đặt tên tựa game

WHITE = (255, 255, 255)  # bảng màu rgb trắng
BLACK = (0, 0, 0)  # bảng màu rgb đen

PADDLE_WIDTH = 20  # chiều rộng của bản
PADDLE_HEIGHT = 100  # chiều cao của bản

BALL_RADIUS = 7  # bán kính của banh

SCORE_FONT = pygame.font.SysFont("comicscans", 50)  # font chữ

WINNING_SCORE = 5  # giới hạn mức điểm tối đa để kết thúc game


class Paddle:  # lớp bản
    COLOR = WHITE  # set màu bản
    VEL = 4  # tốc độ ban đầu

    def __init__(self, x, y, width, height):  # khởi tạo
        self.x = self.original_x = x  # khởi tạo toạ độ x
        self.y = self.original_y = y  # khởi tạo toạ độ y
        self.width = width  # chiều rộng
        self.height = height  # chiều cao

    def draw(self, win):  # hàm vẽ hình chữ nhật(surface,color,chiều rộng ,chiều cao)
        pygame.draw.rect(
            win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL  # đi lên
        else:
            self.y += self.VEL  # đi xuống

    def reset(self):  # reset về vị trí ban đầu
        self.x = self.original_x
        self.y = self.original_y


class Ball:  # lớp banh
    MAX_VEL = 5  # set vận tốc tối đa là 5
    COLOR = WHITE  # màu trắng

    def __init__(self, x, y, radius):  # khởi tạo
        self.x = self.original_x = x  # khởi tạo toạ độ x
        self.y = self.original_y = y  # khởi tạo toạ độ y
        self.radius = radius  # khởi tạo bán kính
        self.x_vel = 5  # khởi tạo tốc độ tối đa đi ngang
        self.y_vel = 0  # khởi tạo tốc độ tối đa đi dọc

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y),
                           self.radius)  # vẽ trái banh

    def move(self):  # di chuyển
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):  # reset toạ độ banh
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1  # reset toạ độ trái banh khi ván mới bắt đầu bay về phía bên người thua


def draw(win, paddles, ball, left_score, right_score):
    win.fill(BLACK)  # fill window with black

    left_score_text = SCORE_FONT.render(
        f"{left_score}", 1, WHITE)  # bảng điểm bên trái
    right_score_text = SCORE_FONT.render(
        f"{right_score}", 1, WHITE)  # bảng điểm bên phải
    win.blit(left_score_text,
             (WIDTH//4 - left_score_text.get_width()//2, 20))  # vị trí bảng điểm trái (gồm 2 thuộc tính : blit(image, (left, top)))
    win.blit(right_score_text,
             (WIDTH*(3/4) - right_score_text.get_width()//2, 20))  # vị trí bảng điểm phải

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10,
                         HEIGHT//20))  # vẽ đường kẻ ở giữa

    ball.draw(win)
    pygame.display.update()  # cập nhật lại


def handle_collision(ball, left_paddle, right_paddle):  # xử lý các va chạm
    if ball.y + ball.radius >= HEIGHT:
        # nếu trái banh chạm đáy thì tốc độ ban đầu đổi dấu (đổi hướng đi lên)
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        # nếu trái banh chạm trần nhà thì tốc độ ban đầu đổi dấu (đổi hướng đi xuống)
        ball.y_vel *= -1

    if ball.x_vel < 0:  # trường hợp banh đang di chuyển sang trái
        # check xem quả banh nằm trong vùng tọa độ y của paddle
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:  # Khi quả banh chạm vào paddle
                ball.x_vel *= -1  # Đổi chiều tọa độ x quả banh

                middle_y = left_paddle.y + left_paddle.height / \
                    2  # Tính vị trí tọa độ y ở giữa của paddle
                # Tính khoảng cách từ vị trí giữa paddle đến vị trí quả banh theo tọa độ y
                difference_in_y = middle_y - ball.y
                # Hệ số từ quãng đường tối đa và tốc độ tối đa
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                # Tính tốc độ phản lại (Quả bóng càng chạm vào vị trị gần biên thì tốc độ phản lại càng lớn)
                y_vel = difference_in_y / reduction_factor
                # Tính tốc độ và hướng phản lại của trái bóng (Chạm nửa dưới của paddle sẽ phản lại xuống dưới và ngược lại)
                ball.y_vel = -1 * y_vel
    # trường hợp banh đang di chuyển sang phải (các câu lệnh ở dưới cũng tương tự nhưng là khi bóng chạm paddle bên phải)
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor

                ball.y_vel = -1 * y_vel


# Xử lý di chuyển cho paddle
def handle_paddle_movement(keys, left_paddle, right_paddle):
    # Xử lý di chuyển lên xuống paddle bên trái
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:  # Lên khi nhấn W
        left_paddle.move(up=True)

    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:  # Xuống khi nhấn S
        left_paddle.move(up=False)

    # Xử lý di chuyển lên xuống paddle bên phải
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:  # Lên khi nhấn UP
        right_paddle.move(up=True)

    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:  # Xuống khi nhấn DOWN
        right_paddle.move(up=False)


def main():
    run = True  # gán biến run = True
    # tính toán khung hình hay phản hồi của người chơi quy về mặt thời gian
    clock = pygame.time.Clock()

    # toạ độ bản trái
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT //
                         2, PADDLE_WIDTH, PADDLE_HEIGHT)

    # toạ độ bản phải
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT //
                          2-PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    # toạ độ trái banh
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)

    left_score = 0  # khởi tạo điểm bên trái
    right_score = 0  # khởi tạo điểm bên phải

    while run:  # main loop (nơi mọi thứ xảy ra hoạt động)
        clock.tick(FPS)  # cập nhật số khung hình trên 1s

        # vẽ
        draw(WINDOW, [left_paddle, right_paddle],
             ball, left_score, right_score)

        for event in pygame.event.get():  # lặp lại khung hình trong qtrinh lặp lại lắng nghe sự kiện xem có sự kiện nào xảy ra ko , nếu có vòng lặp for sẽ bắt sự kiện
            # trong các sự kiện bắt được xem có sự kiện nào = QUIT hay ko ? (nếu người dùng nhấp dấu chéo đỏ)
            if event.type == pygame.QUIT:
                run = False
                break  # thoát khỏi vòng lặp

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()

        handle_collision(ball, left_paddle, right_paddle)

        if ball.x < 0:  # nếu banh chạm vào bản bên trái
            right_score += 1  # điểm bên phải + 1
            ball.reset()  # reset banh về vị trí ban đầu
        elif ball.x > WIDTH:  # nếu banh chạm vào bản bên trái
            left_score += 1  # điểm bên trái + 1
            ball.reset()  # reset toạ độ banh về vị trí ban đầu

        won = False  # khởi tạo biến won =  False

        if left_score >= WINNING_SCORE:  # nếu điểm bên trái lớn hơn điểm giới hạn
            won = True
            win_text = "Left Player Won"  # display anounce
        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Right Player Won"  # display anounce

        if won:  # won = True

            # xuất hiện bản text
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WINDOW.blit(text, (WIDTH//2-text.get_width() //
                               2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()  # cập nhật
            pygame.time.delay(5000)
            ball.reset()  # reset banh về toạ độ ban đầu
            left_paddle.reset()  # reset bản trái về toạ độ ban đầu
            right_paddle.reset()  # reset bản phải về vị trí ban đầu
            left_score = 0  # khởi tạo lại điểm bên trái = 0
            right_score = 0  # khởi tạo lại điểm bên phải = 0

    pygame.quit()  # thoát thư viện pygame


if __name__ == "__main__":
    main()

    # toạ độ x đi ngang qua phải , toạ độ y đi dọc xuống
    # có nhiều thư viện để viết ra game ví dụ như turtle , twintle ko nhất thiết phải là pygame
    # vì sao phải sử dụng thư viện : để xử lí về mặt giao diện và các chuyển động trực quan của game
    # trái banh di chuyển : di dời toạ độ của trái banh đi đến toạ độ khác và cập nhật màn hình lại theo các khung hình
    # để làm được điều trên chúng ta cần vòng lặp để cập nhật cửa sổ liên tục
