# Технические требования к Poki-build

## 1. Пакет игры

### Подтверждённые требования

- Нужна web/HTML5-сборка с `index.html` ([Adding your game](https://developers.poki.com/guide/adding-your-game), [Poki Inspector](https://developers.poki.com/guide/inspector)).
- Inspector принимает папку игры; P4D/официальный CLI загружает содержимое build-directory. Безопасная структура — один `index.html` в корне пакета, рядом локальные assets ([официальный poki-cli](https://github.com/poki/poki-cli)).
- В production-интерфейсе P4D на дату проверки **9 сентября 2026 года** валидатор сообщает: максимум 10 000 файлов, 100 MB на файл, 1 GB несжатого содержимого ZIP, без executable-файлов ([production bundle P4D](https://app.poki.dev/app.9e229c21.js)). Это хешированный и потенциально нестабильный URL; лимиты **не продублированы в публичном Developer Guide**, поэтому их нужно перепроверить перед большой загрузкой.

### Цель производительности, а не upload-limit

Poki рекомендует для хорошей web-игры не более **5 MB initial download** и примерно **8 MB total**. Игроки часто уходят, если загрузка занимает более 10 секунд; критический контент нужно грузить первым, остальное — прогрессивно ([выбор web-движка](https://developers.poki.com/guide/web-engine), [Easy access & onboarding](https://developers.poki.com/guide/easy-access), [Requirements](https://developers.poki.com/guide/requirements-quality)).

## 2. Экран, устройства и управление

Опубликованные platform requirements и UI expectations:

- desktop, mobile и tablet;
- на mobile заполнить игровую область в portrait, landscape или обоих режимах;
- планшету автоматически давать mobile-controls;
- 16:9 и пропорциональное покрытие canvas; Poki называет контрольные размеры `640×360`, `836×470`, `1031×580`;
- responsive UI для разных размеров и способов ввода;
- не позволять стрелкам, пробелу и колесу прокручивать родительскую страницу;
- для keyboard-controlled игр поддержать pause/resume через `Esc` или `Space` и корректные SDK events.

Источник: [Requirements](https://developers.poki.com/guide/requirements-quality), [HTML5 SDK](https://developers.poki.com/guide/sdk-html5).

Poki сообщает, что аудитория преимущественно мобильная и советует поддержать portrait: у таких игр в среднем выше вход в gameplay и появляется право на Gamebar Display ads ([What we look for](https://developers.poki.com/guide/what-we-look-for), [Easy access](https://developers.poki.com/guide/easy-access)). Это рекомендация, не запрет landscape-only.

## 3. Poki SDK: минимальная интеграция

Для HTML5 SDK подключается в `<head>`:

```html
<script src="https://game-cdn.poki.com/scripts/v2/poki-sdk.js"></script>
```

Инициализация не должна блокировать игру при ошибке:

```js
PokiSDK.init().then(startGame).catch(startGame);
```

Основные события:

| Событие | Когда вызывать |
|---|---|
| `gameLoadingFinished()` | обязательная загрузка закончена, можно показать меню/первый playable screen |
| `gameplayStart()` | первое реальное действие игрока, начало уровня, unpause |
| `gameplayStop()` | pause, меню, конец уровня, смерть, cutscene, уход из gameplay |
| `commercialBreak()` | естественная пауза перед подтверждённым возвратом в gameplay |
| `rewardedBreak()` | только после явного выбора игроком рекламной награды |

Правила состояния:

- первый `gameplayStart()` — на первом вводе, не на загрузке;
- не отправлять `start → start` или `stop → stop`;
- при любой остановке gameplay отправить `gameplayStop()`;
- во время рекламы не давать событиям игры срабатывать;
- звук и keyboard input выключить до/на время рекламы, восстановить после завершения Promise.

Типовые последовательности:

```text
Старт:             gameLoadingFinished → gameplayStart
Смерть/restart:    gameplayStop → commercialBreak → gameplayStart
Смерть/revive:     gameplayStop → rewardedBreak → gameplayStart
Следующий уровень: gameplayStop → commercialBreak → gameplayStart
Pause/resume:      gameplayStop → commercialBreak → gameplayStart
```

Источники: [SDK overview](https://developers.poki.com/guide/sdk-overview), [HTML5 SDK](https://developers.poki.com/guide/sdk-html5), [Requirements](https://developers.poki.com/guide/requirements-quality).

## 4. Реклама

### Commercial break

- Сигналить в естественной паузе, когда пользователь собирается продолжить игру.
- Правильно: restart, next level, выход из pause обратно в игру.
- Неправильно: переход из игры в level select/другое меню.
- Не каждый вызов показывает рекламу; решение и частота принадлежат Poki.
- Не создавать собственные рекламные таймеры/cooldowns.
- Безопасная интерпретация SDK flow: не ставить рекламу до первого gameplay; отдельным hard requirement это не опубликовано.

### Rewarded break

- Игрок заранее понимает, что нажимает кнопку видео.
- Награда выдаётся только при `success === true`.
- Основной прогресс не может быть закрыт рекламой.
- Обычная альтернатива показывается одновременно, не меньше по размеру и рядом/выше.
- Rewarded-кнопка не зелёная и содержит заметный значок видео `🎬`.
- Не требовать несколько роликов за одну награду, не выдавать награду дважды.
- При ad blocker награду не выдавать и не показывать собственное предупреждение.

IAP и сторонние рекламные системы на Poki не поддерживаются; монетизация идёт через Poki SDK ([Monetization overview](https://developers.poki.com/guide/how-monetization-works), [Requirements](https://developers.poki.com/guide/requirements-quality)).

## 5. Сохранения, incognito и аккаунт

- Игра остаётся playable в incognito; обращения к `localStorage` оборачиваются в `try/catch`.
- Если долгосрочный прогресс уместен, его сохраняют; иначе игрока явно предупреждают, что прогресс исчезнет после выхода.
- Если User Accounts доступны, вошедший пользователь не отказался от синхронизации и лимит не превышен, SDK автоматически синхронизирует `localStorage` и IndexedDB; лимит cloud save — 1 MB после gzip.
- Данные, которые не нужно синхронизировать, получают префикс `poki_ignore`: это относится к ключам `localStorage`, object stores IndexedDB и row keys.
- Login не вызывают автоматически на старте — только после действия игрока.
- Token живёт 1 минуту, не хранится и проверяется backend-ом; Team API key нельзя включать в клиент.

Источник: [User Accounts](https://developers.poki.com/guide/accounts), [Requirements](https://developers.poki.com/guide/requirements-quality).

## 6. Внешние запросы, CSP и privacy

По умолчанию внешние запросы заблокированы ([External resources policy](https://developers.poki.com/guide/external-resources-policy)).

Нельзя:

- грузить Google Fonts, картинки, аудио или библиотеки с внешнего CDN во время игры;
- использовать внешний email/social login или собирать идентифицирующую информацию;
- добавлять игровой chat;
- использовать Google Analytics/другие Google analytics products.

После индивидуального одобрения возможны multiplayer servers, отдельные analytics providers и leaderboard backends. Для пользовательских multiplayer-имён нужен profanity filter. Порядок:

1. `Settings → CSP` в P4D;
2. точные URL/домены и объяснение назначения;
3. публичная актуальная privacy policy на живой странице, не в Google Docs; ссылка на неё внутри игры;
4. повторная загрузка билда после одобрения для сброса cache.

Ненужные исходящие ссылки следует удалить. Если согласованная с Poki ссылка остаётся, её кнопка обязана использовать `PokiSDK.openExternalLink('URL')`.

## 7. UX и onboarding

- минимизировать или пропустить splash, title, menu и level-select до первого gameplay;
- убрать чужой splash/outgoing branding; собственный studio logo допустим на loading screen;
- visual tutorial вместо стены английского текста;
- первые уровни безопасные и легко проходимые;
- действия вводятся постепенно;
- cutscenes и intro можно пропустить;
- показана правильная схема управления для текущего устройства;
- локализовать интерфейс и предпочтительно определять язык браузера автоматически;
- short, satisfying, repeatable loop около 3 минут; Poki советует концентрироваться примерно на часе сильного контента, а не на огромной mobile-прогрессии ([Engagement](https://developers.poki.com/guide/engagement), [Easy access](https://developers.poki.com/guide/easy-access)).

## 8. Встроенные игровые события

`PokiSDK.measure(category, what, action)` полезен для воронок:

- progression: `start`, затем ровно одно `complete` или `fail`;
- UI/reward offer: `visible`, затем `interact`;
- имена стабильны между версиями;
- символы `/` и `^` не использовать;
- не дублировать ad impression/completion — они считаются SDK автоматически.

Пример:

```js
PokiSDK.measure('tutorial', 'movement', 'start');
PokiSDK.measure('tutorial', 'movement', 'complete');
PokiSDK.measure('rewarded', 'revive', 'visible');
PokiSDK.measure('rewarded', 'revive', 'interact');
```

Источник: [Game Events](https://developers.poki.com/guide/game-events).

## 9. QA-чеклист

- [ ] Один корневой `index.html`, clean production build, без debug/test artifacts.
- [ ] Initial download целится в ≤5 MB, total — ≤8 MB; остальное грузится прогрессивно.
- [ ] Loading bar/арт показывают прогресс, нет пустого экрана.
- [ ] Desktop: keyboard + mouse; mobile/tablet: touch controls; нужные orientation/resize.
- [ ] 16:9 scaling проверен на `640×360`, `836×470`, `1031×580`.
- [ ] Родительская страница не скроллится от игрового ввода.
- [ ] Incognito, ad blocker и отказ `PokiSDK.init()` не ломают игру.
- [ ] SDK event log пройден по start, pause, death, restart, next level, rewarded success/failure.
- [ ] Звук и ввод выключены во время рекламы.
- [ ] External Resources, Image Optimization и Unexpected Behavior warnings устранены.
- [ ] Проверен настоящий телефон через QR и хотя бы один слабый mobile device.
- [ ] Нет сторонней рекламы, покупки/`no ads`, чужого account SDK или прямых внешних ссылок.
- [ ] Нет обхода ad blocker и собственного сообщения о нём.
- [ ] Static thumbnail готова к Player Fit; animated thumbnail добавлена в Soft Release и готова до Global Release.
- [ ] Сохранения работают либо ограничение объяснено игроку.

Главный инструмент: [Poki Inspector](https://inspector.poki.dev/); из P4D он также открывается с уже загруженной версией.

## Не опубликовано

В текущих публичных материалах не найдены: минимальные версии браузеров, обязательный FPS/memory/draw-call threshold, формальная политика для `blur`/`visibilitychange`, максимальная длина URL/пути, полный список запрещённых executable extensions, SLA build review и отдельное требование cookie banner/consent для игры без одобренных внешних сервисов. При подключении одобренной аналитики обязанности остаются provider/privacy-specific. Это нельзя дописывать «по опыту других порталов».
