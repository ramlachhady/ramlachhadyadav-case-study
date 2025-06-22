
# 🧠 Customer Support Ticket Analyzer & Router (Draconic Case Study – Option A)

This project is a multi-agent system built using **Python**, **Pydantic**, and a **local Phi-3 model via Ollama**. It automatically classifies and routes customer support tickets based on urgency, tone, and customer value.

---

## ✅ Project Structure

```
ramlachhadyadav-case-study/
├── main.py                     # Runs the pipeline (interactive or batch)
├── local_ollama_client.py     # Connects to local Ollama model (phi3)
├── agents/
│   ├── ticket_classifier.py   # Classifies ticket urgency
│   └── ticket_router.py       # Routes based on priority, tier, revenue
├── ai_chat_history.txt        # Full conversation log with ChatGPT
├── README.md                  # Project overview and setup
├── docs/                      # (Optional) Notes, visuals
└── evaluation/                # (Optional) Store test results
```

---

## 🧪 Agents

### 1. `ticket_classifier.py`
- Accepts a support ticket
- Uses prompt + local Phi-3 model
- Returns priority label + explanation

### 2. `ticket_router.py`
- Accepts label + tier + revenue
- Returns target department + reason

---

## 💻 How to Run

### Step 1: Install and launch Ollama
```bash
ollama run phi3
```

### Step 2: Activate environment and run main script
```bash
cd ramlachhadyadav-case-study
.env\Scriptsctivate  # On Windows
python main.py
```

You will be asked to enter ticket details.

---

## 🧠 Features

- Local LLM (phi3) integration via `ollama`
- Modular multi-agent system
- Smart fallback for classification (even if no label)
- User-friendly CLI input
- Business-driven routing logic

---

## 🧪 Evaluation Results

- ✅ Tested on 7 tickets (5 realistic + 2 edge cases)
- ✅ Classifier accuracy is strong
- ✅ Router respects customer tier, tone, and urgency
- ✅ See `main.py` for interactive or batch testing

---

## 📝 Example Run

```
Ticket ID: SUP-999
Tier: vip
Message: I paid for this and it’s stuck again!

🏷️ Priority: High
📦 Routed To: priority-support
```

---

## 🤔 What Didn’t Work & Lessons Learned

- ❌ OpenAI API failed due to quota → switched to Ollama with phi3
- ❌ pydantic-ai import bugs → bypassed by building manual prompt handler
- ⚠️ Some LLM responses missed “Label:” — added smart parsing fallback
- ⚠️ CLI formatting initially failed → resolved using Python `input()`

---

## 📬 Submission

- [x] Code: ✅ Working
- [x] Agents: ✅ Classifier & Router
- [x] Evaluation: ✅ 7 test tickets complete
- [x] Documentation: ✅ This file
- [ ] Chat log: Include `ai_chat_history.txt`
- [ ] GitHub Repo: Push public
- [ ] Email: Send final submission with link

---

## 📦 Credits

Developed by **Ramlachhad Shivmurat Yadav**  
Submitted for the **AI/ML Engineer Case Study** at **Draconic Careers**
