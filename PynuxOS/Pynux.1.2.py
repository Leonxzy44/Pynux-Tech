import time
import random
import winsound
import tkinter as tk
from tkinter import messagebox
import json
import os
import sys



print("\033[33m" + r"""
⠀   ⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠛⠛⠛⠛⠷⣶⣤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠈⢳⡀⢀⣠⣴⡿⠿⠛⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠀⢀⣠⣤⣄⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⣾⠋⠈⠹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⢻⡆⠀⠀⢹⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⠈⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⣇⠀⠀⠀⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⣿⠀⠀⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⠀⠀⠈⣿⠀⢀⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠻⢶⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⡾⠃⠀⠀⠀⠈⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣶⣯⣤⣤⣤⣤⡴⠶⠶⣼⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀
 _______                                          
/       \                                         
$$$$$$$  | __    __  _______   __    __  __    __ 
$$ |__$$ |/  |  /  |/       \ /  |  /  |/  \  /  |
$$    $$/ $$ |  $$ |$$$$$$$  |$$ |  $$ |$$  \/$$/ 
$$$$$$$/  $$ |  $$ |$$ |  $$ |$$ |  $$ | $$  $$<  
$$ |      $$ \__$$ |$$ |  $$ |$$ \__$$ | /$$$$  \ 
$$ |      $$    $$ |$$ |  $$ |$$    $$/ /$$/ $$  |
$$/        $$$$$$$ |$$/   $$/  $$$$$$/  $$/   $$/ 
          /  \__$$ |                              
          $$    $$/                               
           $$$$$$/                                
                                                                                   

""" + "\033[0m")

time.sleep(1)
for _ in range(3):
    winsound.Beep(1000, 500)
time.sleep(0.01)





start = input("Welcome to Pynux OS! Make sure you have opened this in fullscreen! Here you browse projects or try different scripts! Press ALT + F4 to leave or Enter to contine...   ")





print("="*150)

print("Booting Pynux...")

time.sleep(3)


Username = input("Enter your username: ")

print("Hi, " + str(Username) + "!")



time.sleep(0.5)
print("Instructions: In the blank space you need to write the command for the thing you want to open.") 

time.sleep(1)

print("-"*100)

print("| Hacking snake game [Cmnd: /snk] | ")

print("-"*100)

print("| Pynux Draw  [Cmnd: /pyd] | ")

print("-"*100)

print("| Retify  [Cmnd: /ref] | ")

print("-"*100)

source = input("Enter your source command here:  ")
print("="*150)



if source == "/pyd":
   import tkinter as tk
from tkinter import colorchooser

class PynuxDraw:
    def __init__(self, root):
        self.root = root
        self.root.title("Pynux Draw")
        self.root.geometry("900x650")
        self.root.configure(bg="#1e1e1e")

        self.brush_color = "white"
        self.brush_size = 5
        self.drawing = False

        
        self.toolbar = tk.Frame(self.root, bg="#2d2d2d", height=50)
        self.toolbar.pack(fill=tk.X, side=tk.TOP)

        
        colors = ["white", "black", "red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink"]
        for c in colors:
            tk.Button(self.toolbar, bg=c, width=2, height=1, command=lambda col=c: self.set_brush_color(col)).pack(side=tk.LEFT, padx=3, pady=5)

        
        tk.Button(self.toolbar, text="Custom Color", bg="#444", fg="white", command=self.choose_color).pack(side=tk.LEFT, padx=10)

        
        tk.Button(self.toolbar, text="Eraser", bg="#555", fg="white", command=self.set_eraser).pack(side=tk.LEFT, padx=10)

        
        tk.Button(self.toolbar, text="Clear", bg="#880000", fg="white", command=self.clear_canvas).pack(side=tk.LEFT, padx=10)

        
        tk.Button(self.toolbar, text="Toggle Paper", bg="#006688", fg="white", command=self.toggle_paper).pack(side=tk.LEFT, padx=10)

        
        tk.Button(self.toolbar, text="Marker", bg="#333", fg="white", command=lambda: self.set_brush_type("marker")).pack(side=tk.LEFT, padx=5)
        tk.Button(self.toolbar, text="Highlighter", bg="#333", fg="white", command=lambda: self.set_brush_type("highlighter")).pack(side=tk.LEFT, padx=5)
        tk.Button(self.toolbar, text="Pencil", bg="#333", fg="white", command=lambda: self.set_brush_type("pencil")).pack(side=tk.LEFT, padx=5)

        
        self.canvas_bg = "white"
        self.canvas = tk.Canvas(self.root, bg=self.canvas_bg, cursor="tcross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

       
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def set_brush_color(self, color):
        self.brush_color = color

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color

    def start_draw(self, event):
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.drawing:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    fill=self.brush_color, width=self.brush_size,
                                    capstyle=tk.ROUND, smooth=True)
            self.last_x, self.last_y = event.x, event.y

    def set_brush_type(self, btype):
        self.brush_type = btype

    def set_eraser(self):
        
        self.brush_color = "#111"

    def clear_canvas(self):
        self.canvas.delete("all")

    def toggle_paper(self):
        self.canvas_bg = "black" if self.canvas_bg == "white" else "white"
        self.canvas.configure(bg=self.canvas_bg)
        if self.brush_color == self.canvas_bg:
            self.brush_color = "white" if self.canvas_bg == "black" else "black"

    def stop_draw(self, event):
        self.drawing = False


