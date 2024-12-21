import tkinter as tk
import time

def gradient_transition(label, start_color, end_color, description_label, description, steps=100, duration=2):
    def hex_color(r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"

    start_r = int(start_color[1:3], 16)
    start_g = int(start_color[3:5], 16)
    start_b = int(start_color[5:7], 16)

    end_r = int(end_color[1:3], 16)
    end_g = int(end_color[3:5], 16)
    end_b = int(end_color[5:7], 16)

    step_time = duration / steps

    for step in range(steps + 1):
        r = int(start_r + (end_r - start_r) * (step / steps))
        g = int(start_g + (end_g - start_g) * (step / steps))
        b = int(start_b + (end_b - start_b) * (step / steps))
        label.config(bg=hex_color(r, g, b))
        label.update()
        description_label.update()
        time.sleep(step_time)

def show_color_and_info():
    emotion = emotion_var.get()
    if emotion == "기쁨":
        colors = ["#FFFFE0", "#FFFACD", "#FAFAD2", "#FFEFD5", "#FFD700", "#FFF8DC", "#FFE4B5", "#FFDAB9", "#EEE8AA", "#F0E68C"]
        description = "활기차고 즐거운 분위기의 노랑은 밝고 긍정적인 활력과 지칠 줄 모르는 에너지를 증폭시킵니다."
    elif emotion == "불안감":
        colors = ["#B0E0E6", "#ADD8E6", "#87CEEB", "#87CEFA", "#4682B4", "#5F9EA0", "#B0C4DE", "#AFEEEE", "#E0FFFF", "#00CED1"]
        description = "파랑은 급한 마음을 진정시키고 지친 마음에 여유와 안정감을 줍니다."
    elif emotion == "스트레스":
        colors = ["#98FB98", "#90EE90", "#00FF7F", "#7CFC00", "#32CD32", "#228B22", "#008000", "#006400", "#ADFF2F", "#9ACD32"]
        description = "노랑과 파랑의 중간색이자 모든 색 중간위치의 초록은 균형과 편안함을 상징하며, 스트레스를 완화하고 평온함을 줍니다."
    elif emotion == "무기력":
        colors = ["#FFA07A", "#FA8072", "#E9967A", "#F08080", "#CD5C5C", "#DC143C", "#B22222", "#FF6347", "#FF4500", "#FF0000"]
        description = "사랑과 열정을 상징하는 빨간색은 기운을 북돋아, 일을 역동적으로 추진할 수 있도록 도와줍니다."
    elif emotion == "우울함":
        colors = ["#DDA0DD", "#EE82EE", "#DA70D6", "#BA55D3", "#9932CC", "#9400D3", "#8A2BE2", "#8B008B", "#9370DB", "#D8BFD8"]
        description = "보라색은 직관적이고 감각적인 정신 활동에 도움을 주는 색으로 내면의 균형을 잡고 위로를 제공합니다."
    elif emotion == "상실감":
        colors = ["#FFDAB9", "#FFE4B5", "#FFE4C4", "#FFDEAD", "#F4A460", "#D2691E", "#FFA500", "#FF8C00", "#FF7F50", "#FF6347"]
        description = "몸을 따뜻하게 하고 정신을 고양하는 주황색은 슬픔과 상실감에 도움을 줍니다."
    else:
        tk.messagebox.showerror("Error", "감정을 선택해주세요!")
        return

    # Show the description immediately
    description_label.config(text=description)

    # Transition through the colors with gradient effect
    for i in range(len(colors) - 1):
        gradient_transition(color_label, colors[i], colors[i + 1], description_label, description)

# Create the main window
root = tk.Tk()
root.title("컬러 테라피")
root.geometry("400x600")

# Emotion selection
emotion_var = tk.StringVar(value="")

emotion_label = tk.Label(root, text="오늘의 감정을 선택하세요:")
emotion_label.pack(pady=10)

emotions = ["기쁨", "불안감", "스트레스", "무기력", "우울함", "상실감"]
for emotion in emotions:
    tk.Radiobutton(root, text=emotion, variable=emotion_var, value=emotion).pack(anchor="w")

# Submit button
submit_button = tk.Button(root, text="확인", command=show_color_and_info)
submit_button.pack(pady=20)

# Color display label
color_label = tk.Label(root, text="", width=50, height=15, bg="white")
color_label.pack(pady=10)

# Description display label
description_label = tk.Label(root, text="", wraplength=350, bg="white")
description_label.pack(pady=10)

# Run the application
root.mainloop()