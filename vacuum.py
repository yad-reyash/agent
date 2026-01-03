import tkinter as tk
import random
import time

# ====================================
# VACUUM CLEANER AGENT
# ====================================

class VacuumAgent:
    """AI Agent that cleans the room while avoiding obstacles"""
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.direction = 0  # 0=Up, 1=Right, 2=Down, 3=Left
        self.cleaned_count = 0
        self.moves_count = 0
    
    def get_position(self):
        return (self.row, self.col)
    
    def move_forward(self, grid_size):
        """Move in current direction"""
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
        dr, dc = directions[self.direction]
        new_row = self.row + dr
        new_col = self.col + dc
        return new_row, new_col
    
    def turn_right(self):
        self.direction = (self.direction + 1) % 4
    
    def turn_left(self):
        self.direction = (self.direction - 1) % 4
    
    def get_direction_name(self):
        names = ["↑ Up", "→ Right", "↓ Down", "← Left"]
        return names[self.direction]


class Room:
    """The room environment with dirt and obstacles"""
    
    # Cell types
    CLEAN = 0
    DIRTY = 1
    OBSTACLE = 2
    AGENT = 3
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[self.CLEAN for _ in range(cols)] for _ in range(rows)]
        self.total_dirty = 0
    
    def add_dirt(self, row, col):
        if self.grid[row][col] == self.CLEAN:
            self.grid[row][col] = self.DIRTY
            self.total_dirty += 1
    
    def add_obstacle(self, row, col):
        self.grid[row][col] = self.OBSTACLE
    
    def is_valid_move(self, row, col):
        """Check if position is valid and not an obstacle"""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col] != self.OBSTACLE
        return False
    
    def is_dirty(self, row, col):
        return self.grid[row][col] == self.DIRTY
    
    def clean_cell(self, row, col):
        if self.grid[row][col] == self.DIRTY:
            self.grid[row][col] = self.CLEAN
            self.total_dirty -= 1
            return True
        return False
    
    def is_obstacle(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col] == self.OBSTACLE
        return True  # Out of bounds is like obstacle
    
    def randomize(self, dirt_probability=0.4, obstacle_probability=0.1, agent_pos=(0, 0)):
        """Randomly place dirt and obstacles"""
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) == agent_pos:
                    continue
                rand = random.random()
                if rand < obstacle_probability:
                    self.add_obstacle(r, c)
                elif rand < obstacle_probability + dirt_probability:
                    self.add_dirt(r, c)


class VacuumGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vacuum Cleaner Agent - Smart Room Cleaning")
        self.root.geometry("800x850")
        self.root.configure(bg="#1a1a2e")
        
        # Room settings
        self.grid_size = 8
        self.cell_size = 60
        
        # Initialize room and agent
        self.room = Room(self.grid_size, self.grid_size)
        self.agent = VacuumAgent(0, 0)
        
        # Colors
        self.colors = {
            "clean": "#2d4059",
            "dirty": "#8b4513",
            "obstacle": "#1a1a2e",
            "agent": "#e94560",
            "grid_line": "#0f3460",
            "detected": "#f39c12"
        }
        
        self.is_running = False
        self.detected_obstacle = None
        
        self.setup_ui()
        self.randomize_room()
        self.draw_room()
    
    def setup_ui(self):
        # BUTTONS AT TOP - START AND NEW ROOM
        btn_frame = tk.Frame(self.root, bg="#1a1a2e")
        btn_frame.pack(pady=15)
        
        self.start_btn = tk.Button(btn_frame, text="START", command=self.start_cleaning,
                                   font=("Arial", 18, "bold"), bg="#00ff00", fg="black",
                                   width=12, height=2, cursor="hand2", relief="raised", bd=5)
        self.start_btn.pack(side="left", padx=20)
        
        self.reset_btn = tk.Button(btn_frame, text="NEW ROOM", command=self.reset_room,
                                   font=("Arial", 18, "bold"), bg="#ff4444", fg="white",
                                   width=12, height=2, cursor="hand2", relief="raised", bd=5)
        self.reset_btn.pack(side="left", padx=20)

        # Title
        title_frame = tk.Frame(self.root, bg="#1a1a2e")
        title_frame.pack(pady=10)
        
        title = tk.Label(title_frame, text="🧹 Vacuum Cleaner Agent", 
                        font=("Segoe UI", 26, "bold"), fg="#eaeaea", bg="#1a1a2e")
        title.pack()
        
        subtitle = tk.Label(title_frame, text="Smart Room Cleaning with Obstacle Detection", 
                           font=("Segoe UI", 12), fg="#16c79a", bg="#1a1a2e")
        subtitle.pack()

        # Canvas for room
        canvas_size = self.grid_size * self.cell_size
        self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size, 
                               bg="#16213e", highlightthickness=2, highlightbackground="#0f3460")
        self.canvas.pack(pady=15)

        # Info panel
        info_frame = tk.Frame(self.root, bg="#0f3460", padx=20, pady=12)
        info_frame.pack(fill="x", padx=20, pady=5)
        
        # Stats row
        stats_frame = tk.Frame(info_frame, bg="#0f3460")
        stats_frame.pack(fill="x")
        
        self.status_label = tk.Label(stats_frame, text="Status: Ready", 
                                     font=("Segoe UI", 13, "bold"), fg="#16c79a", bg="#0f3460")
        self.status_label.pack(side="left")
        
        self.direction_label = tk.Label(stats_frame, text="Direction: ↑ Up", 
                                        font=("Segoe UI", 13), fg="#f39c12", bg="#0f3460")
        self.direction_label.pack(side="right")
        
        # Progress row
        progress_frame = tk.Frame(info_frame, bg="#0f3460")
        progress_frame.pack(fill="x", pady=5)
        
        self.dirt_label = tk.Label(progress_frame, text="Dirt Remaining: 0", 
                                   font=("Segoe UI", 11), fg="#eaeaea", bg="#0f3460")
        self.dirt_label.pack(side="left")
        
        self.cleaned_label = tk.Label(progress_frame, text="Cleaned: 0", 
                                      font=("Segoe UI", 11), fg="#eaeaea", bg="#0f3460")
        self.cleaned_label.pack(side="left", padx=20)
        
        self.moves_label = tk.Label(progress_frame, text="Moves: 0", 
                                    font=("Segoe UI", 11), fg="#eaeaea", bg="#0f3460")
        self.moves_label.pack(side="right")
        
        # Detection info
        self.detect_label = tk.Label(info_frame, text="", 
                                     font=("Segoe UI", 11, "italic"), fg="#f39c12", bg="#0f3460")
        self.detect_label.pack(pady=3)

        # Legend
        legend_frame = tk.Frame(self.root, bg="#1a1a2e")
        legend_frame.pack(pady=5)
        
        legends = [
            ("🟫 Dirty", "#8b4513"),
            ("🟦 Clean", "#2d4059"),
            ("⬛ Obstacle", "#1a1a2e"),
            ("🔴 Agent", "#e94560"),
            ("🟡 Detected", "#f39c12")
        ]
        
        for text, color in legends:
            lbl = tk.Label(legend_frame, text=text, font=("Segoe UI", 10), 
                          fg=color, bg="#1a1a2e")
            lbl.pack(side="left", padx=8)

    def randomize_room(self):
        """Create a new random room"""
        self.room = Room(self.grid_size, self.grid_size)
        self.agent = VacuumAgent(
            random.randint(0, self.grid_size-1),
            random.randint(0, self.grid_size-1)
        )
        self.room.randomize(dirt_probability=0.35, obstacle_probability=0.12, 
                           agent_pos=self.agent.get_position())
        self.detected_obstacle = None
        self.update_labels()

    def draw_room(self):
        """Draw the room grid"""
        self.canvas.delete("all")
        
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                # Determine cell color
                if self.room.grid[r][c] == Room.OBSTACLE:
                    color = self.colors["obstacle"]
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, 
                                                outline=self.colors["grid_line"], width=2)
                    # Draw obstacle symbol
                    self.canvas.create_text(x1 + self.cell_size//2, y1 + self.cell_size//2,
                                           text="🪨", font=("Segoe UI", 20))
                elif self.room.grid[r][c] == Room.DIRTY:
                    color = self.colors["dirty"]
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, 
                                                outline=self.colors["grid_line"], width=2)
                    # Draw dirt particles
                    self.canvas.create_text(x1 + self.cell_size//2, y1 + self.cell_size//2,
                                           text="💩", font=("Segoe UI", 18))
                else:
                    color = self.colors["clean"]
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, 
                                                outline=self.colors["grid_line"], width=2)
                    # Draw sparkle on clean cells
                    self.canvas.create_text(x1 + self.cell_size//2, y1 + self.cell_size//2,
                                           text="✨", font=("Segoe UI", 14))
        
        # Draw detected obstacle highlight
        if self.detected_obstacle:
            dr, dc = self.detected_obstacle
            x1 = dc * self.cell_size
            y1 = dr * self.cell_size
            x2 = x1 + self.cell_size
            y2 = y1 + self.cell_size
            self.canvas.create_rectangle(x1+3, y1+3, x2-3, y2-3, 
                                        outline=self.colors["detected"], width=4)
        
        # Draw agent
        ar, ac = self.agent.get_position()
        ax = ac * self.cell_size + self.cell_size // 2
        ay = ar * self.cell_size + self.cell_size // 2
        
        # Agent body (vacuum cleaner)
        self.canvas.create_oval(ax - 22, ay - 22, ax + 22, ay + 22, 
                               fill=self.colors["agent"], outline="#eaeaea", width=3)
        
        # Direction indicator
        direction_symbols = ["▲", "▶", "▼", "◀"]
        self.canvas.create_text(ax, ay, text=direction_symbols[self.agent.direction],
                               font=("Segoe UI", 16, "bold"), fill="white")

    def update_labels(self):
        """Update all info labels"""
        self.dirt_label.config(text=f"Dirt Remaining: {self.room.total_dirty}")
        self.cleaned_label.config(text=f"Cleaned: {self.agent.cleaned_count}")
        self.moves_label.config(text=f"Moves: {self.agent.moves_count}")
        self.direction_label.config(text=f"Direction: {self.agent.get_direction_name()}")

    def start_cleaning(self):
        """Start the cleaning process"""
        if not self.is_running:
            self.is_running = True
            self.start_btn.config(state="disabled", bg="#4a4a6a")
            self.clean_step()

    def reset_room(self):
        """Reset with a new random room"""
        self.is_running = False
        self.randomize_room()
        self.draw_room()
        self.status_label.config(text="Status: Ready - Press START", fg="#16c79a")
        self.detect_label.config(text="")
        self.start_btn.config(state="normal", bg="#16c79a")

    def sense_environment(self):
        """Agent senses what's ahead"""
        next_row, next_col = self.agent.move_forward(self.grid_size)
        
        # Check for obstacles or boundaries
        if not (0 <= next_row < self.grid_size and 0 <= next_col < self.grid_size):
            return "boundary", None
        elif self.room.is_obstacle(next_row, next_col):
            return "obstacle", (next_row, next_col)
        elif self.room.is_dirty(next_row, next_col):
            return "dirty", (next_row, next_col)
        else:
            return "clean", (next_row, next_col)

    def clean_step(self):
        """Execute one cleaning step"""
        if not self.is_running:
            return
        
        # Check if room is clean
        if self.room.total_dirty == 0:
            self.status_label.config(text="🎉 Room is CLEAN! All done!", fg="#16c79a")
            self.detect_label.config(text="")
            self.is_running = False
            self.start_btn.config(state="normal", bg="#16c79a")
            self.detected_obstacle = None
            self.draw_room()
            return
        
        # Clean current cell if dirty
        current_pos = self.agent.get_position()
        if self.room.is_dirty(current_pos[0], current_pos[1]):
            self.room.clean_cell(current_pos[0], current_pos[1])
            self.agent.cleaned_count += 1
            self.status_label.config(text="🧹 Cleaning current cell...", fg="#16c79a")
            self.detected_obstacle = None
            self.detect_label.config(text="")
            self.update_labels()
            self.draw_room()
            self.root.after(400, self.clean_step)
            return
        
        # Sense environment
        sense_result, target_pos = self.sense_environment()
        
        if sense_result == "boundary":
            self.detect_label.config(text="⚠️ Detected: BOUNDARY ahead! Turning...")
            self.status_label.config(text="🔄 Avoiding boundary", fg="#f39c12")
            self.detected_obstacle = None
            self.agent.turn_right()
            self.agent.moves_count += 1
        
        elif sense_result == "obstacle":
            self.detected_obstacle = target_pos
            self.detect_label.config(text=f"⚠️ Detected: OBSTACLE at ({target_pos[0]}, {target_pos[1]})! Turning...")
            self.status_label.config(text="🔄 Avoiding obstacle", fg="#f39c12")
            self.agent.turn_right()
            self.agent.moves_count += 1
        
        else:
            # Move forward
            self.detected_obstacle = None
            next_row, next_col = self.agent.move_forward(self.grid_size)
            self.agent.row = next_row
            self.agent.col = next_col
            self.agent.moves_count += 1
            
            if sense_result == "dirty":
                self.detect_label.config(text=f"👀 Found DIRT at ({next_row}, {next_col})!")
                self.status_label.config(text="➡️ Moving to dirty cell", fg="#16c79a")
            else:
                self.detect_label.config(text="")
                self.status_label.config(text="➡️ Moving forward", fg="#16c79a")
            
            # Occasionally turn to explore
            if random.random() < 0.15:
                if random.random() < 0.5:
                    self.agent.turn_left()
                else:
                    self.agent.turn_right()
        
        self.update_labels()
        self.draw_room()
        self.root.after(300, self.clean_step)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = VacuumGUI(root)
    root.mainloop()