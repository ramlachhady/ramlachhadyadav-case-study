from pydantic import BaseModel

# ✅ Input schema for the router agent
class RoutingInput(BaseModel):
    priority_label: str
    customer_tier: str
    monthly_revenue: int

# ✅ Output schema
class RoutingDecision(BaseModel):
    department: str
    reason: str

# ✅ Agent logic
def route_ticket(data: RoutingInput) -> RoutingDecision:
    # Simple rules (you can improve these later)
    if data.priority_label.lower() in ["urgent", "high", "high priority"]:
        if data.customer_tier.lower() in ["premium", "enterprise"] or data.monthly_revenue > 5000:
            return RoutingDecision(
                department="priority-support",
                reason="High-priority customer with elevated tier or revenue"
            )
        else:
            return RoutingDecision(
                department="fast-track",
                reason="High-priority issue from a regular customer"
            )
    
    if data.priority_label.lower() in ["normal"]:
        return RoutingDecision(
            department="standard-support",
            reason="Normal issue with no urgency or critical value"
        )
    
    return RoutingDecision(
        department="low-priority",
        reason="Low urgency and low value — can be queued"
    )
