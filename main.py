import pygame, sys
from Project4_Group94.sudoku_generator import generate_sudoku
# from sudoku_generator import *
from constants import *

# Initialize Pygame, game title, background color, and fonts
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')
screen.fill(BG)
pygame.display.update()
sketch_font = pygame.font.Font(None, SKETCH_FONT)
num_font = pygame.font.Font(None, NUM_FONT)
game_over_font = pygame.font.Font(None, OVER_FONT)
button_font = pygame.font.Font(None, BUTTON_FONT)
welcome_font = pygame.font.Font(None, WELCOME_FONT)
diff = 1


# Define "start_menu" function that displays a welcome message and difficulty options when player starts up the game
# When the player selects a difficulty, display the appropriate sudoku board
def start_menu():

    # Displays Welcome Message
    welcome_surf = welcome_font.render("Welcome to Sudoku", 0, BLACK)
    welcome_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 5))
    screen.blit(welcome_surf, welcome_rect)

    # Displays "Game Mode" Message
    game_mode_surf = num_font.render("Select Game Mode:", 0, BLACK)
    game_mode_rect = game_mode_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2.5))
    screen.blit(game_mode_surf, game_mode_rect)

    # Displays "Easy" Button
    easy_text = button_font.render("EASY", 0, WHITE)
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(ORANGE)
    easy_surface.blit(easy_text, (10, 10))
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 4, 490))
    screen.blit(easy_surface, easy_rectangle)

    # Displays "Medium" Button
    med_text = button_font.render("MEDIUM", 0, WHITE)
    med_surface = pygame.Surface((med_text.get_size()[0] + 20, med_text.get_size()[1] + 20))
    med_surface.fill(ORANGE)
    med_surface.blit(med_text, (10, 10))
    med_rectangle = med_surface.get_rect(center=(WIDTH // 2, 490))
    screen.blit(med_surface, med_rectangle)

    # Displays "Hard" Button
    hard_text = button_font.render("HARD", 0, WHITE)
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(ORANGE)
    hard_surface.blit(hard_text, (10, 10))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH - 175, 490))
    screen.blit(hard_surface, hard_rectangle)

    for event in pygame.event.get():
        pygame.display.update()

        # Exit game if user clicks the "X" button in the top right corner
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Display the appropriate board based on which difficulty level was selected
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            diff = 1
            if 463 < y < 517:
                if 148 < x < 188:
                    diff = 30
                elif 317 < x < 357:
                    diff = 40
                elif 480 < x < 520:
                    diff = 50
            if diff != 1:
                board_call = generate_sudoku(9, diff)
                board = board_call[0]
                screen.fill(BG)
                draw_big_grid()
                draw_small_grid()
                draw_og_board(board)
                buttons()
                pygame.display.update()
                if board_call is not None:
                    return board_call


# Define "draw_big_grid" function that draws thicker lines to create an outer grid and divide the board into 3x3 boxes
def draw_big_grid():

    # Draws vertical lines
    for i in range(3):
        pygame.draw.line(screen, BLACK, (BIG_SQUARE * i, START), (BIG_SQUARE * i, END),
                         BIG_LINE_WIDTH)

    # Draws horizontal lines
    for i in range(4):
        pygame.draw.line(screen, BLACK, (START, BIG_SQUARE * i), (END, BIG_SQUARE * i),
                         BIG_LINE_WIDTH)


# Define "draw_small_grid" function that draws thinner lines to create 9 cells within each 3x3 box
def draw_small_grid():

    # Draws vertical lines
    for i in range(10):
        pygame.draw.line(screen, BLACK, (SMALL_SQUARE * i, START), (SMALL_SQUARE * i, END),
                         SMALL_LINE_WIDTH)

    # Draws horizontal lines
    for i in range(9):
        pygame.draw.line(screen, BLACK, (START, SMALL_SQUARE * i), (END, SMALL_SQUARE * i),
                         SMALL_LINE_WIDTH)


# Define "highlight_cell" function that highlights the outline of a cell if the user clicks on it or navigates to it
def highlight_cell(row, col, color):
    pygame.draw.line(screen, color, (SMALL_SQUARE * col, SMALL_SQUARE * row),
                     (SMALL_SQUARE * col, SMALL_SQUARE * row + SMALL_SQUARE),
                     SMALL_LINE_WIDTH)
    pygame.draw.line(screen, color, (SMALL_SQUARE * col, SMALL_SQUARE * row),
                     (SMALL_SQUARE * col + SMALL_SQUARE, SMALL_SQUARE * row),
                     SMALL_LINE_WIDTH)
    pygame.draw.line(screen, color, (SMALL_SQUARE * col + SMALL_SQUARE, SMALL_SQUARE * row),
                     (SMALL_SQUARE * col + SMALL_SQUARE, SMALL_SQUARE * row + SMALL_SQUARE),
                     SMALL_LINE_WIDTH)
    pygame.draw.line(screen, color, (SMALL_SQUARE * col, SMALL_SQUARE * row + SMALL_SQUARE),
                     (SMALL_SQUARE * col + SMALL_SQUARE, SMALL_SQUARE * row + SMALL_SQUARE),
                     SMALL_LINE_WIDTH)


