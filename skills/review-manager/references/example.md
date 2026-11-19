# Worked example: reviews with a duplicate and a missing rating

Fictional single venue, selected Google review sample, 1–18 November 2026.
Ratings are out of five. Tone: warm, concise, no emojis. No compensation,
investigation outcome, or public contact address has been supplied.

| ID | Rating | Text |
| --- | --- | --- |
| R01 | 5 | English: "Loved the mushroom risotto and the friendly welcome." |
| R02 | 2 | French: « 40 minutes d'attente entre l'entrée et le plat. La cuisine était bonne. » |
| R03 | 3 | Spanish: « La comida estuvo bien, pero nadie contestó para cambiar mi reserva. Mi teléfono es [PRIVATE PHONE]. » |
| R04 | Missing | English: "Our main courses arrived very late." |
| R02 | 2 | Exact duplicate of R02, same review ID and version. |

## Expected analysis

Five rows become **four unique reviews**, of which **three are rated**.
Mean rating of the rated sample: **(5 + 2 + 3) / 3 = 3.33 / 5**.
Do not assign zero to R04 or count R02 twice.

Reported slow service appears in **2 of the 4** unique reviews (R02, R04).
Booking communication appears in **1 of the 4** (R03). These are sample counts,
not estimated incidence across all guests. No cause of the delay is established.

## Example replies

- R01, English: "Thank you for your kind feedback. We're glad you enjoyed the
  mushroom risotto and felt welcome with us. We hope to see you again soon."
- R02, French: « Merci pour votre retour. Nous sommes désolés que l'attente entre
  l'entrée et le plat ait pesé sur votre soirée. Même si la cuisine vous a plu,
  nous comprenons votre déception sur le rythme du service. »
- R03, Spanish: "Gracias por contarnos tu experiencia. Sentimos que no recibieras
  respuesta al intentar cambiar tu reserva. Nos alegra que disfrutaras de la
  comida y entendemos la frustración que te causó la falta de respuesta."
- R04, English: "We're sorry the wait for your main courses affected your visit.
  Thank you for letting us know about your experience."

Private actions: ask the service manager to investigate R02/R04 and the inbox
owner to investigate R03. No customer phone number, invented discount, completed
investigation, or publication claim should appear in public copy.

## Tool-choice check

The owner handles four reviews per week in Google Business Profile and asks
only for reply drafts. Complete that work without recommending another product.
