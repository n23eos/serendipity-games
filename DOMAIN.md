# serendipity-games.com

2026-09-09: GitHub Pages serves n23eos/serendipity-games, main branch root. Custom domain currently unset. DNS nameservers: matt.ns.cloudflare.com, betty.ns.cloudflare.com; no apex A record returned. No remote setting changed.

Pending Cloudflare zone access. Configure GitHub Pages custom domain before adding DNS, then verify HTTPS issuance and enforce HTTPS. Do not switch the live Pages URL until the DNS change can be completed.

Required DNS:

| Type | Name | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | n23eos.github.io |

At activation, create root CNAME file containing `serendipity-games.com` and publish the verified site. Check apex and www HTTPS, redirects, both locales, and game assets.

Source: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