# Define "buttons" function that draws the "Reset", "Restart", and "Exit" buttons below the sudoku board
def buttons():

    # Draws "Reset" button
    reset_text = button_font.render("RESET", 0, WHITE)
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(ORANGE)
    reset_surface.blit(reset_text, (10, 10))
    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH // 4, 715))
    screen.blit(reset_surface, reset_rectangle)

    # Draws "Restart" button
    restart_text = button_font.render("RESTART", 0, WHITE)
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(ORANGE)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, 715))
    screen.blit(restart_surface, restart_rectangle)

    # Draws "Exit" button
    exit_text = button_font.render("EXIT", 0, WHITE)
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(ORANGE)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(
        center=(3 * WIDTH // 4 - 10, 715))
    screen.blit(exit_surface, exit_rectangle)


# Define "draw_game_over" function that shows "Game Won" message or "Game Over" message depending on if player wins
# If the player wins, give them the option to exit; if the player loses, give them to option to restart
def draw_game_over(win):
    image = pygame.image.load('sudoku_image.png').convert()
    screen.blit(image, (0, 0))
    if win == 1:
        end_text = "Game Won!"
    else:
        end_text = "Game Over :("

    # Display either "Game Won" or "Game Over" message
    end_surf = game_over_font.render(end_text, 0, BLACK)
    end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(end_surf, end_rect)

    # If the player wins the game, display an "Exit" button and quit the program if the user clicks it
    if end_text == "Game Won!":
        exit_text = button_font.render("EXIT", 0, WHITE)
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(ORANGE)
        exit_surface.blit(exit_text, (10, 10))
        exit_rectangle = exit_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(exit_surface, exit_rectangle)
        while True:
            for event in pygame.event.get():
                pygame.display.update()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 304 <= x <= 370 and 345 <= y <= 405:
                        pygame.quit()
                        sys.exit()

    # If the player loses the game, display a "Restart" button and go back to the start menu if the user clicks it
    else:
        exit_text = button_font.render("RESTART", 0, WHITE)
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(ORANGE)
        exit_surface.blit(exit_text, (10, 10))
        exit_rectangle = exit_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(exit_surface, exit_rectangle)
        while True:
            for event in pygame.event.get():
                pygame.display.update()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 274 <= x <= 400 and 345 <= y <= 405:
                        image = pygame.image.load('sudoku_image.png').convert()
                        screen.blit(image, (0, 0))
                        board_call = start_menu()
                        while board_call is None:
                            board_call = start_menu()
                        pygame.display.update()
                        return board_call


# Define "draw_og_board" function that displays initial board to the grid, 0s (the removed cells) result in blank cells
def draw_og_board(b):
    offset = 20
    for i in range(len(b)):
        for j in range(len(b[i])):
            num = b[i][j]
            if num != 0:
                num_text = num_font.render(str(num), 0, BLACK)
                screen.blit(num_text, ((j * SMALL_SQUARE) + offset + 5, (i * SMALL_SQUARE) + offset - 5))


# Define "draw_changed_board" function that displays the updated board when a user sketches a number into a cell
def draw_changed_board(b, sketch):
    for i in range(len(b)):
        for j in range(len(b[i])):
            num = sketch[i][j]
            if num != b[i][j] and num != 0:
                num_text = sketch_font.render(str(num), 0, GRAY)
                screen.blit(num_text, ((j * SMALL_SQUARE) + 5, (i * SMALL_SQUARE) + 5))


# Define main function that incorporates all files/functions to run the entire program
if __name__ == "__main__":

    # Display start menu
    image = pygame.image.load('sudoku_image.png').convert()
    screen.blit(image, (0, 0))
    board_call = start_menu()

    # If no 2D board has been created yet, create one and store its pre-solved version and its solution
    while board_call is None:
        board_call = start_menu()
    pygame.display.update()
    solved = board_call[1]
    board = board_call[0]
    og_board = []
    for i in range(len(board)):
        og = []
        for j in range(len(board[i])):
            og.append(board[i][j])
        og_board.append(og)
    guess = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    r, c, win = 0, 0, 0

    # Once a board has been created and the user has chosen a difficulty, start the game by showing the initial board
    while True and board is not None:
        game_over = False
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # For any events that include the mouse button being pressed within the Pygame window
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                if (y // SMALL_SQUARE) != r or (x // SMALL_SQUARE) != c:
                    draw_big_grid()
                    draw_small_grid()
                r = y // SMALL_SQUARE
                c = x // SMALL_SQUARE
                
                # Highlight a cell if a user clicks on it
                if y <= 675:
                    highlight_cell(r, c, RED)
                    
                else:
                    if 739 >= y >= 691:
                        # Reset the board back to its original state if the player presses the "Reset" button
                        if 112 <= x <= 224:
                            screen.fill(BG)
                            screen.fill(BG)
                            draw_big_grid()
                            draw_small_grid()
                            board = og_board
                            draw_og_board(board)
                            buttons()

                        # Go back to the start screen if the player presses the "Restart" button
                        elif 263 <= x <= 411:
                            image = pygame.image.load('sudoku_image.png').convert()
                            screen.blit(image, (0, 0))
                            board_call = start_menu()
                            while board_call is None:
                                board_call = start_menu()
                            pygame.display.update()
                            solved = board_call[1]
                            board = board_call[0]
                            og_board = []
                            for i in range(len(board)):
                                og = []
                                for j in range(len(board[i])):
                                    og.append(board[i][j])
                                og_board.append(og)
                            guess = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
                            r, c, win = 0, 0, 0

                        # Exit the game if the player presses the "Exit" button
                        elif 460 <= x <= 548:
                            pygame.quit()
                            sys.exit()

            # If the user presses a directional key, move the highlighted cell outline according to the key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not game_over:  # If left key is pressed
                    draw_big_grid()
                    draw_small_grid()
                    if c != 0:
                        c -= 1
                        highlight_cell(r, c, RED)
                elif event.key == pygame.K_RIGHT and not game_over:  # If right key is pressed
                    draw_big_grid()
                    draw_small_grid()
                    if c != 8:
                        c += 1
                        highlight_cell(r, c, RED)
                elif event.key == pygame.K_UP and not game_over:  # If up key is pressed
                    draw_big_grid()
                    draw_small_grid()
                    if r != 0:
                        r -= 1
                        highlight_cell(r, c, RED)
                elif event.key == pygame.K_DOWN and not game_over:  # If down key is pressed
                    draw_big_grid()
                    draw_small_grid()
                    if r != 8:
                        r += 1
                        highlight_cell(r, c, RED)

                # If user presses the "Enter" key, turn their sketched gray number into a full-sized black number
                # After this action has occurred, the user may not change the cell's number unless they reset the board
                elif event.key == pygame.K_RETURN:
                    if guess[r][c] != 0:
                        board[r][c] = guess[r][c]
                        guess[r][c] = 0
                    screen.fill(BG)
                    draw_big_grid()
                    draw_small_grid()
                    draw_og_board(board)
                    buttons()
                    pygame.display.update()
                    draw_changed_board(board, guess)

                # If user presses a number key, sketch the corresponding number into the highlighted cell (gray color)
                elif event.key == pygame.K_1:  # If key "1" is pressed
                    if board[r][c] == 0:
                        num_text = sketch_font.render('1', 0, GRAY)
                        screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                        guess[r][c] = 1
                elif event.key == pygame.K_2:  # If key "2" is pressed
                    if board[r][c] == 0:
                        num_text = sketch_font.render('2', 0, GRAY)
                        screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                        guess[r][c] = 2
                elif event.key == pygame.K_3:  # If key "3" is pressed
                    if board[r][c] == 0:
                        num_text = sketch_font.render('3', 0, GRAY)
                        screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                        guess[r][c] = 3
                elif event.key == pygame.K_4:  # If key "4" is pressed
                    if board[r][c] == 0:
                        num_text = sketch_font.render('4', 0, GRAY)
                        screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                        guess[r][c] = 4
                elif event.key == pygame.K_5:  # If key "5" is pressed
                    if board[r][c] == 0:
                        num_text = sketch_font.render('5', 0, GRAY)
                        screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                        guess[r][c] = 5
                elif event.key == pygame.K_6:  # If key "6" is pressed
                    if board[r][c] == 0:
                        num_text = sketch_font.render('6', 0, GRAY)
                        screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                        guess[r][c] = 6
                elif event.key == pygame.K_7:  # If key "7" is pressed
                    if board[r][c] == 0:
                        num_text = sketch_font.render('7', 0, GRAY)
                        screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                        guess[r][c] = 7
                elif event.key == pygame.K_8:  # If key "8" is pressed
                    if board[r][c] == 0:
                        num_text = sketch_font.render('8', 0, GRAY)
                        screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                        guess[r][c] = 8
                elif event.key == pygame.K_9:  # If key "9" is pressed
                    if board[r][c] == 0:
                        num_text = sketch_font.render('9', 0, GRAY)
                        screen.blit(num_text, ((c * SMALL_SQUARE) + 5, (r * SMALL_SQUARE) + 5))
                        guess[r][c] = 9

            # If all cells in board are filled and the user's board matches the solution, go to the "Game Won" screen
            # If the board is filled and the user's board doesn't match the solution, go to the "Game Over" screen
            zero_check = False
            for b in board:
                for num in b:
                    if num == 0:
                        zero_check = True
            if not zero_check:
                game_over = True
                if board != solved:
                    win = 123
                else:
                    win = 1
            if game_over:
                pygame.display.update()
                pygame.time.delay(100)
                board_call = draw_game_over(win)
                solved = board_call[1]
                board = board_call[0]
                og_board = []
                for i in range(len(board)):
                    og = []
                    for j in range(len(board[i])):
                        og.append(board[i][j])
                    og_board.append(og)
                guess = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
                r, c, win = 0, 0, 0
        pygame.display.update()

