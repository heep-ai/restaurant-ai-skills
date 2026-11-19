# Example: reminders without invented penalties

Fictional owner brief: Paris, November 2026. The past-period export contains
100 bookings whose scheduled visit is before the observation cutoff:
80 attended, 10 marked no-show, 8 cancelled, and 2 with unknown attendance.
These are booking counts, not covers.

Current accepted policy: no deposit or cancellation fee. Guests may request a
change or cancellation by replying; the team applies it in the booking system.
The owner wants a reminder the day before, during daytime hours. There is no
policy allowing cancellation just because a guest does not answer.

## Expected diagnosis

Resolved non-cancelled bookings: **80 + 10 = 90**.
No-show rate on that denominator: **10 / 90 = 11.1%**.
Report **8 cancellations** and **2 unknown outcomes** separately. A rate of
10/100 describes a different denominator and must not be mislabeled.

## Example reminder

For an actual booking of 4 guests on 26 November 2026 at 20:00:

> Bonjour, nous vous attendons demain, jeudi 26 novembre, à 20 h pour
> 4 personnes. Un changement de programme ? Répondez à ce message pour
> confirmer votre venue ou demander une modification ou une annulation.

## Expected state handling

| Guest response | Team action |
| --- | --- |
| Confirms attendance | Record the confirmation if the workflow supports it |
| Requests cancellation | Apply the cancellation through the authorized workflow, then acknowledge its actual result |
| Does not answer | Keep the booking; flag for follow-up under the existing policy |
| Asks to change the time | Check availability before promising the new time |

No fee, automatic cancellation, provider-approved template, or measured
no-show improvement can be claimed from these inputs.
