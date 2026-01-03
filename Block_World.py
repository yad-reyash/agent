import tkinter as tk
import time
import copy
from collections import deque


class BlockWorldAgent:
    """AI Agent that uses STRIPS-like planning to solve Block World problems"""
    
    def __init__(self, world):
        self.world = world
        self.blocks = ["A", "B", "C"]
    
    def get_state(self, world):
        """Get current state as a hashable tuple"""
        return (tuple(sorted(world.on.items())), 
                tuple(sorted(world.clear.items())), 
                world.holding)
    
    def clone_world(self, world):
        """Create a copy of the world state"""
        new_world = BlockWorld()
        new_world.on = dict(world.on)
        new_world.clear = dict(world.clear)
        new_world.holding = world.holding
        return new_world
    
    def get_possible_actions(self, world):
        """Generate all possible valid actions from current state"""
        actions = []
        
        for block in self.blocks:
            # Try pick_up
            if world.holding is None and world.on[block] == "table" and world.clear[block]:
                actions.append(("pick_up", block, None))
            
            # Try put_down
            if world.holding == block:
                actions.append(("put_down", block, None))
            
            # Try unstack
            target = world.on[block]
            if target and target != "table" and world.clear[block] and world.holding is None:
                actions.append(("unstack", block, None))
            
            # Try stack
            if world.holding is not None:
                for target in self.blocks:
                    if target != world.holding and world.clear[target]:
                        actions.append(("stack", world.holding, target))
        
        return actions
    
    def apply_action(self, world, action):
        """Apply an action to a world state and return success"""
        action_type, block, target = action
        
        if action_type == "pick_up":
            return world.pick_up(block)[0]
        elif action_type == "put_down":
            return world.put_down(block)[0]
        elif action_type == "unstack":
            return world.unstack(block)[0]
        elif action_type == "stack":
            return world.stack(block, target)[0]
        return False
    
    def goal_reached(self, world, goal):
        """Check if the goal state is reached"""
        for block, target in goal.items():
            if world.on[block] != target:
                return False
        return world.holding is None
    
    def plan_bfs(self, goal):
        """Use BFS to find a plan to reach the goal state"""
        start_state = self.get_state(self.world)
        
        if self.goal_reached(self.world, goal):
            return []
        
        queue = deque([(self.clone_world(self.world), [])])
        visited = {start_state}
        
        while queue:
            current_world, plan = queue.popleft()
            
            for action in self.get_possible_actions(current_world):
                new_world = self.clone_world(current_world)
                if self.apply_action(new_world, action):
                    new_state = self.get_state(new_world)
                    
                    if new_state not in visited:
                        new_plan = plan + [action]
                        
                        if self.goal_reached(new_world, goal):
                            return new_plan
                        
                        visited.add(new_state)
                        queue.append((new_world, new_plan))
        
        return None


class BlockWorld:
    def __init__(self):
        self.on = {"A": "table", "B": "table", "C": "A"}
        self.clear = {"A": False, "B": True, "C": True}
        self.holding = None

    def pick_up(self, block):
        if self.holding is None and self.on[block] == "table" and self.clear[block]:
            self.holding = block
            self.on[block] = None
            self.clear[block] = True
            return True, f"Picked up {block}"
        return False, f"Cannot pick up {block}"

    def put_down(self, block):
        if self.holding == block:
            self.on[block] = "table"
            self.holding = None
            return True, f"Put down {block} on table"
        return False, f"Cannot put down {block}"

    def stack(self, block, target):
        if self.holding == block and self.clear[target]:
            self.on[block] = target
            self.clear[target] = False
            self.holding = None
            return True, f"Stacked {block} on {target}"
        return False, f"Cannot stack {block} on {target}"

    def unstack(self, block):
        target = self.on[block]
        if target and target != "table" and self.clear[block] and self.holding is None:
            self.holding = block
            self.on[block] = None
            self.clear[target] = True
            return True, f"Unstacked {block} from {target}"
        return False, f"Cannot unstack {block}"

    def reset(self):
        self.on = {"A": "table", "B": "table", "C": "A"}
        self.clear = {"A": False, "B": True, "C": True}
        self.holding = None


class BlockWorldGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Block World AI Agent - Autonomous Solver")
        self.root.geometry("750x580")
        self.root.configure(bg="#1a1a2e")
        
        self.world = BlockWorld()
        self.agent = BlockWorldAgent(self.world)
        self.block_colors = {"A": "#e94560", "B": "#0f3460", "C": "#16c79a"}
        self.block_size = 70
        self.table_positions = {"A": 150, "B": 350, "C": 550}
        self.current_plan = []
        
        self.goals = [
            ("Build A-B-C Tower", {"A": "table", "B": "A", "C": "B"}),
            ("Build C-B-A Tower", {"A": "B", "B": "C", "C": "table"}),
            ("All Blocks on Table", {"A": "table", "B": "table", "C": "table"}),
        ]
        self.current_goal_index = 0
        self.is_running = False
        
        self.setup_ui()
        self.draw_state()

    def setup_ui(self):
        title_frame = tk.Frame(self.root, bg="#1a1a2e")
        title_frame.pack(pady=15)
        
        title = tk.Label(title_frame, text="Block World AI Agent", 
                        font=("Segoe UI", 28, "bold"), fg="#eaeaea", bg="#1a1a2e")
        title.pack()
        
        subtitle = tk.Label(title_frame, text="Fully Autonomous Problem Solver", 
                           font=("Segoe UI", 14), fg="#16c79a", bg="#1a1a2e")
        subtitle.pack()

        self.canvas = tk.Canvas(self.root, width=700, height=280, bg="#16213e", 
                               highlightthickness=2, highlightbackground="#0f3460")
        self.canvas.pack(pady=15)
        
        self.canvas.create_rectangle(20, 230, 680, 260, fill="#4a4a6a", outline="#6a6a8a", width=2)
        self.canvas.create_text(350, 245, text="TABLE", font=("Segoe UI", 12, "bold"), fill="#eaeaea")

        info_frame = tk.Frame(self.root, bg="#0f3460", padx=20, pady=15)
        info_frame.pack(fill="x", padx=20, pady=10)
        
        self.goal_label = tk.Label(info_frame, text="Goal: Ready to start", 
                                   font=("Segoe UI", 16, "bold"), fg="#f39c12", bg="#0f3460")
        self.goal_label.pack()
        
        self.status_label = tk.Label(info_frame, text="Press START to begin", 
                                     font=("Segoe UI", 13), fg="#f39c12", bg="#0f3460")
        self.status_label.pack(pady=5)
        
        self.plan_label = tk.Label(info_frame, text="", 
                                   font=("Consolas", 11), fg="#eaeaea", bg="#0f3460", wraplength=650)
        self.plan_label.pack()

        self.holding_label = tk.Label(info_frame, text="Holding: None", 
                                      font=("Segoe UI", 11), fg="#eaeaea", bg="#0f3460")
        self.holding_label.pack(pady=5)

        # Button frame
        btn_frame = tk.Frame(self.root, bg="#1a1a2e")
        btn_frame.pack(pady=15)
        
        self.start_btn = tk.Button(btn_frame, text="▶ START", command=self.start_agent,
                                   font=("Segoe UI", 14, "bold"), bg="#16c79a", fg="#1a1a2e",
                                   padx=30, pady=10, cursor="hand2")
        self.start_btn.pack(side="left", padx=10)
        
        self.restart_btn = tk.Button(btn_frame, text="🔄 RESTART", command=self.restart_agent,
                                     font=("Segoe UI", 14, "bold"), bg="#e94560", fg="white",
                                     padx=30, pady=10, cursor="hand2")
        self.restart_btn.pack(side="left", padx=10)

    def draw_state(self):
        self.canvas.delete("block")
        block_positions = {}
        
        for block in ["A", "B", "C"]:
            if self.world.on[block] == "table":
                x = self.table_positions[block]
                y = 230 - self.block_size
                block_positions[block] = (x, y)
            elif self.world.on[block] is None and self.world.holding == block:
                block_positions[block] = (350, 30)
        
        for _ in range(3):
            for block in ["A", "B", "C"]:
                target = self.world.on[block]
                if target and target != "table" and target in block_positions and block not in block_positions:
                    base_x, base_y = block_positions[target]
                    block_positions[block] = (base_x, base_y - self.block_size)
        
        for block, (x, y) in block_positions.items():
            self.draw_block(block, x, y)
        
        holding_text = self.world.holding if self.world.holding else "None"
        self.holding_label.config(text=f"Holding: {holding_text}")

    def draw_block(self, block, x, y):
        color = self.block_colors[block]
        self.canvas.create_rectangle(x - self.block_size//2 + 3, y + 3,
                                     x + self.block_size//2 + 3, y + self.block_size + 3,
                                     fill="#0a0a1a", outline="", tags="block")
        self.canvas.create_rectangle(x - self.block_size//2, y,
                                     x + self.block_size//2, y + self.block_size,
                                     fill=color, outline="#eaeaea", width=2, tags="block")
        self.canvas.create_text(x, y + self.block_size//2, text=block,
                               font=("Segoe UI", 24, "bold"), fill="white", tags="block")

    def format_action(self, action):
        action_type, block, target = action
        if action_type == "pick_up":
            return f"pick_up({block})"
        elif action_type == "put_down":
            return f"put_down({block})"
        elif action_type == "unstack":
            return f"unstack({block})"
        elif action_type == "stack":
            return f"stack({block}, {target})"
        return str(action)

    def start_agent(self):
        """Start the agent when button is clicked"""
        if not self.is_running:
            self.is_running = True
            self.start_btn.config(state="disabled", bg="#4a4a6a")
            self.start_next_goal()

    def restart_agent(self):
        """Restart the agent from beginning"""
        self.is_running = False
        self.current_goal_index = 0
        self.current_plan = []
        self.world.reset()
        self.draw_state()
        self.goal_label.config(text="Goal: Ready to start")
        self.status_label.config(text="Press START to begin", fg="#f39c12")
        self.plan_label.config(text="")
        self.start_btn.config(state="normal", bg="#16c79a")

    def start_next_goal(self):
        if not self.is_running:
            return
        goal_name, goal = self.goals[self.current_goal_index]
        
        self.goal_label.config(text=f"Goal: {goal_name}")
        self.status_label.config(text="Agent Planning...", fg="#f39c12")
        self.root.update()
        
        self.agent = BlockWorldAgent(self.world)
        plan = self.agent.plan_bfs(goal)
        
        if plan is None:
            self.status_label.config(text="No solution exists!", fg="#e94560")
            self.root.after(2000, self.move_to_next_goal)
        elif len(plan) == 0:
            self.status_label.config(text="Goal already achieved!", fg="#16c79a")
            self.plan_label.config(text="No actions needed")
            self.root.after(2000, self.move_to_next_goal)
        else:
            self.current_plan = plan
            plan_str = " -> ".join([self.format_action(a) for a in plan])
            self.plan_label.config(text=f"Plan: {plan_str}")
            self.status_label.config(text=f"Executing plan ({len(plan)} steps)...", fg="#16c79a")
            self.root.after(1000, lambda: self.execute_plan_step(0))

    def execute_plan_step(self, index):
        if index >= len(self.current_plan):
            self.status_label.config(text="Goal Achieved! Press RESTART to try again.", fg="#16c79a")
            self.is_running = False
            self.start_btn.config(state="normal", bg="#16c79a")
            return
        
        action = self.current_plan[index]
        action_type, block, target = action
        
        if action_type == "pick_up":
            success, msg = self.world.pick_up(block)
        elif action_type == "put_down":
            success, msg = self.world.put_down(block)
        elif action_type == "unstack":
            success, msg = self.world.unstack(block)
        elif action_type == "stack":
            success, msg = self.world.stack(block, target)
        
        step_num = index + 1
        total = len(self.current_plan)
        self.status_label.config(text=f"Step {step_num}/{total}: {msg}", 
                                fg="#16c79a" if success else "#e94560")
        self.draw_state()
        self.root.after(1000, lambda: self.execute_plan_step(index + 1))

    def move_to_next_goal(self):
        self.current_goal_index = (self.current_goal_index + 1) % len(self.goals)
        
        if self.current_goal_index == 0:
            self.world.reset()
            self.draw_state()
            self.status_label.config(text="Resetting world...", fg="#f39c12")
            self.root.after(1500, self.start_next_goal)
        else:
            self.start_next_goal()


if __name__ == "__main__":
    root = tk.Tk()
    app = BlockWorldGUI(root)
    root.mainloop()
