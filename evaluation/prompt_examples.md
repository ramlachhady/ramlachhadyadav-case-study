# 🧪 Prompt Examples – Good & Bad Model Outputs

---

## ✅ Good Example

**Prompt:**
```
Subject: Can't log in  
Message: I paid and it still won't load. Fix this now!
Tier: VIP
```

**Response:**
```
Label: High
Reason: High urgency due to access failure for paid user
```

---

## ❌ Bad Example (Missing Label)

**Prompt:**
```
Message: why is dashboard slow again??
```

**Response:**
```
This is a serious concern. Customer seems frustrated.
```

✅ **Handled by:** fallback parsing logic using regex + tone keywords

---

## Notes:
- Responses without `Label:` are handled via fallback
- Tone and tier strongly influence routing