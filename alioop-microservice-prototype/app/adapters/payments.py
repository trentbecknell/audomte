from typing import Optional

def resolve_payment_link(payment_pref: str, payment_custom_url: Optional[str]) -> Optional[str]:
    if payment_pref == "Custom":
        return payment_custom_url
    if payment_pref == "Stripe":
        return "https://pay.stripe.com/example-link"
    if payment_pref == "PayPal":
        return "https://paypal.me/example-studio"
    if payment_pref == "Zelle":
        return "zelle://pay/your-handle"
    return None
