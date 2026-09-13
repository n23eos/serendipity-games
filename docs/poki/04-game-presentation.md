# Оформление игры на Poki

## Название

Poki не публикует формулу оценки названия или A/B-инструмент для него. Практически лучше:

- короткое, произносимое и легко набираемое имя;
- одна стабильная английская версия во всех полях и assets;
- имя отражает fantasy/mechanic, но не копирует поисковое имя чужого хита;
- заранее проверить торговые марки, домены/поиск и уже существующие игры;
- не использовать намеренно похожее название для перехвата поиска — Poki относит это к признакам клона ([Content & player safety](https://developers.poki.com/guide/content-player-safety)).

Внешний пример: Vortina’s Boutique переименовали из-за SEO и трудного написания `boutique`; это единичный кейс, не официальное правило ([история Devortel](https://poki.com/blog/i-quit-my-job-to-make-a-dress-up-web-game-and-it-blew-up)).

## Категории и описание

- В P4D разработчик предлагает до четырёх категорий; Poki может изменить или дополнить их, чтобы найти подходящую аудиторию.
- В описании нужно кратко назвать главную механику и отличие игры.
- Poki использует текст разработчика как input, затем приводит описание к своему SEO-формату ([P4D platform](https://developers.poki.com/guide/p4d-platform)).

Рабочая формула pitch:

> `[Game] is a [genre] where players [core action] to [immediate goal]. Unlike [broad category norm], it [one concrete twist]. Built for instant mobile and desktop web play, it supports [replay/update hook].`

Не обещать функции, которых нет в тестовом билде.

## Статичная thumbnail

Thumbnail — главный фактор CTR на Poki ([Game thumbnail](https://developers.poki.com/guide/game-thumbnail)).

Обязательное/конкретное:

- квадрат 1:1, full bleed;
- минимум `628×628 px`;
- без рамок, padding и letterbox;
- читается в маленькой плитке;
- избегать фона, сливающегося с Poki `#83FFE7`;
- требуется для Player Fit Test.

Рекомендации Poki:

- один главный объект: основной персонаж в стандартном скине или ключевой gameplay element;
- простой фон и высокий контраст;
- динамичная поза/движение;
- без title/текста;
- art style и обещание точно совпадают с игрой;
- для серии — визуально родственная система обложек.

Thumbnail в основном двигает CTR. C2P зависит прежде всего от загрузки, responsiveness и pre-play experience; ложная обложка дополнительно ухудшает переход и playtime.

## Анимированная thumbnail

Добавляется и тестируется во время Soft Release; обязательна до Global Release ([Your game page](https://developers.poki.com/guide/your-game-page)).

| Параметр | Требование |
|---|---|
| Размер | `1080×1080` или больше |
| Aspect ratio | 1:1 |
| FPS | 50+ |
| Длительность | 4–6 секунд |
| Звук | muted |
| Формат | `.mp4` |
| Максимум | 100 MB |

Содержание:

- core mechanic и самые сильные моменты;
- 2–3 сцены по 1–2 секунды;
- минимум текста и несущественного UI;
- действие в центре с учётом квадратного crop;
- курсор удалён;
- желательно плавно продолжать статичную картинку.

## Первые 60 секунд — часть оформления

Poki оценивает первое впечатление шире обложки. После клика:

- нет обязательного ролика и лишнего меню;
- игрок быстро совершает core action;
- tutorial визуальный и пошаговый;
- первые успех и награда приходят рано;
- controls соответствуют touch/keyboard;
- обещание thumbnail сразу подтверждается экраном игры.

Кейсы это поддерживают: Cannon Clash удалил intro-video, посадил игрока сразу к пушке и получил 81% C2P при 2.4 MB/76 запросах ([Elanra Studios](https://poki.com/blog/how-we-made-cannon-clash-load-fast-and-boosted-conversion)); у Vortella’s Dress Up половина пользователей уходила на текстовом modal даже при множестве переводов ([Devortel](https://poki.com/blog/i-quit-my-job-to-make-a-dress-up-web-game-and-it-blew-up)). Это наблюдения конкретных игр, не универсальные гарантии.

## Локализация

Poki рекомендует:

1. EFIGS: English, French, Italian, German, Spanish; в первую волну также Turkish;
2. Simplified Chinese, Japanese, Korean;
3. Brazilian Portuguese и Russian.

Для text-heavy игр строки нужно заранее вынести в единый ресурс, интерфейс — подготовить к длинным переводам, а язык лучше определять по браузеру ([Localization](https://developers.poki.com/guide/localization)). Ручной переключатель в дополнение к автоопределению — наша рекомендация; Poki допускает toggle, но не требует сочетать оба подхода.

Практический приоритет:

- сначала понятный без текста core loop;
- затем качественный English build;
- затем EFIGS + Turkish;
- расширять по данным и бюджету.

В кейсе Vortella’s локализация примерно на восемь языков не компенсировала плохой onboarding с блокирующим текстовым modal.

## Мини-пакет материалов на игру

- [ ] окончательное английское название;
- [ ] one-line hook до 140 символов;
- [ ] описание: mechanic + goal + distinction;
- [ ] до четырёх предложенных категорий;
- [ ] input map для desktop/mobile/tablet;
- [ ] square static thumbnail ≥628 px без текста;
- [ ] позднее: 1080 px, 50+ fps, 4–6 s muted MP4;
- [ ] перечень языков и fallback;
- [ ] update roadmap на 2–3 существенных обновления;
- [ ] список прав/лицензий и AI provenance;
- [ ] ссылка на privacy policy, если есть одобренные внешние сервисы.
