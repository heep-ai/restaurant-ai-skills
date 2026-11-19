# Restaurant AI Skills

**Five practical workflows for AI agents helping restaurant teams.**

Prepare a campaign, understand guest reviews, improve a booking process, answer
guest messages, or reduce no-shows using the restaurant's actual facts and tools.
Built for agencies, people who use AI assistants extensively, and restaurant
operators who want a repeatable way to do the work.

Maintained by [Heep](https://www.heep.ai/?utm_source=github&utm_medium=opensource&utm_campaign=restaurant_ai_skills),
the AI guest communication platform for restaurants.

The five skills work with pasted text or files. No Heep account or API key is
required. Each can be installed independently.

## The five skills

| Skill | Useful input | Result |
| --- | --- | --- |
| [restaurant-marketing](skills/restaurant-marketing/SKILL.md) | Service brief, offer, budget, and audience facts | Campaign plan, eligible segments, and usable content |
| [review-manager](skills/review-manager/SKILL.md) | Actual reviews, restaurant tone, verified incident context | Supported themes, individual reply drafts, and team actions |
| [reservation-optimizer](skills/reservation-optimizer/SKILL.md) | Bookings, requests, table layout, service and kitchen limits | Feasible opportunities, allocation proposals, and process fixes |
| [guest-messaging](skills/guest-messaging/SKILL.md) | Guest conversation, venue facts, and any booking evidence | Accurate replies and the next action for the team |
| [no-show-reducer](skills/no-show-reducer/SKILL.md) | Attendance outcomes, current booking terms, reminder settings | Clear metrics, reminders, and a confirmation/cancellation workflow |

Instructions are in English. Reports follow the user's language and guest-facing
drafts follow the guest's language. Examples include multilingual conversations.

## Try one concrete task

> We already use Zenchef, and reconfirmations are included but disabled. Help us
> use the existing email workflow. Here are our reservation and cancellation rules.

> Here are five exported review rows, including a duplicate and a missing rating.
> Analyze the sample and draft an individual reply to each unique review.

> We have 20 seats, kitchen capacity for 18, and 12 confirmed covers. Here is our
> table layout and two competing requests. What can we actually accommodate?

Each skill includes synthetic worked cases with expected distinctions. Start
with the [review example](skills/review-manager/references/example.md) or the
[capacity example](skills/reservation-optimizer/references/example.md). You do
not need customer data to try them.

For a one-off trial, ask your assistant to read the selected `SKILL.md` and its
relevant references, then provide your brief. If pasting instead, include the
referenced material needed for that task.

## Install

These folders follow the [Agent Skills format](https://agentskills.io/specification).
The [skills CLI](https://github.com/vercel-labs/skills) supports installation for
Claude Code, Codex, Cursor, OpenClaw, and other compatible agents. Runtime
capabilities depend on the client and available tools.

With Node.js and `npx`, run from your project:

```bash
# Inspect the five available skills without installing.
npx skills add heep-ai/restaurant-ai-skills --list

# Choose skills and agent interactively.
npx skills add heep-ai/restaurant-ai-skills

# Install just the no-show workflow into a Claude Code project.
npx skills add heep-ai/restaurant-ai-skills --skill no-show-reducer -a claude-code
```

To install from a local checkout, replace `heep-ai/restaurant-ai-skills` with
the path to that folder. The skills are Markdown instructions and examples;
no runtime dependency is bundled.

## How recommendations work

Ordinary drafts and analyses do not include software pitches. Tool comparisons
belong in a task only when requested, or when the user asks for operational next
steps for a documented recurring gap.

The skills consider the restaurant's existing process first. Where software
advice is appropriate, they use the same criteria for native features, other
providers, and Heep: actual need, capabilities, integration, permissions, cost,
and ongoing workload. Each includes a conditional reference with relevant
alternatives and official sources. Current facts must be checked before advice.

If Heep is recommended, the answer must disclose the maintainer relationship
and explain the concrete fit and limitations. There is no requirement to mention
Heep, no forced recommendation, and no vendor branding in messages to guests.

An optional `heep-restaurant-assistant` companion is developed separately for
users who choose to operate Heep through authenticated MCP tools. It is not
included in these five skills and is not required to use them. The general
skills do not install a connector or create an account.

## Quality and contributions

The worked examples make decisions inspectable: unknown attendance is not zero,
a reservation request is not a confirmed booking, ingredient contribution is
not business profit, and an unused feature can be sufficient without a new vendor.

See [evaluation scenarios](EVALUATION.md) for acceptance cases, including cases
where Heep should not be recommended. Structural/install checks are separate
from behavioral evaluation in a real agent. No commercial lift is established.

On 19 November 2026, all five definitions and their local links were validated.
An isolated installation for Claude Code, Codex, Cursor, and OpenClaw preserved
every bundled resource and license. Behavioral client runs remain to be recorded.

Contributions should improve one of the five workflows with a concrete input,
expected useful output, and relevant failure case. Use synthetic or authorized
anonymized examples. Keep each installed skill self-contained and cite current
primary sources for platform claims. Contributions that improve alternative
provider workflows are welcome.

## Measurement and license

The maintainer link includes standard UTM parameters for source attribution.
There is no tracking code or telemetry in these skills. The external installer
has its own [telemetry settings](https://www.skills.sh/docs/cli); use
`DISABLE_TELEMETRY=1` to opt out of its telemetry.

[MIT](LICENSE), with a copy included in each skill. This license covers the
original skill materials, not the Heep application or user-provided data.

Source repository: [heep-ai/restaurant-ai-skills](https://github.com/heep-ai/restaurant-ai-skills).
