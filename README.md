# Class Timetabling with a Genetic Algorithm

> **AI 201 – Final Mini‑Project**\

This repository contains a complete, self‑contained implementation of a **genetic‑algorithm solver for the university class‑timetabling problem**.\
Given a set of courses, rooms, professors, and constraints, the algorithm evolves a population of candidate schedules until it finds one that satisfies *all* hard constraints and minimises soft‑constraint violations.  The code base produces both **JSON** and **interactive HTML** reports so you can inspect the resulting timetable immediately in a browser.

The project was originally developed as a mini‑project for the AI 201 course and is accompanied by a short research paper that explains the design choices and fitness formulation.

---

## ✨ Key Features

- **Custom chromosome design** – every individual represents an entire weekly schedule.
- **Constraint‑aware crossover & mutation** operators keep the search space feasible.
- **Multi‑criteria fitness** with seven configurable criteria (room clashes, room type, professor overlaps, student overlaps, lunch break, capacity, and preferred times).
- **Parameterisable GA** – population size, generations, elitism, mutation rate, etc. are all easy to tune in `Configuration.py`.
- **Instant visualisation** – `HtmlOutput.py` turns the best chromosome into a colour‑coded, tooltip‑rich HTML timetable.
- **Headless console runner** – `GA_ConsoleApp2.py` lets you launch long experiments from the command line or a batch script.
- **Lightweight dependencies** – just `numpy` and `joblib`; everything else is Python ≥ 3.9 standard library.

---

## 🚀 Quick Start

```bash
# 1. Grab the repo
git clone https://github.com/<your‑username>/timetabling_ga.git
cd timetabling_ga

# 2. (Recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 3. Install the minimal requirements
pip install numpy joblib

# 4. Run the solver on the sample data set
python GA_ConsoleApp2.py GaSchedule.json
```

The script will log the generation‑by‑generation progress and, on completion, drop an HTML file (e.g. `output/GaSchedule_latest.html`). Open it in any modern browser to explore the schedule.

---

## 📁 Repository Layout

```text
timetabling_ga/
├── algorithm/
│   └── GeneticAlgorithm.py        ← core GA logic
├── model/                         ← domain entities & constraints
│   ├── Course.py
│   ├── Room.py
│   └── …
├── GA_ConsoleApp2.py              ← CLI entry‑point
├── HtmlOutput.py                  ← HTML report generator
├── GaSchedule.json                ← sample instance
├── output/                        ← generated timetables
└── AI_201_Final_Mini_Project_Paper.pdf
```

---

## 🛠 Tuning the Algorithm

Open `model/Configuration.py` and adjust:

| Setting           | Description                                | Typical value |
| ----------------- | ------------------------------------------ | ------------- |
| `POPULATION_SIZE` | number of chromosomes per generation       | 100 – 500     |
| `MAX_GENERATIONS` | hard stop if no perfect timetable is found | 1000          |
| `MUTATION_RATE`   | probability of a gene mutation             | 0.05          |
| `ELITISM`         | number of top individuals copied unchanged | 2             |

Re‑run `GA_ConsoleApp2.py` after every change to see the effect.

---

## 📝 Paper

If you want the full theoretical background, read [`AI_201_Final_Mini_Project_Paper.pdf`](AI_201_Final_Mini_Project_Paper.pdf).\
It details the chromosome encoding, fitness formulation, and provides benchmark results.

---

## 🤝 Contributing

1. Fork the project and create your feature branch: `git checkout -b feature/my‑feature`.
2. Commit your changes with clear messages.
3. Open a Pull Request – make sure the unit tests still pass.

Bug reports and enhancement suggestions are also welcome via the **Issues** tab.

---

## 📄 License

This work is released under the **MIT License** – see the [LICENSE](LICENSE) file for details.

