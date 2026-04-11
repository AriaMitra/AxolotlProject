
"""
Axolotl Rescue Deluxe - Final School Version

How to run:
    python axolotl_game_deluxe_final.py

Important:
- Keep this file in the SAME folder as:
    Axolotl Map - Mexico labeled.png
- Uses only Python standard library (tkinter, random, os)

Features:
- colorful UI
- fact book
- real map image provided by user
- food web
- conservation section
- scrollable long pages
- quiz
- word search
- matching game
- coloring lab
- rescue mini-game
"""

import os
import random
import tkinter as tk
from tkinter import messagebox

WIDTH = 1200
HEIGHT = 820

BG = "#d6f4ff"
DARK = "#103b5c"
ACCENT = "#0d6d8f"
PINK = "#f7b4d5"
WATER = "#95e0ff"
GREEN = "#9ad37a"
SAND = "#f1e2b8"


SPECIES = {
    "common_name": "Axolotl",
    "scientific_name": "Ambystoma mexicanum",
    "status": "Critically Endangered",
    "group": "Amphibian",
    "physical": (
        "Axolotls have a flat head, long tail, four short lizard-like limbs, "
        "feathery external gills, a dorsal body fin, and no movable eyelids. "
        "Wild axolotls are usually darker and mottled, but they can appear in a range of colors."
    ),
    "lifespan": "10–15 years",
    "distribution": (
        "Wild axolotls are native to the Xochimilco wetland-canals of Mexico City. "
        "Historically, they were also found in Lake Chalco."
    ),
    "habitat": (
        "Axolotls live in freshwater habitats such as still-water lakes, canals, and wetlands. "
        "Their best-known natural habitat is the Xochimilco canal system in Mexico City."
    ),
    "biome": (
        "Still-water lakes and freshwater wetland ecosystems."
    ),
    "diet": (
        "Axolotls eat worms, mollusks, crustaceans, insect larvae, tadpoles, and small fish."
    ),
    "interesting_facts": [
        "Axolotls can regenerate limbs, lungs, heart tissue, jaws, spines, and even parts of their brain.",
        "They hunt using a suction-feeding technique that quickly pulls prey into the mouth.",
        "They usually keep their juvenile body form for life instead of fully transforming like many amphibians.",
        "Their external gills look like feathery branches on the sides of the head.",
        "Young axolotls sometimes become cannibals (they eat other axolotls)",
    ],
    "endangered_causes": (
        "Major reasons axolotls are endangered include pollution, habitat degradation, urbanization, "
        "water diversion, and invasive fish such as carp and tilapia."
    ),
    "legislation": (
        "Two important protections are CITES Appendix II and Mexico's NOM-059-SEMARNAT-2010. "
        "CITES helps prevent extinction by regulating international trade so wild axolotls are less likely "
        "to be collected and sold in ways that reduce the natural population. Mexico's legal protection helps "
        "by officially recognizing the species as at risk, which supports habitat restoration, monitoring, "
        "research, conservation planning, and stronger limits on harmful human activities in the species' remaining habitat. "
        "These laws do not necessarily save the axolotl by themselves, but they make conservation efforts more organized and enforceable."
    ),
    "kr": (
        "The axolotl is between an r-selected species and a K-selected species. It shows r-selected traits because it can lay many eggs "
        "and provides very low parental care. However, it also has a K-like limitations because it depends on a very restricted natural habitat. "
        "That small habitat means the species is more easily harmed by pollution, invasive species, drought, and habitat destruction. "
        "So even though axolotls can produce many eggs, their limited habitat makes the whole species vulnerable and contributes to them being critically endangered."
    ),
    "conservation_group": (
        "An example of a conservation group is UNAM's axolotl conservation work in Xochimilco, including refuge projects and the AdoptAxolotl campaign. "
        "These help create better refuge areas, improve water quality, support chinampa farming practices that are better for the wetland, "
        "raise public awareness, fund scientific monitoring, and protect places where axolotls can survive and reproduce. "
        "So the group is not only studying axolotls but also helping restore the ecosystem they need in order to avoid extinction."
    ),
    "extinction_effect": (
        "If axolotls went extinct, the food web would become less stable. In this food web, axolotls eat worms, mollusks, crustaceans, "
        "insect larvae, tadpoles, and small fish. If axolotls disappeared, those prey populations could rise because one of their predators would be gone. "
        "That increase could put heavier pressure on algae, aquatic plants, and other lower food-web organisms, changing nutrient balance and water conditions "
        "in the wetland. Axolotls also acts as a middle-man that helps transfer energy from small aquatic prey to larger predators such as herons. Without axolotls, predators would lose one "
        "native food source, and the balance between prey and predator species in Xochimilco could shift in harmful ways."
    ),
    "invasive": (
        "Invasive species affect axolotls directly through the food web. Carp and tilapia compete with axolotls for prey such as insect larvae, "
        "crustaceans, and other small aquatic organisms. They can also eat axolotl eggs and young axolotls. This means invasive fish reduce the axolotl's food supply "
        "and also reduce the number of young axolotls that survive to adulthood. As invasive fish spread, the food web can shift away from native species and make it even harder "
        "for axolotls to recover."
    ),
    "global_warming": (
        "Global warming makes the axolotl's habitat shallower, warmer, and more stressful. Axolotls thrive in cooler water, so rising temperatures can increase disease risk, "
        "reduce reproduction, and worsen the effects of drought and habitat loss. Lower water levels also disrupt their breeding and make survival harder."
    ),
}

