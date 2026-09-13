# Источники и методика исследования

Дата доступа: **9 сентября 2026 года**. Исследование выполнено четырьмя параллельными потоками: onboarding/договоры, техническая интеграция, внешние developer case studies и локальный аудит Serendipity Games.

## Метод

- Первоисточники Poki использовались для требований, стадий, числовых порогов и коммерческой модели.
- Для важных практических выводов искались named developer postmortems с конкретными before/after данными.
- Sponsored articles, platform-hosted case studies и анонимные форумы не приравнивались к независимым правилам.
- Текущая live-форма была проверена через браузер, включая раскрывающиеся варианты.
- Локальные выводы основаны на статическом поиске, структуре файлов и подсчёте размеров; Poki Inspector и реальные fit-тесты ещё не запускались.
- Факты, выводы и рекомендации в документах разделены формулировками. Непубличные критерии не реконструировались как «секретные пороги».

## Официальные источники — высокий приоритет

1. [Poki for Developers](https://developers.poki.com/) — аудитория, инструменты, общая модель работы.
2. [Request access / Share your game](https://developers.poki.com/guide/share) — live-форма доступа и обязательные поля.
3. [Working with Poki](https://developers.poki.com/guide/working-with-poki) — поддержка и публичная схема 100% direct / 50:50 Poki traffic.
4. [What we look for](https://developers.poki.com/guide/what-we-look-for) — quality, player fit, tech, originality, depth, first impression, devices, roadmap.
5. [Poki for Developers platform](https://developers.poki.com/guide/p4d-platform) — team roles, versions, settings, categories, descriptions и thumbnails.
6. [Adding your game](https://developers.poki.com/guide/adding-your-game) — web build/prototype, moderation, Inspector и следующий шаг.
7. [How testing works](https://developers.poki.com/guide/how-testing-works) — пять стадий, метрики, сроки и целевые значения.
8. [Playtesting](https://developers.poki.com/guide/playtesting) — 10 recordings, данные записи, audience/device selection.
9. [Player Fit Test](https://developers.poki.com/guide/player-fit-test) — 500 игроков, >3 мин и ≥25% >3 мин, ~5 часов, 2 теста/день.
10. [Web Fit Test](https://developers.poki.com/guide/web-fit-test) — ~10 000 игроков, CTR/playtime/C2P, category benchmarking.
11. [Interpreting test results](https://developers.poki.com/guide/reading-results) — карта причин и цели 65% C2P/5+ минут.
12. [Final Review](https://developers.poki.com/guide/final-review) — ручное решение, 1–2 недели, причины и последствия.
13. [Release process](https://developers.poki.com/guide/release-process) — agreement, QA, Soft Release, Global Release и сроки.
14. [Requirements](https://developers.poki.com/guide/requirements-quality) — hard/platform/UX/ad/content requirements.
15. [Content & player safety](https://developers.poki.com/guide/content-player-safety) — family-safe content, clones/templates/AI/trends.
16. [External resources policy](https://developers.poki.com/guide/external-resources-policy) — CSP, privacy, запрещённые и одобряемые requests.
17. [Easy access & onboarding](https://developers.poki.com/guide/easy-access) — progressive loading, skip menu, visual onboarding, portrait.
18. [Engagement](https://developers.poki.com/guide/engagement) — session-0, примерно 3-минутный loop и scope.
19. [Localization](https://developers.poki.com/guide/localization) — порядок языков, browser detection и layout.
20. [Game thumbnail](https://developers.poki.com/guide/game-thumbnail) — static specs и CTR principles.
21. [Your game page](https://developers.poki.com/guide/your-game-page) — fullscreen policy и animated thumbnail specs.
22. [SDK overview & events](https://developers.poki.com/guide/sdk-overview) — события, последовательности, dashboard и CLI.
23. [PokiSDK: HTML5](https://developers.poki.com/guide/sdk-html5) — код интеграции, ads, input/audio, scroll и mobile pill.
24. [Game Events](https://developers.poki.com/guide/game-events) — `measure()` и аналитические funnels.
25. [Poki Inspector](https://developers.poki.com/guide/inspector) — QA modules, event log, devices, scaling, warnings.
26. [Choosing a web engine](https://developers.poki.com/guide/web-engine) — 5 MB initial/8 MB total ориентир и engine-specific факты.
27. [User Accounts](https://developers.poki.com/guide/accounts) — cloud save, login/token и ограничения.
28. [Monetization overview](https://developers.poki.com/guide/how-monetization-works) — midroll, rewarded и отсутствие IAP.
29. [Monetization tips](https://developers.poki.com/guide/monetization) — economy/reward placements.
30. [How we partner](https://developers.poki.com/guide/revenue-deal-types) — exclusive/non-exclusive, 5-year indicative term.
31. [Payouts & billing](https://developers.poki.com/guide/payouts-billing) — wire/PayPal, currency и billing lock.
32. [Post-release updates](https://developers.poki.com/guide/post-release-updates) — performance/content/language updates.
33. [Poki Terms of use, версия 13.03.2024](https://app.poki.dev/2024.03.13_Terms_and_Conditions_Poki_for_Developers.pdf) — тестовая лицензия, права, отсутствие гарантии/оплаты и termination.
34. [Official poki-cli](https://github.com/poki/poki-cli) — `build_dir`, authentication, upload и manual review.
35. [P4D production bundle](https://app.poki.dev/app.9e229c21.js) — фактические сообщения upload validator (10 000 files / 100 MB per file / 1 GB uncompressed). Это менее устойчивый источник, чем Guide: имя bundle меняется, лимиты надо перепроверять.

## Внешние кейсы — подтверждают практику, но не создают правила

### Высокая/средне-высокая уверенность

1. [Blumgi: I’ve killed my first Blumgi game, 28.08.2025](https://blumgi.games/ive-killed-my-first-blumgi-game/) — postmortem провала из-за skill floor, controls/goal и overscope.
2. [Blumgi: How my 15-year-old son gave me a game-making lesson, 07.09.2025](https://blumgi.games/how-my-15-year-old-son-gave-me-a-game-making-lesson/) — PFT 3:49→7:50 за пять дней, WFT >10 мин.
3. [Blumgi: From idea to millions of players, 15.09.2025](https://blumgi.games/from-idea-to-millions-of-players/) — Poki-specific checklist от успешного разработчика.
4. [Kuyi Mobile: My game production process, 03.02.2026](https://kuyimobile.substack.com/p/my-game-production-process-and-how) — трёхмесячный scope, быстрый prototype validation и не количественно описанный выбор из нескольких thumbnail-вариантов.
5. [Devortel: Vortella’s Dress Up, 28.05.2025](https://poki.com/blog/i-quit-my-job-to-make-a-dress-up-web-game-and-it-blew-up) — modal drop-off, item funnel, 6:28→12:40 session. Размещено Poki, но автор идентифицирован и цифры конкретны.
6. [OnRush: Higher success rates with playtests, 08.03.2024](https://poki.com/blog/higher-success-rates-with-playtests) — метод playtesting и reported 2→10 min после UX/input fix.
7. [Elanra: Cannon Clash load/C2P, 11.11.2024](https://poki.com/blog/how-we-made-cannon-clash-load-fast-and-boosted-conversion) — 2.4 MB, 76 requests, 81% C2P и удаление intro.
8. [Devortel: Story of Vortelli’s Pizza, 02.12.2022](https://poki.com/blog/the-story-of-vortellis-pizza) — единичный пример ответа/договора за несколько дней; не SLA.
9. [Blumgi’s web journey, 05.09.2023](https://poki.com/blog/blumgi-my-journey-on-the-web-how-i-reached-100m-players-in-2-years-as-an-indie-game-developer) — каталог и долгосрочная publisher relationship.
10. [Defold: Flazm and Poki, 01.06.2021](https://defold.com/2021/06/01/Developer-Case-Study-Flazm-and-Poki/) — pacing и опыт QA.
11. [PlayCanvas: Vortelli’s Pizza, 10.11.2022](https://forum.playcanvas.com/t/vortellis-pizza-a-3d-multiplayer-kitchen-sim/28322) — soft launch scale и server scaling.
12. [PlayCanvas: Pizza Delivery, 08.11.2023](https://forum.playcanvas.com/t/vortelli-s-pizza-delivery-a-3d-open-world-driving-game/33735) — 5 MB target, реальный device performance и launches.
13. [Defold–Poki integration, 25.04.2025](https://defold.com/2025/04/25/Defold-Foundation-And-Poki-Integration/) — прямой build/upload integration.

Кейсы Devortel, OnRush, Elanra и архивный Blumgi размещены/редактировались на Poki Blog. Это first-person partner case studies с конкретными, но self-reported цифрами, а не независимые controlled studies.

### Средняя уверенность / явная заинтересованность

14. [EU-Startups sponsored Poki article, 15.04.2026](https://www.eu-startups.com/2026/04/how-amsterdam-based-poki-is-becoming-one-of-the-best-launchpads-for-indie-game-developers-in-europe-sponsored/) — цитата о подписании developer relationship, не независимый criterion.
15. [Bounty Board: monetizing HTML5, Aug 2026](https://www.bountyboard.gg/blog/how-to-monetize-an-html5-game) — корректная оговорка об индивидуальном revenue share; не источник условий Poki.

### Низкая уверенность / только контекст

16. [Reddit: Making a living off web games, 2023–2024](https://www.reddit.com/r/gamedev/comments/16bhlit/making_a_living_off_web_games/) — старые жалобы на отсутствие ответа и комментарии предполагаемого представителя.
17. [Reddit: submit games to Poki, 2024–2025](https://www.reddit.com/r/gamedev/comments/1gs4343/any_devs_ever_submit_their_web_games_to_poki/) — анонимные сроки ожидания 3–4 недели.
18. [Defold forum, 18.03.2026](https://forum.defold.com/t/i-have-decided-to-create-a-Web-3D-mini-game-called-Gravity-Attack/82367?page=3) — анекдот о signup; не использовать описанный обходной путь.
19. [Google AdMob interview, 2015](https://blog.google/products/admob/app-monetization-insights-how-poki/) — исторический mobile context, не текущий Poki Web Fit threshold.

## Синтез внешних кейсов

Повторяющиеся, хорошо подтверждённые темы:

- playable prototype важнее большого GDD;
- быстрый core action и понятная цель;
- touch/desktop controls проверяются реальными игроками;
- одна итерация должна отвечать на одну гипотезу;
- визуальная красота не компенсирует скучный/непонятный loop;
- маленький initial payload — один из основных факторов C2P наряду с execution/device performance и onboarding;
- scope увеличивают после доказательства fit;
- разработчик должен быстро читать данные и выпускать обновления.

Не подтверждено как универсальное правило:

- фиксированный CTR для всех жанров;
- D1/D7 как текущий порог Poki review;
- гарантированный срок ответа на developer application;
- гарантированный объём трафика или конкретная homepage/category позиция; при этом Release Process обещает участие Global Release в promotion system и заметный системный push новой игре примерно на две недели;
- обязательный большой портфель/юрлицо;
- универсальная revenue-share ставка вне конкретного договора.

## Замеченные расхождения/нестабильность

- Web Fit duration: обзор — ~7 дней; профильная страница — 3–5 дней, иногда больше. В документах использован плановый диапазон до недели+.
- Terms датированы 13.03.2024, тогда как Guide динамически обновляется. Publishing agreement всё равно отдельный.
- Старые форумы описывают прежние способы регистрации; текущую live-форму и текущий Guide считать приоритетнее.
- Production bundle и его лимиты могут смениться без стабильного URL.

## Пробелы, которые можно закрыть только после доступа/контракта

- фактический response SLA и причина решения по developer application;
- полный интерфейс создания game entry и текущий upload validator;
- category-specific CTR benchmarks;
- точные QA browser/device matrices;
- коммерческий договор, attribution rules, payout calendar/threshold и налоги;
- допустимость portfolio demo при web-exclusive deal;
- реальные Player Fit/Web Fit показатели каждой игры Serendipity Games.
