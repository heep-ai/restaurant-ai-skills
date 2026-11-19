# Example: invite former regulars back

All records are fictional. As of 19 November 2026, the owner chooses this rule:
at least 90 days since the last attended visit, permission for this restaurant's
email marketing, no upcoming active booking, and no campaign in the last 30 days.
The owner has confirmed that a new autumn menu is available. No discount is
approved. Replies to the restaurant's email are monitored for booking requests
and opt-outs. All guests below prefer French; no unresolved complaints are known.

| Guest | Days since visit | Email marketing permission | Upcoming booking | Days since campaign |
| --- | ---: | --- | --- | ---: |
| G01 | 120 | Yes | No | 45 |
| G02 | 180 | Opted out | No | 80 |
| G03 | 95 | Unknown | No | 60 |
| G04 | 100 | Yes | Yes | 50 |
| G05 | 15 | Yes | No | 45 |
| G06 | 140 | Yes | No | 7 |
| G07 | 200 | Yes | No | 100 |
| G01 | 120 | Yes | No | 45 |

The second G01 is an exact duplicate, not a new guest.

## Expected audience

8 rows → **7 unique guests** → **2 eligible** (G01, G07), **1 awaiting permission
verification** (G03), **4 excluded** (G02 opted out, G04 already booked, G05 recent
visitor, G06 recently contacted). The sum of the final groups is 7.

Unknown permission must not silently become permission. No recipient list should
include G03 until the gap is resolved.

## Draft email

Subject: La carte d'automne vous attend

> Bonjour,
>
> Notre nouvelle carte d'automne est arrivée. Ce serait un plaisir de vous
> retrouver à table ! Pour préparer votre prochaine visite, répondez à ce
> message avec la date et le nombre de personnes souhaités ; notre équipe
> vérifiera les disponibilités.
>
> Vous préférez ne plus recevoir nos nouvelles ? Dites-le-nous simplement en
> réponse à cet e-mail.

This is a draft; nothing has been scheduled or sent. No return bookings or
incremental revenue are known.
