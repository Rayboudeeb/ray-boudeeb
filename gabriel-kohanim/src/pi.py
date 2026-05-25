

# code snippet for example
object_label = "sdf"
def execute_grasp(coords):
    # Code to control the robot to grasp the object at the given coordinates
    pass
cup_coords = (x1, y1, z1)  # Coordinates for the cup
bottle_coords = (x2, y2, z2)  # Coordinates for the bottle


# Classical robot: rigid, brittle
if object_label == "cup":
    execute_grasp(cup_coords) 
elif object_label == "bottle":
    execute_grasp(bottle_coords)
# What if it's a mug? A thermos? Anything unlabeled?
# → robot does nothing




def token_id(value):
    # Convert the value to a discrete token ID (0-255)
    # This is a placeholder for the actual discretization logic
    return int((value + 1) / 2 * 255)  # Example: map [-1, 1] to [0, 255]






# Simplified: RT-2 action token representation
# Each action = 7 values discretized into 256 bins → treated as text tokens

action = {
    "delta_x":    token_id("+0.03m"),   # arm moves right
    "delta_y":    token_id("-0.01m"),
    "delta_z":    token_id("0.00m"),
    "roll":       token_id("0.0"),
    "pitch":      token_id("+0.05"),
    "yaw":        token_id("0.0"),
    "gripper":    token_id("close")
}
# The model outputs this as a sequence, just like generating a sentence

#Chain-of-thought: plan before act
'''
Instruction: "Throw away the empty wrapper"

Plan:   "Crumpled silver object near the bottle is likely
         food packaging. Classify as trash.
         Sequence: move to object → grasp → transport to bin."

Action: [delta_x: +0.12] [delta_y: -0.03] [gripper: open]
        [move_to: bin_coords] [gripper: close→open]

'''