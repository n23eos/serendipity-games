# Готовность Serendipity Games к Poki

Дата локального аудита: 9 сентября 2026 года. Это статическая проверка текущих portfolio-builds, а не Poki Inspector/Player Fit Test. Игры не изменялись.

## Что уже хорошо для заявки разработчика

- Живой англоязычный сайт: `https://serendipity-games.com/`.
- Четыре мгновенно запускаемых browser-demo без установки и аккаунта.
- Ясное позиционирование: casual browser game studio.
- Опубликованный контакт: `hello@serendipity-games.com`; forwarding настроен со слов пользователя, фактическая доставка письма не проверялась.
- Покрыты action/survival, runner, match puzzle и arcade puzzle.
- README явно говорит, что это unreleased demos и что текущие standalone adapters — **не Poki SDK integration**.

Для первичной заявки это полезное доказательство способности довести проекты до web-build. Но portfolio-build и submission-ready Poki-build — разные артефакты.

## Текущая техническая картина

| Игра | Файлы / общий размер | Poki SDK | Текущие риски |
|---|---:|---:|---|
| Ricochet: Neon Drive | 62 / 2.53 MiB | нет | нужно доказать touch-удобство, удержание 5+ минут и выразительную оригинальность |
| Bunny Runner | 40 / 2.92 MiB | нет | насыщенная runner-категория; требуется сильное отличие от известных lane runners |
| Jelly Mix | 97 / 15.33 MiB | нет | raw-папка больше Poki-ориентира 8 MB total; два MP3 весят примерно 1.34 и 1.57 MB; нужны замеры transfer, progressive loading и оптимизация |
| Bunny Survival | 350 / 55.06 MiB | нет | raw-папка во много раз больше ориентира; много крупных MP3, landscape/mobile friction, platform/economy cleanup |

Размеры посчитаны по raw-содержимому `games/<slug>` и не равны compressed initial или total network transfer: часть ресурсов сжимается и может грузиться лениво. Окончательный вывод возможен только после измерения initial/total download и requests в Inspector/DevTools.

Дополнительные находки:

- Все четыре `index.html` размечены `lang="ru"`; portfolio wrapper может передавать язык, но Poki-build должен иметь проверенный English default/browser-language selection.
- В собранных bundles найдены маркеры Yandex/других platform adapters; в Bunny Survival также есть CrazyGames adapter strings. Это не доказывает активный network call, но перед Poki submission чужие SDK/покупки/ads надо удалить из исходного build target, а не маскировать.
- В `games/*` нет `PokiSDK` или `game-cdn.poki.com`.
- Текущие промоизображения — landscape (`800×470` или `1119×630`), не квадратные Poki thumbnails ≥628×628.
- Animated thumbnails 1:1 пока нет.
- Долговременное сохранение использует `localStorage`; все найденные прямым статическим поиском вызовы `getItem`/`setItem`/`removeItem` уже защищены `try/catch`. Всё равно нужны runtime-проверка incognito и проверка поведения сохранения. Cloud/account sync — отдельная возможность Poki, а не общее требование; достаточно надёжного уместного сохранения либо ясного предупреждения об его отсутствии.
- Прямые внешние runtime-URL по грубому статическому поиску не обнаружены, кроме строк спецификаций W3C/ссылки Three.js в vendor code. Реальные network requests всё равно нужно проверить в Inspector.
- В `games/bunny-survival/index.html` boot-art использует корневой путь `/images/run-…`, тогда как файлы лежат в `games/bunny-survival/images/`: текущий корневой URL даёт 404, относительный — 200. В отдельном Poki-build путь нужно заменить на `./images/...` и проверить все варианты заставки.

## Предварительный порядок кандидатов

Это **рекомендация**, пока нет Player Fit данных.

### 1. Ricochet: Neon Drive — первый дешёвый кандидат

Почему:

- самый маленький общий build;
- отличимая arcade-puzzle подача потенциально лучше защищена от clone/saturation риска;
- проще довести до Poki технического baseline и быстро проверить fit.

Главный риск: головоломка может давать короткую сессию или требовать слишком точного ввода. Перед заявкой нужен внутренний 10-player test: понимают ли цель без текста, делают ли первый выстрел за 10–15 секунд, остаются ли на несколько уровней.

### 2. Bunny Runner — сильный вариант на мгновенный onboarding

Плюсы: маленький build, понятный genre, touch/keyboard premise. Риски: высокая конкуренция и сравнение с Subway Surfers/другими lane runners. В pitch нужно назвать конкретный оригинальный twist, а не только «кролик вместо героя».

### 3. Jelly Mix — потенциально сильное удержание после оптимизации

Плюсы: 300 levels, pets/world progression, понятный casual loop. Риски: raw-папка 15.33 MiB до сетевого сжатия и насыщенная match-категория. Имеет смысл после замера initial/total transfer, разделения initial/late content и доказательства уникального loop/мета-игры.

### 4. Bunny Survival — отдельный optimization project

Плюсы: заметная глубина, progression и update hooks. Риски: raw-папка 55.06 MiB до сетевого сжатия, сотни файлов и много музыки по 1–2 MB; адаптер другого портала и потенциальные purchase/economy ветки. Не отправлять как первый Poki-build без существенной упаковки, сетевых замеров и мобильного теста.

