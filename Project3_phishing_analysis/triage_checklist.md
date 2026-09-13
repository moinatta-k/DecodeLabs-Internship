# Phishing Triage Checklist & Decision Tree

## Purpose

This is a practical tool for anyone — technical or not — to quickly judge whether an incoming email or message is safe, suspicious, or malicious, and decide what to do about it. It's built from analyzing real phishing patterns and testing the logic against sample attacks.

## The Checklist

Go through these seven questions for any message that feels off. Answer honestly with Yes or No.

1. Does the sender's email address exactly match the real organization's domain, rather than a similar-looking copy?
2. Does the message use urgency or fear (deadlines, threats, account suspension) to pressure quick action?
3. Does the message include an attachment with an unusual or risky file type (e.g. `.iso`, `.js`, `.scr`)?
4. Does the message request sensitive information (passwords, OTPs, card details) directly?
5. Does the message include a phone number urging you to call, instead of directing you through official channels?
6. Does any link contain a mismatched or suspicious domain — typos, extra words, or the real brand name buried inside a longer fake domain?
7. Does this message match how this sender/organization normally communicates with you (channel, tone, level of formality)?

Some of these questions matter more than others. A single "yes" on the wrong question can be more dangerous than several "yes" answers on minor ones — so before counting anything up, check the severity list below first.

## Severity Tiers

**Tier 1 — Any single "yes" here is enough on its own to call the message Malicious:**
- Directly asks for a password, OTP, or card details
- Has a dangerous attachment
- The link's real domain doesn't match the organization at all (not just "looks a bit off" — actually a different domain entirely)

**Tier 2 — Everything else. Count how many of the remaining questions are "yes":**
- 0 → Safe
- 1–2 → Suspicious
- 3 or more → Malicious

## Decision Tree

Incoming Suspicious Message
                          |
          Does it trigger any Tier 1 red flag?
          (direct credential request, dangerous
           attachment, or fully mismatched domain)
                 /                      \
               YES                       NO
                |                         |
          MALICIOUS                Count Tier 2 "yes" answers
          Block & Escalate                |
                               /           |           \
                              0           1-2          3+
                              |            |            |
                            SAFE      SUSPICIOUS    MALICIOUS
                            Close      Warn User   Block & Escalate

## Worked Examples

### Example 1 — Fake Netflix billing email

**Message summary:** Claims to be from Netflix, sent from `netflix-billing-support.com`. Says payment failed, threatens account suspension in 24 hours, includes a link to `netflix.com.billing-verify-secure.info/update`, gives a phone number to call, and attaches `Invoice_Details.iso`.

**Checklist results:**
- Q1 (domain match): No — sender domain is `netflix-billing-support.com`, not `netflix.com`
- Q2 (urgency/fear): Yes — 24-hour deadline, threat of suspension
- Q3 (dangerous attachment): Yes — `.iso` file
- Q4 (asks for sensitive info): Not directly, but the link leads to a fake payment form
- Q5 (phone number pressure): Yes
- Q6 (suspicious link domain): Yes — real domain is actually `billing-verify-secure.info`, with `netflix.com` used as a fake subdomain to trick the eye (read the URL right to left to find the true root)
- Q7 (matches normal communication): No — real Netflix doesn't attach files or use urgent phone numbers

**Verdict: Malicious.** This trips Tier 1 twice over (dangerous attachment, and a link that doesn't actually belong to Netflix at all) — either one alone is enough to call it malicious, and this message has both plus several Tier 2 flags on top.

### Example 2 — "Sarah Chen" internship email

**Message summary:** Claims to coordinate DecodeLabs Week 3 submissions, sent from `s.chen@decodelabs.tech`. Asks for GitHub username and registration email, includes a link to a real Google Drive file, no urgency language.

**Checklist results:**
- Q1 (domain match): Looks legitimate at first glance
- Q2 (urgency/fear): No
- Q3 (dangerous attachment): No
- Q4 (asks for sensitive info): Only low-sensitivity info (username, email) — not a password or OTP
- Q5 (phone number pressure): No
- Q6 (suspicious link): No — genuinely a real `drive.google.com` link
- Q7 (matches normal communication): No — DecodeLabs has only ever communicated through their WhatsApp group, never individual email

**Verdict: Suspicious.** No Tier 1 triggers present, and only one Tier 2 "yes" (breaks the established communication pattern). Under the model, this means: pause and verify through the known channel before responding, rather than treating it as an immediate threat.

## Why This Matters

Technical filters catch a lot of phishing automatically, but the ones that get through are specifically designed to exploit human judgment in the moment — urgency, trust in a familiar brand, or a request that seems small enough to just comply with. A simple, repeatable checklist like this turns "does this feel weird?" into a concrete process anyone can follow, even without a security background.