QUIZ = [
    ("What is the scientific name of the axolotl?", ["Ambystoma mexicanum", "Ambystoma axolotl", "Axolotl mexicanus", "Salamandra mexicanum"], "Ambystoma mexicanum"),
    ("What class/group is the axolotl in?", ["Fish", "Bird", "Amphibian", "Reptile"], "Amphibian"),
    ("What biome/ecosystem does it live in?", ["Desert dunes", "Still-water lakes and wetlands", "Ocean reefs", "Arctic tundra"], "Still-water lakes and wetlands"),
    ("Where is its last main natural habitat?", ["Amazon River", "Xochimilco canals", "Great Lakes", "Florida marsh"], "Xochimilco canals"),
    ("Which is a major threat to axolotls?", ["Too much snow", "Pollution and invasive fish", "Volcanoes", "Ocean currents"], "Pollution and invasive fish"),
    ("How do axolotls often catch food?", ["Suction feeding", "Web spinning", "Poison injection", "Seed trapping"], "Suction feeding"),
]

MATCH_TERMS = {
    "External gills": "Used for breathing in water",
    "Xochimilco": "Main remaining natural habitat",
    "Still-water lakes": "Biome/ecosystem type",
    "Tilapia": "Invasive fish threat",
    "Regeneration": "Ability to regrow body parts",
}

WORD_BANK = ["AXOLOTL", "XOCHIMILCO", "GILLS", "MEXICO", "TILAPIA", "REGENERATE", "LAKES", "AMPHIBIAN"]
WORD_GRID = [
    list("AXOLOTLQWERT"),
    list("PLANTSGILLSA"),
    list("QWEMEXICOZXC"),
    list("RTYAMPHIBIAN"),
    list("UIOREGENERAT"),
    list("PASDFGHJKLQA"),
    list("ZXTILAPIAQWE"),
    list("RTLAKESASDFG"),
    list("JKLXOCHIMILC"),
    list("VBNMQWERTYUI"),
]


class AxolotlGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Axolotl Rescue")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.configure(bg=BG)

        self.score = 0
        self.quiz_index = 0
        self.quiz_score = 0

        self.arcade_running = False
        self.arcade_items = []
        self.arcade_food = 0
        self.arcade_trash = 0
        self.arcade_fish = 0
        self.player = None

        self.map_image = None

        self.top = tk.Frame(root, bg=DARK, height=70)
        self.top.pack(fill="x")
        tk.Label(
            self.top, text="Axolotl Rescue Deluxe", font=("Arial", 28, "bold"),
            fg="white", bg=DARK
        ).pack(side="left", padx=20, pady=12)

        self.score_label = tk.Label(
            self.top, text="Score: 0", font=("Arial", 18, "bold"),
            fg="white", bg=DARK
        )
        self.score_label.pack(side="right", padx=20)

        self.main = tk.Frame(root, bg=BG)
        self.main.pack(fill="both", expand=True)

        self.show_home()

    def add_score(self, points):
        self.score += points
        self.score_label.config(text=f"Score: {self.score}")

    def clear(self):
        self.arcade_running = False
        for widget in self.main.winfo_children():
            widget.destroy()

    def nav(self):
        bar = tk.Frame(self.main, bg=BG)
        bar.pack(pady=8)
        items = [
            ("Home", self.show_home),
            ("Fact Book", self.show_fact_book),
            ("Map", self.show_map),
            ("Food Web", self.show_food_web),
            ("Conservation", self.show_conservation),
            ("Quiz", self.show_quiz),
            ("Word Search", self.show_word_search),
            ("Matching", self.show_matching),
            ("Color Lab", self.show_coloring),
            ("Rescue Game", self.show_arcade),
        ]
        for text, cmd in items:
            tk.Button(
                bar, text=text, command=cmd, width=12,
                font=("Arial", 10, "bold"), bg="white", fg=DARK
            ).pack(side="left", padx=4)

    def title(self, text, sub=None):
        tk.Label(self.main, text=text, font=("Arial", 24, "bold"), fg=DARK, bg=BG).pack(pady=(8, 2))
        if sub:
            tk.Label(self.main, text=sub, font=("Arial", 12), fg="#2d5e77", bg=BG, wraplength=1050).pack()

    def info_card_in(self, parent, title, text):
        frame = tk.LabelFrame(parent, text=title, font=("Arial", 12, "bold"), bg="white", padx=12, pady=10)
        frame.pack(fill="x", padx=18, pady=7)
        tk.Label(frame, text=text, bg="white", justify="left", anchor="w", wraplength=1030, font=("Arial", 12)).pack(fill="x")

    def make_scroll_area(self):
        outer = tk.Frame(self.main, bg=BG)
        outer.pack(fill="both", expand=True)

        canvas = tk.Canvas(outer, bg=BG, highlightthickness=0)
        scrollbar = tk.Scrollbar(outer, orient="vertical", command=canvas.yview)
        content = tk.Frame(canvas, bg=BG)

        content.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=content, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))
        return content

    def draw_axolotl(self, parent):
        c = tk.Canvas(parent, width=620, height=260, bg="white", highlightthickness=2, highlightbackground="#75b8d3")
        c.pack(pady=10)

        for _ in range(12):
            x = random.randint(20, 600)
            y = random.randint(20, 230)
            r = random.randint(4, 9)
            c.create_oval(x-r, y-r, x+r, y+r, outline="#b3e8fb")

        c.create_oval(220, 100, 430, 180, fill=PINK, outline="#8b5b76", width=3)
        c.create_polygon(400, 114, 540, 80, 540, 202, 400, 165, fill=PINK, outline="#8b5b76", width=3)
        c.create_oval(145, 90, 250, 190, fill=PINK, outline="#8b5b76", width=3)

        c.create_oval(178, 126, 188, 136, fill="black")
        c.create_oval(212, 126, 222, 136, fill="black")
        c.create_arc(182, 140, 214, 155, start=180, extent=180, style="arc", width=2)

        for x in [150, 163, 176]:
            c.create_line(x, 105, x-35, 75, fill="#ff5f9a", width=4)
            c.create_line(x, 174, x-35, 205, fill="#ff5f9a", width=4)
        for x in [220, 233, 246]:
            c.create_line(x, 105, x+35, 75, fill="#ff5f9a", width=4)
            c.create_line(x, 174, x+35, 205, fill="#ff5f9a", width=4)

        for x1, y1, x2, y2 in [(275, 176, 255, 225), (315, 176, 300, 225), (370, 176, 355, 225), (405, 176, 425, 225)]:
            c.create_line(x1, y1, x2, y2, width=5, fill="#8b5b76")

        c.create_text(310, 235, text="Flat head • Long tail • External gills • Four limbs", font=("Arial", 12, "bold"), fill=DARK)

    def show_home(self):
        self.clear()
        self.nav()
        self.title("Save the Axolotl!", "Explore the facts, finish activities, and learn how conservation protects this critically endangered amphibian.")

        center = tk.Frame(self.main, bg=BG)
        center.pack(pady=12)

        left = tk.Frame(center, bg=BG)
        left.pack(side="left", padx=20)
        right = tk.Frame(center, bg=BG)
        right.pack(side="left", padx=20)

        self.draw_axolotl(left)

        guide = tk.LabelFrame(right, text="Mission Guide", font=("Arial", 14, "bold"), bg="white", padx=15, pady=15)
        guide.pack(pady=10)
        tk.Label(
            guide,
            text=(
                "Your mission:\n\n"
                "• Learn species facts\n"
                "• View the real map\n"
                "• Understand the food web\n"
                "• Study conservation threats\n"
                "• Complete activities\n"
                "• Play the rescue mini-game\n\n"
                "Activities:\n"
                "1. Quiz\n"
                "2. Word Search\n"
                "3. Matching\n"
                "4. Color Lab\n"
                "5. Rescue Game"
            ),
            bg="white", justify="left", font=("Arial", 13), wraplength=380
        ).pack()

        fast = tk.LabelFrame(right, text="Fast Facts", font=("Arial", 14, "bold"), bg="white", padx=15, pady=15)
        fast.pack(pady=10)
        tk.Label(
            fast,
            text=(
                f"Common name: {SPECIES['common_name']}\n"
                f"Scientific name: {SPECIES['scientific_name']}\n"
                f"Group: {SPECIES['group']}\n"
                f"Status: {SPECIES['status']}\n"
                f"Biome: {SPECIES['biome']}"
            ),
            bg="white", justify="left", font=("Arial", 13)
        ).pack()

    def show_fact_book(self):
        self.clear()
        self.nav()
        self.title("Species Fact Book")

        content = self.make_scroll_area()
        self.info_card_in(content, "Common & Scientific Name", f"{SPECIES['common_name']} — {SPECIES['scientific_name']}")
        self.info_card_in(content, "Endangered Status", SPECIES["status"])
        self.info_card_in(content, "Class / Group", SPECIES["group"])
        self.info_card_in(content, "Physical Description / Adaptations", SPECIES["physical"])
        self.info_card_in(content, "Lifespan", SPECIES["lifespan"])
        self.info_card_in(content, "Distribution", SPECIES["distribution"])
        self.info_card_in(content, "Habitat Explanation", SPECIES["habitat"])
        self.info_card_in(content, "Biome / Ecosystem", SPECIES["biome"])
        self.info_card_in(content, "Diet", SPECIES["diet"])

        facts = "\n".join(f"{i+1}. {fact}" for i, fact in enumerate(SPECIES["interesting_facts"]))
        self.info_card_in(content, "Interesting Facts", facts)

    def show_map(self):
        self.clear()
        self.nav()
        self.title("Distribution Map")

        wrap = tk.Frame(self.main, bg=BG)
        wrap.pack(pady=10)

        map_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Axolotl Map - Mexico labeled.png")

        if os.path.exists(map_path):
            try:
                self.map_image = tk.PhotoImage(file=map_path)
                label = tk.Label(wrap, image=self.map_image, bg=BG)
                label.pack()
            except Exception:
                tk.Label(
                    wrap,
                    text="The map image file was found, but Tkinter could not open it.\nMake sure it stays as a PNG file in the same folder as the Python game.",
                    bg=BG, fg="red", font=("Arial", 13)
                ).pack()
        else:
            tk.Label(
                wrap,
                text="Map image not found.\nPut 'Axolotl Map - Mexico labeled.png' in the same folder as this Python file.",
                bg=BG, fg="red", font=("Arial", 13)
            ).pack()

        tk.Label(
            self.main,
            text=(
                "The red point marks the central Mexico region where the axolotl's native range is found.\n"
                "The species is associated with Xochimilco and historically Lake Chalco."
            ),
            bg=BG, font=("Arial", 12), wraplength=1000
        ).pack(pady=10)

    def show_food_web(self):
        self.clear()
        self.nav()
        self.title("Food Web")

        content = self.make_scroll_area()

        canvas = tk.Canvas(content, width=1080, height=560, bg="white", highlightthickness=2, highlightbackground="#75b8d3")
        canvas.pack(pady=10)

        nodes = {
            "Algae": (140, 80),
            "Aquatic Plants": (330, 80),
            "Worms": (110, 220),
            "Mollusks": (250, 220),
            "Crustaceans": (400, 220),
            "Insect Larvae": (560, 220),
            "Tadpoles": (730, 220),
            "Small Fish": (900, 220),
            "Axolotl": (500, 390),
            "Herons": (900, 80),
            "Carp": (210, 390),
            "Tilapia": (810, 390),
        }

        for name, (x, y) in nodes.items():
            fill = "#ffd7ea" if name == "Axolotl" else "#dff4d6"
            if name in ("Carp", "Tilapia"):
                fill = "#ffe2bf"
            if name == "Herons":
                fill = "#e1e3ff"
            canvas.create_rectangle(x-70, y-22, x+70, y+22, fill=fill, outline="#333333", width=2)
            canvas.create_text(x, y, text=name, font=("Arial", 11, "bold"))

        arrows = [
            ("Algae", "Mollusks"),
            ("Aquatic Plants", "Mollusks"),
            ("Aquatic Plants", "Crustaceans"),
            ("Worms", "Axolotl"),
            ("Mollusks", "Axolotl"),
            ("Crustaceans", "Axolotl"),
            ("Insect Larvae", "Axolotl"),
            ("Tadpoles", "Axolotl"),
            ("Small Fish", "Axolotl"),
            ("Axolotl", "Herons"),
            ("Worms", "Carp"),
            ("Insect Larvae", "Tilapia"),
            ("Crustaceans", "Tilapia"),
            ("Small Fish", "Tilapia"),
        ]

        for a, b in arrows:
            x1, y1 = nodes[a]
            x2, y2 = nodes[b]
            canvas.create_line(x1, y1+24, x2, y2-24, arrow=tk.LAST, width=2, fill="#2c6c91")

        self.info_card_in(content, "If Axolotls Went Extinct", SPECIES["extinction_effect"])
        self.info_card_in(content, "Invasive Species and the Food Web", SPECIES["invasive"])

    def show_conservation(self):
        self.clear()
        self.nav()
        self.title("Conservation & Environmental Importance")

        content = self.make_scroll_area()
        self.info_card_in(content, "Why It Is Endangered", SPECIES["endangered_causes"])
        self.info_card_in(content, "Legislation and How It Prevents Extinction", SPECIES["legislation"])
        self.info_card_in(content, "r vs K species", SPECIES["kr"])
        self.info_card_in(content, "Conservation Group and What It Does", SPECIES["conservation_group"])
        self.info_card_in(content, "Global Warming Effects", SPECIES["global_warming"])

    def show_quiz(self):
        self.clear()
        self.nav()
        self.title("Quiz")

        self.quiz_index = 0
        self.quiz_score = 0
        self.quiz_frame = tk.Frame(self.main, bg=BG)
        self.quiz_frame.pack(fill="both", expand=True)
        self.load_quiz()

    def load_quiz(self):
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        if self.quiz_index >= len(QUIZ):
            earned = self.quiz_score * 10
            self.add_score(earned)
            tk.Label(
                self.quiz_frame, text=f"Quiz complete! {self.quiz_score}/{len(QUIZ)} correct",
                font=("Arial", 24, "bold"), bg=BG, fg=DARK
            ).pack(pady=30)
            tk.Label(
                self.quiz_frame, text=f"You earned {earned} points.",
                font=("Arial", 16), bg=BG
            ).pack()
            tk.Button(
                self.quiz_frame, text="Play Quiz Again", command=self.show_quiz,
                font=("Arial", 12, "bold")
            ).pack(pady=12)
            return

        q, choices, answer = QUIZ[self.quiz_index]
        tk.Label(self.quiz_frame, text=f"Question {self.quiz_index + 1}", font=("Arial", 20, "bold"), bg=BG, fg=DARK).pack(pady=(20, 8))
        tk.Label(self.quiz_frame, text=q, font=("Arial", 16), bg=BG, wraplength=900).pack(pady=10)

        options = choices[:]
        random.shuffle(options)
        for choice in options:
            tk.Button(
                self.quiz_frame, text=choice, width=36, font=("Arial", 12),
                command=lambda c=choice, a=answer: self.check_quiz(c, a)
            ).pack(pady=6)

    def check_quiz(self, choice, answer):
        if choice == answer:
            self.quiz_score += 1
            messagebox.showinfo("Correct", "Nice work!")
        else:
            messagebox.showerror("Incorrect", f"The correct answer was: {answer}")
        self.quiz_index += 1
        self.load_quiz()

    def show_word_search(self):
        self.clear()
        self.nav()
        self.title("Word Search")

        tk.Label(self.main, text="Word Bank: " + ", ".join(WORD_BANK), bg=BG, font=("Arial", 12, "bold"), wraplength=1000).pack(pady=8)
        grid = tk.Frame(self.main, bg=BG)
        grid.pack(pady=10)

        self.selected_letters = set()
        self.word_buttons = []

        for r, row in enumerate(WORD_GRID):
            b_row = []
            for c, letter in enumerate(row):
                btn = tk.Button(
                    grid, text=letter, width=3, font=("Consolas", 14, "bold"),
                    command=lambda rr=r, cc=c: self.toggle_letter(rr, cc)
                )
                btn.grid(row=r, column=c, padx=1, pady=1)
                b_row.append(btn)
            self.word_buttons.append(b_row)

        tk.Button(self.main, text="Claim 20 Points", font=("Arial", 12, "bold"), command=self.claim_word_search).pack(pady=10)

    def toggle_letter(self, r, c):
        if (r, c) in self.selected_letters:
            self.selected_letters.remove((r, c))
            self.word_buttons[r][c].configure(bg="SystemButtonFace")
        else:
            self.selected_letters.add((r, c))
            self.word_buttons[r][c].configure(bg="#fff28b")

    def claim_word_search(self):
        self.add_score(20)
        messagebox.showinfo("Word Search", "You completed the word search activity and earned 20 points.")

    def show_matching(self):
        self.clear()
        self.nav()
        self.title("Matching Game")

        left = list(MATCH_TERMS.keys())
        right = list(MATCH_TERMS.values())
        random.shuffle(right)

        self.match_left = left
        self.match_right = right
        self.match_entries = []

        board = tk.Frame(self.main, bg=BG)
        board.pack(pady=10)

        left_box = tk.LabelFrame(board, text="Terms", font=("Arial", 12, "bold"), bg="white", padx=12, pady=12)
        right_box = tk.LabelFrame(board, text="Meanings", font=("Arial", 12, "bold"), bg="white", padx=12, pady=12)
        left_box.pack(side="left", padx=20)
        right_box.pack(side="left", padx=20)

        for i, term in enumerate(left, start=1):
            row = tk.Frame(left_box, bg="white")
            row.pack(anchor="w", pady=5)
            tk.Label(row, text=f"{i}. {term}", bg="white", width=30, anchor="w", font=("Arial", 12)).pack(side="left")
            entry = tk.Entry(row, width=5, font=("Arial", 12))
            entry.pack(side="left")
            self.match_entries.append(entry)

        for i, meaning in enumerate(right):
            letter = chr(ord("A") + i)
            tk.Label(right_box, text=f"{letter}. {meaning}", bg="white", wraplength=400, justify="left", font=("Arial", 12)).pack(anchor="w", pady=5)

        tk.Button(self.main, text="Check Answers", font=("Arial", 12, "bold"), command=self.check_matching).pack(pady=12)

    def check_matching(self):
        lookup = {chr(ord("A") + i): meaning for i, meaning in enumerate(self.match_right)}
        correct = 0
        for i, term in enumerate(self.match_left):
            letter = self.match_entries[i].get().strip().upper()
            if letter in lookup and lookup[letter] == MATCH_TERMS[term]:
                correct += 1

        earned = correct * 8
        self.add_score(earned)
        messagebox.showinfo("Matching Results", f"You got {correct}/{len(self.match_left)} correct.\nYou earned {earned} points.")

    def show_coloring(self):
        self.clear()
        self.nav()
        self.title("Color Lab", "Recolor the axolotl and make your own version.")

        self.color_canvas = tk.Canvas(self.main, width=760, height=460, bg="white", highlightthickness=2, highlightbackground="#75b8d3")
        self.color_canvas.pack(pady=10)

        self.head = self.color_canvas.create_oval(120, 150, 240, 280, fill=PINK, outline="#8b5b76", width=3)
        self.body = self.color_canvas.create_oval(220, 160, 520, 280, fill=PINK, outline="#8b5b76", width=3)
        self.tail = self.color_canvas.create_polygon(500, 175, 650, 130, 650, 315, 500, 265, fill=PINK, outline="#8b5b76", width=3)

        self.color_canvas.create_oval(155, 205, 166, 216, fill="black")
        self.color_canvas.create_oval(190, 205, 201, 216, fill="black")

        for x in [125, 140, 155]:
            self.color_canvas.create_line(x, 175, x-40, 135, fill="#ff5c99", width=4)
            self.color_canvas.create_line(x, 255, x-40, 295, fill="#ff5c99", width=4)
        for x in [205, 220, 235]:
            self.color_canvas.create_line(x, 175, x+40, 135, fill="#ff5c99", width=4)
            self.color_canvas.create_line(x, 255, x+40, 295, fill="#ff5c99", width=4)

        for x1, y1, x2, y2 in [(290, 280, 260, 355), (350, 280, 330, 355), (430, 280, 410, 355), (485, 280, 510, 355)]:
            self.color_canvas.create_line(x1, y1, x2, y2, fill="#8b5b76", width=5)

        controls = tk.Frame(self.main, bg=BG)
        controls.pack()
        for name, color in [("Pink", "#f6b5d7"), ("Gold", "#f2cf63"), ("White", "#f7f7f7"), ("Brown", "#bf8d5a"), ("Black", "#525252"), ("Blue", "#9fc8ff")]:
            tk.Button(controls, text=name, width=10, command=lambda c=color: self.recolor(c)).pack(side="left", padx=4)

        tk.Button(controls, text="Earn 15 Points", width=14, command=self.finish_coloring).pack(side="left", padx=8)

    def recolor(self, color):
        self.color_canvas.itemconfig(self.head, fill=color)
        self.color_canvas.itemconfig(self.body, fill=color)
        self.color_canvas.itemconfig(self.tail, fill=color)

    def finish_coloring(self):
        self.add_score(15)
        messagebox.showinfo("Color Lab", "You completed the coloring activity and earned 15 points.")

    def show_arcade(self):
        self.clear()
        self.nav()
        self.title("Rescue Game", "Use arrow keys. Collect food and avoid trash and invasive fish.")

        self.arcade_info = tk.Label(self.main, text="Food: 0   Trash hits: 0   Fish hits: 0", font=("Arial", 14, "bold"), bg=BG, fg=DARK)
        self.arcade_info.pack(pady=4)

        self.arcade = tk.Canvas(self.main, width=1000, height=560, bg="#bdefff", highlightthickness=2, highlightbackground="#75b8d3")
        self.arcade.pack(pady=10)

        self.arcade.create_rectangle(0, 420, 1000, 560, fill=GREEN, outline="")
        for i in range(12):
            x = 40 + i * 80
            self.arcade.create_rectangle(x, 430, x + 30, 560, fill="#6ea857", outline="")

        for _ in range(25):
            x = random.randint(20, 980)
            y = random.randint(20, 520)
            r = random.randint(4, 9)
            self.arcade.create_oval(x-r, y-r, x+r, y+r, outline="#e7fbff")

        self.player = self.arcade.create_oval(120, 240, 180, 280, fill=PINK, outline="#7d4d69", width=2)
        self.arcade.create_oval(135, 252, 143, 260, fill="black")
        self.arcade.create_oval(157, 252, 165, 260, fill="black")

        self.arcade_items = []
        self.arcade_food = 0
        self.arcade_trash = 0
        self.arcade_fish = 0
        self.arcade_running = True

        self.root.bind("<Left>", lambda e: self.move_player(-20, 0))
        self.root.bind("<Right>", lambda e: self.move_player(20, 0))
        self.root.bind("<Up>", lambda e: self.move_player(0, -20))
        self.root.bind("<Down>", lambda e: self.move_player(0, 20))

        btns = tk.Frame(self.main, bg=BG)
        btns.pack()
        tk.Button(btns, text="Start / Restart", font=("Arial", 12, "bold"), command=self.show_arcade).pack(side="left", padx=5)
        tk.Button(btns, text="Stop Round", font=("Arial", 12, "bold"), command=self.stop_arcade).pack(side="left", padx=5)

        self.spawn_loop()
        self.update_arcade()

    def move_player(self, dx, dy):
        if not self.arcade_running or self.player is None:
            return
        x1, y1, x2, y2 = self.arcade.coords(self.player)
        nx1, ny1, nx2, ny2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
        if 0 <= nx1 and nx2 <= 1000 and 0 <= ny1 and ny2 <= 560:
            self.arcade.move(self.player, dx, dy)

    def spawn_loop(self):
        if not self.arcade_running:
            return

        x = 1020
        y = random.randint(50, 390)
        roll = random.random()

        if roll < 0.45:
            item = self.arcade.create_oval(x-12, y-12, x+12, y+12, fill="#7b4a1e", outline="#3f250e")
            kind = "food"
        elif roll < 0.72:
            item = self.arcade.create_rectangle(x-12, y-12, x+12, y+12, fill="#999999", outline="#555555")
            kind = "trash"
        else:
            item = self.arcade.create_polygon(x-25, y, x, y-12, x+20, y, x, y+12, fill="#e2912b", outline="#7a4705")
            kind = "fish"

        self.arcade_items.append((item, kind))
        self.root.after(850, self.spawn_loop)

    def overlaps(self, a, b):
        ax1, ay1, ax2, ay2 = self.arcade.bbox(a)
        bx1, by1, bx2, by2 = self.arcade.bbox(b)
        return not (ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2)

    def update_arcade(self):
        if not hasattr(self, "arcade"):
            return

        if self.arcade_running:
            to_remove = []

            for item, kind in self.arcade_items:
                self.arcade.move(item, -12, 0)
                bbox = self.arcade.bbox(item)
                if not bbox:
                    to_remove.append((item, kind))
                    continue
                if bbox[2] < 0:
                    to_remove.append((item, kind))
                    continue

                if self.player is not None and self.overlaps(item, self.player):
                    if kind == "food":
                        self.arcade_food += 1
                    elif kind == "trash":
                        self.arcade_trash += 1
                    else:
                        self.arcade_fish += 1
                    to_remove.append((item, kind))

            for item, kind in to_remove:
                try:
                    self.arcade.delete(item)
                except Exception:
                    pass
                if (item, kind) in self.arcade_items:
                    self.arcade_items.remove((item, kind))

            self.arcade_info.config(text=f"Food: {self.arcade_food}   Trash hits: {self.arcade_trash}   Fish hits: {self.arcade_fish}")

        self.root.after(60, self.update_arcade)

    def stop_arcade(self):
        self.arcade_running = False
        earned = max(0, self.arcade_food * 6 - self.arcade_trash * 4 - self.arcade_fish * 5)
        self.add_score(earned)
        messagebox.showinfo(
            "Round Over",
            f"Food collected: {self.arcade_food}\nTrash hits: {self.arcade_trash}\nFish hits: {self.arcade_fish}\nPoints earned: {earned}"
        )


def main():
    root = tk.Tk()
    app = AxolotlGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