if __name__ == "__main__":
    root = tk.Tk()
    app = PynuxDraw(root)
    root.mainloop()


    
elif source == "/ref":
    print(Username, "welcome to Retify! This is an app for memory storing and taking notes.")
    time.sleep(0.5)
    first_note = input("Enter your first reminder here: ")

    try:
        timeenter = int(input("In how many minutes do you want to be reminded? (5, 10, 15, 20, 30, 60): "))
    except ValueError:
        print("You must enter a number.")
        exit()

    if timeenter in [5, 10, 15, 20, 30, 60]:
        print(f"Reminder will appear in {timeenter} minutes...")
        time.sleep(timeenter * 60)
        for _ in range(5):
            print(str(first_note))
        for _ in range(2):
            winsound.Beep(1000, 500)
            time.sleep(0.1)
    else:
        print("Invalid time entered.")



elif source == "/snk":
   import tkinter as tk
from tkinter import messagebox
import json
import random
import os
import time



try:
    import winsound
    SOUND_ENABLED = True
except ImportError:
    SOUND_ENABLED = False

DATA_FILE = "users.json"
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        users = json.load(f)
else:
    users = {}

current_user = None

COLOR_OPTIONS = {
    "green": {"price": 0, "head": "lime", "body": "green"},
    "red": {"price": 5, "head": "red", "body": "darkred"},
    "cyan": {"price": 8, "head": "cyan", "body": "darkcyan"},
    "purple": {"price": 10, "head": "magenta", "body": "purple"},
    "yellow": {"price": 12, "head": "yellow", "body": "goldenrod"},
    "blue": {"price": 15, "head": "blue", "body": "navy"},
    "pink": {"price": 18, "head": "pink", "body": "deeppink"},
    "orange": {"price": 20, "head": "orange", "body": "darkorange"},
    "white": {"price": 25, "head": "white", "body": "lightgray"},
}


CAP_OPTIONS = {
    "none": {"price": 0, "icon": ""},
    "cowboy hat": {"price": 15, "icon": "🤠"},
    "top hat": {"price": 20, "icon": "🎩"},
    "crown": {"price": 30, "icon": "👑"},
}


WHEEL_ONLY_CAPS = ["wizard hat", "pirate hat", "party hat"]
CAP_ICONS = {
    "wizard hat": "🧙",
    "pirate hat": "🏴‍☠️",
    "party hat": "🎉"
}

def save_users():
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=2)

