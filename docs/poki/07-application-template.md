# Черновик заявки Serendipity Games

Это рабочий текст, а не отправленная форма. Личные данные, страна и фактический состав команды должны быть заполнены владельцем аккаунта. Перед отправкой выбрать одну флагманскую игру и заменить все `[PLACEHOLDER]`.

## Рекомендация для текущей формы

Проверено по открытому черновику формы 9 сентября 2026 года; форма не отправлялась.

- `AA / Mid-Sized Studio` оставлять только для реально сформированной студии среднего размера с соответствующей командой и production history. Для маленькой независимой команды выбрать вариант формы с `Indie`, для одного разработчика — `Solo Developer`.
- Текущий `Hypercasual` заменить на более точное `Casual, arcade puzzle, runner, action, and match puzzle games`. Если нужен более сфокусированный профиль вокруг первого кандидата: `Casual arcade and puzzle games with approachable, replayable core loops`.
- Технологии можно записать чище: `JavaScript/TypeScript, HTML5 Canvas, and Three.js` — только если всё перечисленное действительно используется командой.
- Главную страницу не оставлять единственной ссылкой. Поставить первым мгновенно запускаемый английский Ricochet, затем portfolio:

```text
https://serendipity-games.com/play.html?game=ricochet&lang=en, https://serendipity-games.com/
```

- Текущий сайт честно маркирует игры как `IN DEVELOPMENT` и `PLAYABLE DEMO`. Поэтому `Web` в поле **previously released games** лучше снять, если ни одна игра не имела фактического публичного релиза; само поле платформы не Required. Обязательное поле ссылок всё равно можно заполнить playable demo и portfolio.
- К `Releasing new titles` и `Releasing existing titles` стоит добавить `Using our developer tools`, если план — использовать Playtesting, Player Fit и Web Fit для итераций.
- Перед отправкой проверить доставку на `hello@serendipity-games.com` тестовым письмом с другого адреса.

## Значения формы

**What's your name?**

`[REAL FULL NAME]`

**What's your email?**

`hello@serendipity-games.com` либо `[DIRECT WORK EMAIL]`

**What's the name of your studio or team?**

`Serendipity Games`

**In which country are you based?**

`[REAL COUNTRY OF PERSON OR ENTITY]`

**How would you describe your studio or team?**

- `Indie Studio`
- `Solo Developer` — выбрать только если это фактически верно; форма допускает multiple selection.

**If you've previously released games, which platform have you used?**

- `Web` — выбирать только для фактически публично выпущенной игры. Playable development demo само по себе не считать previous release без уверенности; поле не помечено Required и его можно оставить пустым.
- Другие варианты добавлять только при реальных релизах.

**Can you provide us with links to those games?**

Вариант после подготовки flagship:

```text
Studio portfolio: https://serendipity-games.com/
Featured playable web demo: [DIRECT ENGLISH GAME URL]
Additional demos: [OPTIONAL, ONLY POLISHED LINKS]

Serendipity Games is an indie studio focused on original, instantly playable casual web games. The linked builds are playable development demos, not previously published Poki titles. We own or have commercial rights to the code and production assets and can provide an asset/AI provenance overview if needed.
```

**Which genres do you typically work on?**

```text
Casual action, arcade puzzle, runner, and match puzzle games, with an emphasis on approachable core loops and progression.
```

Сократить список до жанров выбранных 1–2 сильных проектов, если Poki ожидает более узкий фокус.

**Which engines do you typically work with?**

Сверить с исходниками и оставить только правду:

```text
HTML5, JavaScript/TypeScript, and Three.js-based web development. [ADD/REMOVE ACTUAL ENGINES].
```

**What are you looking to gain from working with Poki?**

- `Releasing existing titles`
- `Releasing new titles`
- `Using our developer tools`

Выбрать все три, если план действительно включает текущие игры, будущие игры и Poki testing/analytics.

## Короткий сопроводительный pitch

Форма сейчас не показывает отдельного длинного pitch-поля. Текст пригодится, если Poki ответит email или попросит контекст.

```text
Hi Poki team,

I'm [NAME] from Serendipity Games, an indie studio building original casual games for instant play on mobile and desktop web.

Our current portfolio is available at https://serendipity-games.com/. The best starting point is [GAME + DIRECT URL], a [GENRE] where players [CORE ACTION] to [GOAL]. Its distinguishing hook is [ONE SPECIFIC, VISIBLE DIFFERENTIATOR].

We would like to use Poki's playtesting and fit-test tools to validate the first-session experience, iterate from real player behavior, and prepare the strongest title for release. We can produce a dedicated Poki build, integrate the Poki SDK, optimize loading and cross-device controls, and support fast updates during testing and soft release.

The linked games are playable development demos. We can provide a clear overview of asset licenses and any AI-assisted production steps on request.

Best,
[NAME]
Serendipity Games
hello@serendipity-games.com
```

## Вставка про конкретную игру

### Ricochet: Neon Drive

```text
Ricochet: Neon Drive is an arcade puzzle game where players line up a shot, predict its bounces, and solve compact neon challenges. Its second mirror-puzzle mode extends the same light-and-angle fantasy with a distinct puzzle format.
```

Проверить, что `second mirror-puzzle mode` доступен в подаваемом билде и не переусложняет первый pitch.

### Bunny Runner

```text
Bunny Runner is a fast, approachable lane runner where a small rabbit dodges, jumps, and dives through colorful worlds. Its distinguishing Poki pitch must be completed with a concrete mechanic or progression feature that is not just a character/theme swap: [SPECIFIC TWIST].
```

Не отправлять `[SPECIFIC TWIST]` и не заявлять originality, пока отличие не сформулировано и не видно в первых минутах.

## Ответы на вероятные вопросы

**Is the game already live elsewhere on the web?**

```text
The current development demo is playable on our own portfolio site. It has not been commercially launched on another web-game portal. [CORRECT IF NEEDED].
```

**Are you open to web exclusivity?**

```text
We are open to reviewing a web-exclusive partnership for the right title. We would need to review the individual agreement, including treatment of our own portfolio demo and other browser channels, before confirming.
```

**How will you support the game?**

```text
We can prioritize test-driven onboarding, performance, and control improvements, respond quickly during QA and soft release, and maintain a roadmap covering [2–3 REAL UPDATE THEMES].
```

## Финальная проверка текста

- [ ] Нет преувеличений: demo ≠ commercial release, portfolio views ≠ players.
- [ ] Все ссылки открыты без логина, HTTPS и mobile-friendly.
- [ ] Одна игра явно главная.
- [ ] Differentiator конкретен и виден в gameplay.
- [ ] Указаны реальные engines, страна и состав команды.
- [ ] Нет обещания эксклюзивности без договора.
- [ ] IP/AI statement подтверждается внутренними документами.
- [ ] Текст вычитан на естественный английский.
