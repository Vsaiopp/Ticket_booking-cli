# 🎟️ Ticket Booking CLI

A simple, interactive **command-line ticket booking system** built using Python. It handles seat availability, pricing (including tax), and wallet-based payments — all from the terminal.

---

## 🚀 Features

- ✅ Real-time seat availability
- 💰 Wallet system with balance checks
- 🧾 Tax calculation based on subtotal
- 🔁 Input validation and user-friendly flow
- ❌ Cancel and refund seat selection
- 📦 Modular functions (easy to maintain)

---

## 🖥️ Preview

```bash
==================================================================
        🪑 Seats Available: 120                    
         💰 Wallet Balance: ₹0.00                        
==================================================================
Enter number of seats to book (or 0 to quit): 2
You have selected 2 seat(s).

To confirm the selection, press (y) or press (q) to quit: y
--------------------------------------------------------------------
Subtotal        : ₹40.00
Tax @12%        : ₹4.80
Total to Pay    : ₹44.80
--------------------------------------------------------------------
❌ Not enough money in wallet. Balance: ₹0.00, Required: ₹44.80

1. Add money
2. Show wallet balance
3. Cancel booking