def login_window():
    login = tk.Toplevel(root)
    login.title("Login")
    login.geometry("400x300")
    login.configure(bg="black")

    canvas = tk.Canvas(login, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    chars = "0 1 0 1 1 0 1 0 1 1 0 1"
    columns = 40
    drops = [0 for _ in range(columns)]

    matrix_job = None  

    def draw_matrix():
        nonlocal matrix_job
        if not login.winfo_exists():  
            return
        canvas.delete("matrix")
        for i in range(columns):
            char = random.choice(chars)
            x = i * 10
            y = drops[i] * 15
            canvas.create_text(x, y, text=char, fill="lime", font=("Courier", 10), tags="matrix")
            drops[i] = 0 if y > 300 and random.random() > 0.975 else drops[i] + 1
        matrix_job = canvas.after(50, draw_matrix)

    def stop_matrix():
        
        nonlocal matrix_job
        if matrix_job is not None:
            try:
                canvas.after_cancel(matrix_job)
            except tk.TclError:
                pass
            matrix_job = None

    draw_matrix()

    
    def on_close():
        stop_matrix()
        login.destroy()
    login.protocol("WM_DELETE_WINDOW", on_close)

    frame = tk.Frame(login, bg="black")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    def login_user():
        user = username.get()
        pwd = password.get()
        if user in users and users[user]["password"] == pwd:
            global current_user
            current_user = user
            if "tokens" not in users[user]:
                users[user]["tokens"] = 0
                users[user]["unlocked"] = ["green"]
                users[user]["equipped"] = "green"
                users[user]["caps_unlocked"] = ["none"]
                users[user]["cap_equipped"] = "none"
            messagebox.showinfo("Success", f"Welcome, {user}")
            stop_matrix() 
            login.destroy()
            shop_window()
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def register_user():
        user = username.get()
        pwd = password.get()
        if user in users:
            messagebox.showerror("Error", "User already exists.")
        else:
            users[user] = {
                "password": pwd,
                "highscore": 0,
                "tokens": 0,
                "unlocked": ["green"],
                "equipped": "green",
                "caps_unlocked": ["none"],
                "cap_equipped": "none"
            }
            save_users()
            messagebox.showinfo("Success", "User registered!")

    tk.Label(frame, text="Username:", fg="lime", bg="black", font=("Courier", 10)).pack(pady=5)
    username = tk.Entry(frame, bg="black", fg="lime", insertbackground='lime', font=("Courier", 10))
    username.pack()

    tk.Label(frame, text="Password:", fg="lime", bg="black", font=("Courier", 10)).pack(pady=5)
    password = tk.Entry(frame, show="*", bg="black", fg="lime", insertbackground='lime', font=("Courier", 10))
    password.pack()

    tk.Button(frame, text="Login", command=login_user, bg="black", fg="lime", font=("Courier", 10)).pack(pady=5)
    tk.Button(frame, text="Register", command=register_user, bg="black", fg="lime", font=("Courier", 10)).pack()

def shop_window():
    shop = tk.Toplevel(root)
    shop.title("Shop")
    shop.geometry("500x500")
    shop.configure(bg="black")

    tk.Label(shop, text="🛍️ Snake Customization", fg="lime", bg="black", font=("Courier", 14)).pack(pady=10)

    token_label = tk.Label(shop, text=f"Tokens: {users[current_user]['tokens']}", fg="lime", bg="black", font=("Courier", 12))
    token_label.pack()

    frame = tk.Frame(shop, bg="black")
    frame.pack(pady=10)

    def update_colors():
        for widget in frame.winfo_children():
            widget.destroy()
        token_label.config(text=f"Tokens: {users[current_user]['tokens']}")
        for color, info in COLOR_OPTIONS.items():
            unlocked = color in users[current_user]['unlocked']
            btn_text = f"{color.capitalize()} - {'Owned' if unlocked else f'{info['price']} Tokens'}"
            btn_state = "normal" if unlocked or users[current_user]['tokens'] >= info['price'] else "disabled"
            def buy_equip(c=color):
                if c in users[current_user]['unlocked']:
                    users[current_user]['equipped'] = c
                elif users[current_user]['tokens'] >= COLOR_OPTIONS[c]['price']:
                    users[current_user]['tokens'] -= COLOR_OPTIONS[c]['price']
                    users[current_user]['unlocked'].append(c)
                    users[current_user]['equipped'] = c
                save_users()
                update_colors()
            tk.Button(frame, text=btn_text, command=buy_equip,
                      state=btn_state, bg="black", fg=COLOR_OPTIONS[color]['head'], font=("Courier", 10)).pack(pady=2)

    def update_caps():
        for widget in frame.winfo_children():
            widget.destroy()
        token_label.config(text=f"Tokens: {users[current_user]['tokens']}")
        for cap, info in CAP_OPTIONS.items():
            unlocked = cap in users[current_user]['caps_unlocked']
            btn_text = f"{cap.capitalize()} - {'Owned' if unlocked else f'{info['price']} Tokens'}"
            btn_state = "normal" if unlocked or users[current_user]['tokens'] >= info['price'] else "disabled"
            def buy_equip_cap(c=cap):
                if c in users[current_user]['caps_unlocked']:
                    users[current_user]['cap_equipped'] = c
                elif users[current_user]['tokens'] >= CAP_OPTIONS[c]['price']:
                    users[current_user]['tokens'] -= CAP_OPTIONS[c]['price']
                    users[current_user]['caps_unlocked'].append(c)
                    users[current_user]['cap_equipped'] = c
                save_users()
                update_caps()
            tk.Button(frame, text=btn_text, command=buy_equip_cap,
                      state=btn_state, bg="black", fg="lime", font=("Courier", 10)).pack(pady=2)

    def spin_wheel():
        if users[current_user]['tokens'] < 20:
            messagebox.showerror("Error", "Not enough tokens!")
            return
        users[current_user]['tokens'] -= 20
        available_caps = [cap for cap in WHEEL_ONLY_CAPS if cap not in users[current_user]['caps_unlocked']]
        if not available_caps:
            messagebox.showinfo("Wheel", "You already own all exclusive caps!")
            return
        prize = random.choice(available_caps)
        users[current_user]['caps_unlocked'].append(prize)
        messagebox.showinfo("🎡 Wheel Result", f"You won a {prize} {CAP_ICONS[prize]}!")
        save_users()
        update_caps()

    tk.Button(shop, text="🎨 Colors", command=update_colors, bg="black", fg="lime").pack(side="left", padx=5)
    tk.Button(shop, text="🎩 Caps", command=update_caps, bg="black", fg="lime").pack(side="left", padx=5)
    tk.Button(shop, text="🎡 Spin Wheel (20 Tokens)", command=spin_wheel, bg="black", fg="yellow").pack(side="left", padx=5)
    tk.Button(shop, text="▶ Start Game", command=lambda:[shop.destroy(), start_game()], bg="black", fg="lime").pack(side="right", padx=5)

    update_colors()

CELL_SIZE = 30
GRID_WIDTH = 15
GRID_HEIGHT = 15

class SnakeGame(tk.Canvas):
    def __init__(self, parent):
        width = GRID_WIDTH * CELL_SIZE
        height = GRID_HEIGHT * CELL_SIZE
        super().__init__(parent, width=width, height=height, bg="gray10", highlightthickness=0)
        self.parent = parent
        self.snake = [(5, 5)]
        self.food = None
        self.direction = "Right"
        self.running = True
        self.paused = False
        self.score = 0
        self.matrix_chars = "0 1 0 1 0 1 0 1 "
        self.matrix_drops = [0 for _ in range(GRID_WIDTH)]
        self.bind_all("<Key>", self.change_direction)
        self.spawn_food()
        self.animate_background()
        self.game_loop()

    def change_direction(self, event):
        key = event.keysym.lower()
        key_map = {'w': 'Up', 's': 'Down', 'a': 'Left', 'd': 'Right'}
        if key in key_map:
            new_dir = key_map[key]
            opposite = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
            if new_dir != opposite.get(self.direction):
                self.direction = new_dir
        elif key == 'p':
            self.paused = not self.paused
            self.draw_pause_message()

    def draw_pause_message(self):
        self.delete("pause")
        if self.paused:
            self.create_text(self.winfo_width() // 2, self.winfo_height() // 2,
                             text="PAUSED", fill="lime", font=("Courier", 24), tag="pause")

    def spawn_food(self):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def animate_background(self):
        self.delete("bg")
        for i in range(GRID_WIDTH):
            char = random.choice(self.matrix_chars)
            x = i * CELL_SIZE + CELL_SIZE // 2
            y = self.matrix_drops[i] * CELL_SIZE
            self.create_text(x, y, text=char, fill="darkgreen",
                             font=("Courier", 10), tags="bg")
            if y > GRID_HEIGHT * CELL_SIZE or random.random() > 0.975:
                self.matrix_drops[i] = 0
            else:
                self.matrix_drops[i] += 1
        self.after(100, self.animate_background)

    def game_loop(self):
        if not self.running:
            return
        if not self.paused:
            self.move_snake()
            self.check_collisions()
            self.draw()
        self.after(150, self.game_loop)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= 1
        elif self.direction == "Down":
            head_y += 1
        elif self.direction == "Left":
            head_x -= 1
        elif self.direction == "Right":
            head_x += 1
        new_head = (head_x, head_y)

        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.score += 1
            if self.score % 5 == 0:
                users[current_user]["tokens"] += 1
            self.spawn_food()
            if SOUND_ENABLED:
                winsound.Beep(1000, 100)
        else:
            self.snake = [new_head] + self.snake[:-1]

    def check_collisions(self):
        head = self.snake[0]
        if (
            head in self.snake[1:] or
            not (0 <= head[0] < GRID_WIDTH) or
            not (0 <= head[1] < GRID_HEIGHT)
        ):
            self.running = False
            self.save_score()
            self.show_leaderboard()

    def save_score(self):
        if current_user:
            users[current_user]["highscore"] = max(
                users[current_user]["highscore"], self.score
            )
            save_users()

    def draw(self):
        self.delete("snake")
        for i in range(GRID_WIDTH + 1):
            x = i * CELL_SIZE
            self.create_line(x, 0, x, GRID_HEIGHT * CELL_SIZE, fill="gray20", tags="snake")
        for j in range(GRID_HEIGHT + 1):
            y = j * CELL_SIZE
            self.create_line(0, y, GRID_WIDTH * CELL_SIZE, y, fill="gray20", tags="snake")

        fx, fy = self.food
        self.create_rectangle(fx * CELL_SIZE, fy * CELL_SIZE,
                              (fx + 1) * CELL_SIZE, (fy + 1) * CELL_SIZE,
                              fill="lime", outline="", tags="snake")

        colors = COLOR_OPTIONS[users[current_user]["equipped"]]
        cap_equipped = users[current_user].get("cap_equipped", "none")
        cap_icon = ""
        if cap_equipped in CAP_OPTIONS:
            cap_icon = CAP_OPTIONS[cap_equipped]["icon"]
        elif cap_equipped in CAP_ICONS:
            cap_icon = CAP_ICONS[cap_equipped]

        for i, (x, y) in enumerate(self.snake):
            color = colors["head"] if i == 0 else colors["body"]
            self.create_rectangle(x * CELL_SIZE, y * CELL_SIZE,
                                  (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                                  fill=color, outline="gray25", tags="snake")
            if i == 0 and cap_icon:
                self.create_text(x * CELL_SIZE + CELL_SIZE//2, y * CELL_SIZE - 5,
                                 text=cap_icon, font=("Arial", 14), tags="snake")

        self.create_text(10, 10, anchor="nw", fill="lime",
                         font=("Courier", 12), text=f"Score: {self.score}", tags="snake")

    def show_leaderboard(self):
        leaderboard = sorted(users.items(), key=lambda item: item[1]["highscore"], reverse=True)[:5]
        scores = "\n".join([f"{i+1}. {u[0]} - {u[1]['highscore']}" for i, u in enumerate(leaderboard)])
        messagebox.showinfo("Leaderboard", f"\U0001F3C6 High Scores \U0001F3C6\n\n{scores}")
        self.parent.destroy()

def start_game():
    game = SnakeGame(root)
    game.pack()

root = tk.Tk()
root.title("Hacking Snake game made by Leonxzy")
root.configure(bg="black")
root.geometry("500x500")
login_window()
root.mainloop()








time.sleep(1)

print("\033[33mPynux is made by Leon and Marko. For any technical issues or bugs, contact: leon.hodzic@outlook.com\033[0m")

time.sleep(5000)