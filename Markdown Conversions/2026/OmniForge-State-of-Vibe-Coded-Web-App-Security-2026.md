**OmniForge Security Research**  
*228 SaaS Benchmarks · Honest Comparisons · VibeShield v7.0 · InboxShield v7.0 · BrandShield v6.2*  
*Launch Special: $2 (was $9)*  
*Launch Audit Reports / 2026 Vibe-Coded Web App Security Study*  
*Live Empirical Study (2026-11-22) · 55 Newly Shipped Apps · 6,126 Read-Only Checks*

---

# State of AI & Vibe-Coded Web App Security (2026)

## Table of Contents
- [Executive Overview](#executive-overview)
- [Audit Your Own Production URL Free](#audit-your-own-production-url-free-live-vibeshield-v70-engine)
- [1. Most Common Vulnerabilities Found Across 55 Newly Shipped Apps](#1-most-common-vulnerabilities-found-across-55-newly-shipped-apps)
- [2. Security Posture by Hosting Platform](#2-security-posture-by-hosting-platform)
- [3. Why AI Code Generators Miss These 4 Controls by Default](#3-why-ai-code-generators-miss-these-4-controls-by-default)
  - [1. Zero HTTP Security Headers on Default Deployments](#1-zero-http-security-headers-on-default-deployments)
  - [2. Client-Side Secret Leaks in Bundled JS](#2-client-side-secret-leaks-in-bundled-js)
  - [3. Unprotected Supabase Tables (Missing RLS)](#3-unprotected-supabase-tables-missing-rls)
  - [4. Forgotten Static Files & Source Maps](#4-forgotten-static-files--source-maps)
- [4. Copy-Paste 60-Second Hardening Snippets (Free MIT)](#4-copy-paste-60-second-hardening-snippets-free-mit)
  - [A. Baseline Security Headers for vercel.json](#a-baseline-security-headers-for-verceljson-fixes-7-of-10-observatory-checks-immediately)
  - [B. Mandatory Supabase Row Level Security Baseline SQL](#b-mandatory-supabase-row-level-security-baseline-sql)
- [Launch Special: Fix Every Finding in 5 Minutes — $2 Once (was $9)](#launch-special-fix-every-finding-in-5-minutes--2-once-was-9)
- [Stack-Specific Hardening Guides & Live Scanners](#stack-specific-hardening-guides--live-scanners)
- [Complete Your Pre-Launch Checklist (Zero-Install Free Web Tools)](#complete-your-pre-launch-checklist-zero-install-free-web-tools)

---

## Executive Overview

AI builders like Cursor, Lovable, Bolt, and v0 let solo founders ship production web apps in hours. We ran **VibeShield v7.0** (6-phase passive scanner, ~111 checks per app) across 55 freshly launched public GitHub web apps to measure what actually ships unprotected on day one.

[Scan Your Own App Free (6-Phase Deep Audit) → Launch Special: Unlock Full Fixes $2 (was $9)](https://yourdomain.com)  
[Open-Source Security Checklist (MIT)](https://yourdomain.com)

- **74.5%** — Missing 8–9 of 10 Security Headers (41/55)
- **20.0%** — Ship Live Supabase Backends (11/55)
- **3.6%** — Leaked Client Secret / API Key (2/55)
- **6,126** — Total Passive Checks Executed (Avg Score 81/100)

> **Responsible Disclosure & Anonymization Policy:** Every scan in this study was strictly passive and read-only (TLS handshake, public HTTP headers, client-delivered JS assets, and non-destructive metadata checks). To protect indie builders, zero target domains with critical secret leaks or exposed files are named here, and zero raw key material is ever stored or published.

---

## Audit Your Own Production URL Free (Live VibeShield v7.0 Engine)

Paste your `.lovable.app`, `.vercel.app`, `.netlify.app`, or custom production domain to run all 6 passive phases (TLS, 24 JS bundles, 52 secret rules, Supabase/Firebase check, 28 probes, 10 Observatory headers):

`https://your-app.vercel.app or yourdomain.com` [Run 6-Phase Scan Free]

*Try benchmark demos:*  
`supabase.com` · `vercel.com` · `linear.app`

---

## 1. Most Common Vulnerabilities Found Across 55 Newly Shipped Apps

- **Missing 8–9 of 10 Mozilla Observatory Security Headers**: 74.5% (41/55)
- **Missing Any Security Header (CSP / HSTS / XFO / COOP / security.txt)**: 100.0% (55/55)
- **Live Supabase Backend Detected (Requires Strict RLS Policy Audit)**: 20.0% (11/55)
- **Weak CSP Directives (`unsafe-inline` / missing `base-uri` or `frame-ancestors`)**: 12.7% (7/55)
- **Client-Delivered Secret / API Key Detected (Anonymized; 1 Critical Stripe Live Key)**: 3.6% (2/55)
- **Exposed Sensitive File (`/.DS_Store` Reachable on Production Host)**: 3.6% (2/55)

---

## 2. Security Posture by Hosting Platform

| HOSTING PLATFORM | APPS AUDITED | AVERAGE VIBESHIELD SCORE | APPS SCORING BELOW 70 | PRIMARY GAP OBSERVED |
| :--- | :--- | :--- | :--- | :--- |
| **Custom Domain** | 9 | 79 / 100 | 11% | Highest variance — includes exposed `/.DS_Store`, weak HSTS & client-side API key leaks |
| **Vercel** | 41 | 82 / 100 | 0% | Default deployments ship without CSP, Permissions-Policy, COOP/CORP, or `security.txt` |
| **GitHub Pages** | 4 | 78 / 100 | 0% | Cannot set custom HTTP security headers without a Cloudflare/edge proxy |
| **Cloudflare Pages** | 1 | 98 / 100 | 0% | Strong edge defaults; verify CSP & backend RLS policies |

---

## 3. Why AI Code Generators Miss These 4 Controls by Default

### 1. Zero HTTP Security Headers on Default Deployments
Vercel, Netlify, and Lovable provide automatic HTTPS, which lulls builders into thinking transport and browser security are finished. In our sample, 74.5% of apps shipped without `Content-Security-Policy`, `X-Frame-Options`, `Permissions-Policy`, or `Cross-Origin-Opener-Policy`, leaving apps exposed to XSS script injection and clickjacking.

### 2. Client-Side Secret Leaks in Bundled JS
When AI assistants wire Stripe, OpenAI, or Gemini SDKs quickly, they occasionally import server secrets into client components or `NEXT_PUBLIC_` / `VITE_` variables. Even a 3.6% live key leak rate (including a live Stripe secret key in our 55-app batch) translates to catastrophic billing or data exposure.

### 3. Unprotected Supabase Tables (Missing RLS)
20.0% of freshly launched apps shipped with Supabase. Creating a table in the SQL editor or via an AI migration prompt without `ENABLE ROW LEVEL SECURITY` and explicit `auth.uid()` policies allows anyone holding the public anon key to query or mutate rows via PostgREST.

### 4. Forgotten Static Files & Source Maps
Pushing local build directories without strict ignore rules leaves `/.DS_Store`, `.env` backups, or full production `.js.map` source maps reachable on public hosts — handing attackers your entire folder layout and unminified business logic.

---

## 4. Copy-Paste 60-Second Hardening Snippets (Free MIT)

### A. Baseline Security Headers for vercel.json (Fixes 7 of 10 Observatory Checks Immediately)

```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains; preload" },
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()" },
        { "key": "Cross-Origin-Opener-Policy", "value": "same-origin" },
        { "key": "Content-Security-Policy", "value": "default-src 'self'; base-uri 'self'; font-src 'self' https: data:; form-action 'self'; frame-ancestors 'self'; img-src 'self' data: https:; object-src 'none'; script-src 'self'; style-src 'self' 'unsafe-inline'; upgrade-insecure-requests" }
      ]
    }
  ]
}
```

### B. Mandatory Supabase Row Level Security Baseline SQL

```sql
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users read own profile only"
ON public.profiles FOR SELECT
USING (auth.uid() = id);

CREATE POLICY "Users update own profile only"
ON public.profiles FOR UPDATE
USING (auth.uid() = id)
WITH CHECK (auth.uid() = id);
```

---

## Launch Special: Fix Every Finding in 5 Minutes — $2 Once (was $9)

Run a free 116-check scan on VibeShield v7.0, then unlock exact JS chunk locations, line-level evidence, and tailored 5-platform fix scripts (Cursor/Lovable, Next.js/Vercel, Cloudflare, Nginx, Supabase SQL) for $2 once (78% off Launch Special, was $9) — zero monthly subscription, 14-day refund guarantee.

- [Run Free 6-Phase Scan →](https://yourdomain.com)
- [Unlock VibeShield — $2 (was $9)](https://yourdomain.com)
- [Complete 3-App Suite — $5 (was $29)](https://yourdomain.com)

---

## Stack-Specific Hardening Guides & Live Scanners

### Lovable + Supabase
**Lovable App Security Checklist**  
Live scanner + RLS SQL lockdown for `.lovable.app` and custom domains.  
[Open Lovable guide →](https://yourdomain.com)

### Cursor + Next.js
**Cursor & Next.js Hardening Guide**  
Drop-in `next.config.mjs` `headers()`, `.cursor/rules` & source-map lockdown.  
[Open Cursor guide →](https://yourdomain.com)

### Bolt.new + Netlify
**Bolt.new & Netlify Security Audit**  
Fix `VITE_` secret leaks & deploy `public/_headers` cleanly.  
[Open Bolt guide →](https://yourdomain.com)

### PostgreSQL RLS
**Supabase RLS Audit & SQL Guide**  
Two-query audit catching every public table missing Row Level Security.  
[Open Supabase guide →](https://yourdomain.com)

---

## Complete Your Pre-Launch Checklist (Zero-Install Free Web Tools)

### 100% Free Domain + USPTO
**Moving Off `.vercel.app` or `.lovable.app`?**  
Check 78+ domain extensions via direct IANA RDAP, live USPTO Class 009/042 trademarks, and aftermarket availability on BrandShield v6.2.  
[Check Your Launch Domain →](https://yourdomain.com)

### Email Deliverability ($2 Launch Special)
**Signup Emails Landing in Spam?**  
Verify SPF <=10 lookup limits, 24 DKIM selectors, DMARC policy, and 5 DNSBL blacklists in 2 seconds on InboxShield v7.0.  
[Audit Email DNS Free →](https://yourdomain.com)

### AI Search GEO ($2 Launch Special)
**Invisible to ChatGPT & Perplexity?**  
Check 10 global & China AI crawlers, score Schema.org Entity Graph depth, and generate `/llms.txt` on CiteReady v6.0.  
[Check AI Visibility Free →](https://yourdomain.com)

---

OmniForge · Agent Arena Studio · Empirical read-only security research. Zero raw secrets stored or published.  
*228 SaaS Benchmarks · 4 Honest Comparisons · Support 14-Day Refund · agentarenastudio@proton.me · @agentarenastudi*

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-11-24", "model": "gemini-3.8-flash"} -->
