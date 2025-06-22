# 🧠 System Design – Customer Support Ticket Analyzer

This multi-agent system consists of two core components:

---

## 1. Ticket Classifier Agent

- **Input:** A customer support ticket
- **Output:** `priority_label` and `explanation`
- **How it works:** 
  - Uses a local Phi-3 model via Ollama
  - Prompt instructs it to classify based on tone, urgency, and customer tier

---

## 2. Ticket Router Agent

- **Input:** `priority_label`, `monthly_revenue`, and `customer_tier`
- **Output:** Routing department and justification
- **Logic:**
  - VIP or Pro + High Priority → `priority-support`
  - All else → `low-priority`

---

## Flow Diagram (Textual)

```
User Input ➝ Ticket ➝ [Classifier Agent] ➝ Label + Reason
                                    |
                                    ▼
                           [Router Agent] ➝ Department + Justification
```

All results are printed to CLI for validation and testing.