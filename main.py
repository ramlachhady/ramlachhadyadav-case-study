from agents.ticket_classifier import Ticket, ticket_classifier
from agents.ticket_router import RoutingInput, route_ticket

# 👋 Ask user for ticket input
print("📝 Enter support ticket details:")

ticket = Ticket(
    ticket_id=input("Ticket ID: "),
    customer_tier=input("Customer Tier (free/premium/enterprise): "),
    subject=input("Subject: "),
    message=input("Message: "),
    previous_tickets=int(input("Number of previous tickets: ")),
    monthly_revenue=int(input("Monthly revenue (in ₹ or $): ")),
    account_age_days=int(input("Account age (in days): "))
)

# 🧠 Step 1: Classification
classification = ticket_classifier(ticket)

# 📦 Step 2: Routing
routing_input = RoutingInput(
    priority_label=classification.priority_label,
    customer_tier=ticket.customer_tier,
    monthly_revenue=ticket.monthly_revenue
)
routing_result = route_ticket(routing_input)

# 📊 Final output
print("\n📩 Ticket Analysis Result:")
print("🏷️ Priority Label:", classification.priority_label)
print("📝 Explanation:", classification.explanation)
print("📦 Routed To:", routing_result.department)
print("📋 Routing Reason:", routing_result.reason)
