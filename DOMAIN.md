# serendipity-games.com

2026-09-09: configured GitHub Pages custom domain and all five Cloudflare DNS records below (DNS only, TTL Auto). CNAME was created by GitHub in commit 08eb82b and fast-forwarded locally. Redesign commit 4c74a22 was pushed to main; Pages build succeeded.

Verified: authoritative DNS values, Cloudflare table, GitHub Pages health reports both domains valid and HTTPS-eligible. Eighteen live HTTP page/asset/game entrypoints return 200; www redirects to apex.

Pending: GitHub Pages certificate provisioning. Latest HTTPS request fails hostname validation; https_certificate is null and https_enforced is false. Recheck certificate readiness, then enable Enforce HTTPS and verify both domains. Do not bypass certificate validation. No further DNS change is needed based on the current health response.

Configured DNS:

| Type | Name | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | n23eos.github.io |

Root CNAME contains `serendipity-games.com`. Both locales and game entrypoints have been published; final HTTPS check remains pending.

Source: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