## Что сделать до заявки на доступ

### Минимум

1. Выбрать Ricochet или Bunny Runner для первой ссылки после сайта.
2. Подготовить English-first direct link без русской заставки и чужого platform branding.
3. Записать 20–30 секунд чистого gameplay video/GIF для быстрого просмотра, но playable URL оставить главным доказательством.
4. Добавить на game detail page конкретные engine/input/platform facts и один чёткий differentiator.
5. Подготовить внутренний IP manifest.
6. Заполнить английский черновик из [07-application-template.md](07-application-template.md).

### Не делать до получения доступа, если это задержит заявку

- Не обязательно полностью интегрировать Poki SDK во все четыре игры.
- Не требуется заранее делать animated thumbnail для каждого проекта: её добавляют и тестируют во время Soft Release выбранной игры, но она обязательна до Global Release.
- Не нужно обещать эксклюзивность до чтения индивидуального договора.

## План отдельного Poki-build для выбранной игры

1. Создать отдельный platform target/adapter `poki`, не менять portfolio build.
2. Удалить Yandex/CrazyGames SDK, IAP, `no ads`, стороннюю рекламу и прямые external links.
3. До Web Fit интегрировать `init`, loading и gameplay state; добавлять `measure()` только под конкретные аналитические гипотезы.
4. После подтверждения fit, к QA/Soft Release, встроить естественные commercial/rewarded placements.
5. English default + browser language fallback; visual tutorial.
6. Проверить portrait/landscape решение, tablet-as-mobile controls и 16:9 scaling.
7. Сделать initial package ≤5 MB и по возможности total ≤8 MB; тяжёлый контент грузить после первого gameplay.
8. Проверить incognito/ad blocker/SDK failure/offline-ish slow network.
9. Создать квадратную честную thumbnail; animated thumbnail добавить в Soft Release и завершить до Global Release.
10. Прогнать Inspector, затем 10 qualitative recordings → Player Fit → Web Fit.

## Внутренние метрики готовности

Перед Player Fit:

- first meaningful input ≤10–15 секунд после готовности build;
- никто из 10 внешних тестеров не спрашивает основную цель;
- нет blocker/crash/console error на test matrix;
- initial download ≤5 MB, total target ≤8 MB или обоснованный progressive exception;
- median внутренней первой сессии ≥5 минут как отдельный более строгий внутренний proxy; он не сопоставим напрямую с официальным average и не заменяет Poki test.

Внутренние цели во время Web Fit и перед Final Review:

Это ориентиры Poki и проектные цели, а не опубликованные отдельные pass/fail-пороги Web Fit. Poki сравнивает CTR, time on page и C2P с категорией, придаёт им одинаковый вес и выдаёт category score 0–5; точная формула прохода не опубликована ([How testing works](https://developers.poki.com/guide/how-testing-works), [Web Fit Test](https://developers.poki.com/guide/web-fit-test)).

- Poki C2P ≥65%, лучше около/выше 70%; 80%+ — амбициозная цель, а не официальный проходной порог;
- average playtime ≥5 минут (10+ для management/sim);
- Player Fit заметно выше минимума: average playtime >3 минут **и** ≥25% из 500 сессий >3 минут;
- стремиться улучшать thumbnail CTR относительно category benchmark; отдельного опубликованного порога нет;
- нет originality/content/IP/AI provenance рисков;
- есть реалистичный roadmap обновлений и возможность быстро отвечать в Soft Release.

## Доказательства из публичных кейсов

- Blumgi Merge: ежедневные итерации подняли Player Fit playtime с 3:49 до 7:50 за 5 дней, Web Fit дал >10 минут ([Blumgi](https://blumgi.games/how-my-15-year-old-son-gave-me-a-game-making-lesson/)).
- Неудачный Blumgi Chase был слишком требователен к навыку: игроки не понимали управление/цель; автор также признал overscope и поздний prototype validation ([Blumgi](https://blumgi.games/ive-killed-my-first-blumgi-game/)).
- Cannon Clash: 2.4 MB, 76 requests и 81% C2P; intro-video удалили, игрок начинает у core mechanic ([Elanra Studios](https://poki.com/blog/how-we-made-cannon-clash-load-fast-and-boosted-conversion)).
- Vortella’s: текстовый modal терял около половины аудитории; упрощение controls подняло типичную сессию примерно с 2 до 4–5 минут до релиза. Средняя сессия на релизе была 6:28, а после последующих content/multiplayer updates выросла примерно до 12:00–12:40 ([Devortel](https://poki.com/blog/i-quit-my-job-to-make-a-dress-up-web-game-and-it-blew-up)).
- OnRush исправил проблему ввода/фокуса и сообщил рост engagement примерно с 2 до 10 минут; полезный пример силы одной найденной UX-причины, но не обещание такого uplift ([Poki blog / OnRush](https://poki.com/blog/higher-success-rates-with-playtests)).

Числа кейсов относятся к отдельным играм и не являются обещанием результата Serendipity Games.
