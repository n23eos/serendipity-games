# Контент, IP, AI и коммерческие условия

## Контент и безопасность игроков

Poki рассчитан на широкую аудиторию, включая детей, и требует advertiser-safe контент. Вне scope:

- bullying, abuse, stereotypes, sexism;
- graphic violence, открытые/инфицированные раны, видимые жидкости тела;
- длительные страшные темы;
- sexual content/неподходящая одежда;
- cheating, gambling, alcohol, tobacco и offensive material;
- in-game chat; безопасная альтернатива — emoji-система.

Лёгкие проблемные элементы иногда можно удалить/переосмыслить. Adult themes и неправомерно использованный IP ведут к немедленному отказу. Источник: [Content & player safety](https://developers.poki.com/guide/content-player-safety).

## Оригинальность

Не принимаются прямые копии, asset flips и почти неизменённые templates. Poki сравнивает art style, loop/goal/input, progression/economy, UI/icons/audio, персонажей, name/thumbnail. Вдохновение жанром допустимо, если есть собственная механика, twist, blend, мир или progression.

Переполненность категории сама по себе может снизить шанс: Poki управляет разнообразием и может отказаться от ещё одной похожей игры, даже если она работает.

## AI-контент

AI использовать можно, но Poki ждёт человеческой авторской работы:

- цельный и очищенный visual style;
- нет watermark/prompt text;
- диалоги отредактированы;
- сгенерированные levels вручную проверены и сбалансированы;
- AI-code протестирован и оптимизирован;
- разработчик контролирует game logic;
- по запросу можно показать инструменты, процесс, prompts и iterations;
- условия AI-сервисов разрешают коммерческое использование и выполнены требования attribution.

Полностью AI-созданная игра несёт риск неясного IP ownership. Источник: канонический раздел [Content & player safety — Working with AI](https://developers.poki.com/guide/content-player-safety).

Для этого проекта следует сохранить отдельный provenance manifest: файл → автор/источник → лицензия/договор → применённый AI tool → prompt/итерации → ручные изменения.

## Что принимается при использовании P4D

[Terms of use P4D в официальном файле с `2024.03.13` в имени](https://app.poki.dev/2024.03.13_Terms_and_Conditions_Poki_for_Developers.pdf) относятся к **временному тестированию**, а не к последующему partnership agreement.

Основные пункты:

- данные аккаунта правдивы и актуальны;
- сервис бесплатен, но тестирование и публикация не гарантированы;
- тестовый трафик не оплачивается;
- разработчик сохраняет ownership, но даёт Poki worldwide license для web-тестирования;
- у разработчика есть права/разрешения на код, название, artwork, OSS, stock, музыку и работу contractors;
- Terms 2024 запрещают third-party trackers; текущая External Resources Policy допускает отдельные analytics providers только после case-by-case CSP/privacy approval (Google Analytics и другие Google products не одобряются). До письменного одобрения считать tracker запрещённым;
- нельзя загружать нарушающий права/закон контент;
- разработчик гарантирует отсутствие соглашений, конфликтующих с правами, предоставленными Poki, включая ранее выданную третьей стороне эксклюзивность;
- preview link нельзя использовать для распространения на конкурентной платформе;
- Poki и разработчик могут прекратить тестирование/использование аккаунта в рамках условий;
- применяется право Нидерландов и юрисдикция Амстердама с оговоркой об обязательном consumer law.

Перед реальной подачей читать PDF полностью: юридическое резюме здесь не заменяет консультацию.

## Модели сотрудничества после Final Review

### Web exclusive — предпочтительная Poki модель

- та же игра в open web публикуется только на Poki;
- Discord и YouTube Playables считаются web;
- Steam, mobile stores и consoles остаются свободны;
- default term сейчас описан как 5 лет;
- прямой/search/bookmark/social/community трафик разработчика: публичный ориентир 100% дохода разработчику;
- трафик Poki.com/маркетинга Poki: публичный ориентир 50/50.

Источники: [How we partner](https://developers.poki.com/guide/revenue-deal-types), [Working with Poki](https://developers.poki.com/guide/working-with-poki).

Poki прямо называет срок, revenue share и investment **indicative**: реальные условия задаёт индивидуальный договор. Значит, 5 лет и 50/50 нельзя считать гарантией.

### Non-exclusive

Для уже опубликованной на других web-порталах либо более нишевой/краткосрочной игры Poki описывает разовую flat license fee, без revenue share и без маркетинговой инвестиции exclusive-модели. Размер выплаты не опубликован.

## Монетизация и выплаты

- Midroll и rewarded video идут через Poki SDK; IAP недоступны, сторонние рекламные системы не допускаются.
- Выплата — wire transfer или PayPal в предпочитаемой валюте.
- После релиза billing настраивается в Team settings, dashboard показывает earnings по дням.
- Точный расчёт определяет договор; billing details блокируются на период текущего платёжного цикла после email notification.

Источники: [Monetization overview](https://developers.poki.com/guide/how-monetization-works), [Payouts & billing](https://developers.poki.com/guide/payouts-billing).

## Что обязательно проверить в индивидуальном договоре

Публично не раскрыты либо не гарантированы:

- точный revenue share/flat fee, доступные валюты, валюта расчёта, FX-правила, payout schedule/threshold, fees и taxes;
- определение direct и Poki-attributed traffic;
- minimum guarantee/advance;
- term, renewal, termination и последствия снятия игры;
- разрешение оставить demo на собственном сайте/itch.io;
- обязательства по updates, support, QA и срокам исправлений;
- объём/гарантии marketing и placement;
- ownership, derivative works, sequels, ports, trademarks;
- Discord/YouTube/webview и будущие web-каналы;
- audit/reporting rights, indemnities, liability и dispute process.

Это список для юриста/переговоров, а не утверждение, что каждый пункт будет проблемным.
