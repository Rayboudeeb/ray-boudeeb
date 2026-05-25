# When LLMs Learn to Move: Language Models as Robot Brains
### CS131 — Discrete Structures | Spring 2026 | Pierce College


---

##  Topic Overview

This project explores **Vision-Language-Action (VLA) models**  a class of AI systems that connect large language models directly to physical robot control. The central case study is **RT-2 (Robotics Transformer 2)**, published by Google DeepMind in 2023, which was the first model to prove that internet-scale language pretraining could transfer to real-world robotic tasks.

The presentation also covers the current state of humanoid robotics in 2026, including the **Beijing E-Town Half-Marathon** (April 2026), where a humanoid robot completed a 21km course faster than any human world record, autonomously.

---

##  Key Concepts Covered

- **Classical robotics vs. LLM-driven robotics** —> why hardcoded control pipelines fail at generalization
- **Vision-Language-Action (VLA) models** —> how RT-2 unifies perception, language, and action into one transformer
- **Action tokenization** —> representing robot motor commands as discrete text tokens
- **Chain-of-thought reasoning in physical tasks** —> how RT-2 plans before it acts
- **The embodied AI landscape in 2026** —> Gemini Robotics, Unitree, Agibot, and the US-China robotics race

---

##  Code Snippets

### Classical control, brittleness problem
```python
# Classical robot: rigid, task-specific
if object_label == "cup":
    execute_grasp(cup_coords)
elif object_label == "bottle":
    execute_grasp(bottle_coords)
# fails on anything unlabeled — no semantic understanding
```

### RT-2 action token representation
```python
# RT-2 discretizes continuous motor commands into 256 bins
# each bin maps to a token ID — the same format as text output

action = {
    "delta_x":  token_id("+0.03m"),  # arm moves right
    "delta_y":  token_id("-0.01m"),
    "delta_z":  token_id("0.00m"),
    "roll":     token_id("0.0"),
    "pitch":    token_id("+0.05"),
    "yaw":      token_id("0.0"),
    "gripper":  token_id("close")
}
# model outputs this sequence the same way it outputs words
```

### Chain-of-thought: plan before act
```
Instruction: "Throw away the empty wrapper"

Plan:   "Crumpled silver object near the bottle is likely
         food packaging. Classify as trash.
         Sequence: move to object → grasp → transport to bin."

Action: [delta_x: +0.12] [delta_y: -0.03] [gripper: open]
        [move_to: bin_coords] [gripper: close→open]
```

---

##  Timeline: VLA Model Evolution

| Year | Model | Milestone |
|------|-------|-----------|
| 2022 | RT-1 | Multi-task robot control, no language reasoning |
| 2023 | **RT-2** | First VLA — LLM reasoning transferred to physical action |
| 2024 | AutoRT / SARA-RT | Multi-robot coordination, 14% faster inference |
| 2026 | Gemini Robotics | RT-2 paradigm + Gemini foundation model |
| 2026 | Unitree / Agibot | 5,000+ humanoid units shipped using VLA principles |

---

##  Sources & Further Reading

- [RT-2 Paper — arXiv 2307.15818](https://arxiv.org/abs/2307.15818)
- [Google DeepMind RT-2 Blog](https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/)
- [Google DeepMind — Shaping the Future of Advanced Robotics](https://deepmind.google/discover/blog/shaping-the-future-of-advanced-robotics/)
- [Beijing Half-Marathon Robot Breaks World Record — Al Jazeera](https://www.aljazeera.com/sports/2026/4/19/humanoid-robot-breaks-half-marathon-world-record-in-beijing)
- [China Leads the Humanoid Robot Race — Rest of World](https://restofworld.org/2026/china-humanoid-robots-unitree-agibot-tesla-optimus/)
- [China vs Tesla Robot Race — Rest of World](https://restofworld.org/2026/china-tesla-robot-race/)
- [RT-2 Deep Dive — Toward Humanoids, Medium](https://medium.com/correll-lab/what-happens-when-a-language-model-controls-a-robot-a-review-of-rt-2-709e60ea9081)

---

## 👤 Author

**Gabriel Kohanim**
Pierce College — CS131, Spring 2026
