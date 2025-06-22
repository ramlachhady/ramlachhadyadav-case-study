import re
from pydantic import BaseModel
from local_ollama_client import query_phi3

# 🎫 Input schema
class Ticket(BaseModel):
    ticket_id: str
    customer_tier: str
    subject: str
    message: str
    previous_tickets: int
    monthly_revenue: int
    account_age_days: int

# 🏷️ Output schema
class TicketClassification(BaseModel):
    priority_label: str
    explanation: str

# 🧠 Ticket Classification Agent
def ticket_classifier(ticket: Ticket) -> TicketClassification:
    prompt = f"""
You are a support ticket classifier.

Classify the urgency of this ticket and provide a reason.

Ticket:
- ID: {ticket.ticket_id}
- Customer Tier: {ticket.customer_tier}
- Subject: {ticket.subject}
- Message: {ticket.message}
- Previous Tickets: {ticket.previous_tickets}
- Monthly Revenue: {ticket.monthly_revenue}
- Account Age (days): {ticket.account_age_days}

Respond in this format:
Label: <priority>
Reason: <why>
""".strip()

    response = query_phi3(prompt)

    # 🧾 Robust parsing with markdown cleanup and fallback
    try:
        lines = response.strip().splitlines()
        label = ""
        reason = ""

        for line in lines:
            clean_line = re.sub(r"[*_`]", "", line).strip()  # remove markdown characters
            if clean_line.lower().startswith("label:"):
                label = clean_line.split(":", 1)[1].strip()
            elif clean_line.lower().startswith("reason:"):
                reason = clean_line.split(":", 1)[1].strip()

        # Fallback detection if label still missing
        if not label:
            lowered = response.lower()
            if "urgent" in lowered or "immediate" in lowered or "frustration" in lowered:
                label = "High"
            elif "normal" in lowered:
                label = "Normal"
            elif "low" in lowered or "can be queued" in lowered:
                label = "Low"
            else:
                label = "unknown"

        if not reason:
            reason = response.strip()

    except Exception:
        label = "unknown"
        reason = response.strip()

    return TicketClassification(priority_label=label, explanation=reason)
