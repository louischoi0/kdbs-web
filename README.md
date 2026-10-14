<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo/kdbs-logo-dark.svg">
    <img src="assets/logo/kdbs-logo.svg" alt="KDBS" width="360">
  </picture>
</p>

# kdbs-web

KDBS 웹사이트 저장소입니다.

## 브랜드

### 로고

| 파일 | 용도 |
|---|---|
| `assets/logo/kdbs-logo.svg` | 심볼 + 워드마크, 밝은 배경용 |
| `assets/logo/kdbs-logo-dark.svg` | 심볼 + 워드마크, 어두운 배경용 |
| `assets/logo/kdbs-logo-vertical.svg` | 세로형 (심볼 위, 워드마크 아래), 밝은 배경용 |
| `assets/logo/kdbs-logo-vertical-dark.svg` | 세로형, 어두운 배경용 |
| `assets/logo/kdbs-logo-vertical.png`, `kdbs-logo-vertical-dark.png` | 세로형 PNG (너비 1024px, 투명 배경) |
| `assets/logo/kdbs-symbol.svg` | 심볼 단독, 밝은 배경용 |
| `assets/logo/kdbs-symbol-dark.svg` | 심볼 단독, 어두운 배경용 |

워드마크는 Sora Bold 기반이며, 서체 설치 없이 동일하게 표시되도록 외곽선(path)으로 변환되어 있습니다.

### 프로필 아이콘

GitHub, X, LinkedIn 등 프로필 사진용 아이콘입니다. 파비콘과 같은 단순화 심볼에 배경을 채웠습니다. 원형으로 잘려도 심볼이 온전히 보이도록 여백을 두었습니다.

| 파일 | 용도 |
|---|---|
| `assets/profile/kdbs-profile.svg` | 흰 배경 (기본) |
| `assets/profile/kdbs-profile-dark.svg` | 잉크 네이비 배경 |

SVG 업로드를 지원하지 않는 서비스에는 PNG를 씁니다. X용 400×400 PNG: `kdbs-profile-x.png`, `kdbs-profile-dark-x.png`.

### 파비콘

작은 크기에서도 형태가 뭉개지지 않도록 날개깃을 3개로 줄이고 두께를 키운 단순화 심볼을 사용합니다. 파일은 `assets/favicon/`에 있습니다.

| 파일 | 용도 |
|---|---|
| `favicon.svg` | 브라우저 탭 (다크 모드에서 하단 깃이 흰색으로 전환) |
| `favicon.ico` | 구형 브라우저용 (16·32·48px) |
| `apple-touch-icon.png` | iOS 홈 화면 (180px) |
| `icon-192.png`, `icon-512.png`, `icon-maskable-512.png` | PWA / Android |
| `site.webmanifest` | 웹 앱 매니페스트 |

사이트 배포 시 파일을 웹 루트에 두고 `<head>`에 다음을 추가합니다.

```html
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
```

### 컬러

| 이름 | HEX | 용도 |
|---|---|---|
| 키컬러 (레드 오렌지) | `#E8380D` | 심볼, 강조 요소 |
| 포인트 컬러 (잉크 네이비) | `#14213D` | 워드마크, 텍스트, 어두운 배경 |

## 디자인 시스템

`design-system/` 폴더에 웹사이트·문서·콘솔이 함께 쓰는 토큰과 컴포넌트 CSS가 있습니다.

| 파일 | 내용 |
|---|---|
| `tokens.json` | 토큰 원본 (컬러 라이트/다크, 타이포, 간격, 라운드, 그림자) |
| `tokens.css` | `tokens.json`에서 생성한 CSS 변수와 `@font-face`. **직접 수정하지 않습니다.** |
| `components.css` | 컴포넌트 클래스 (`kd-btn`, `kd-input`, `kd-badge`, `kd-card`, `kd-code`, `kd-callout`, `kd-table`) |
| `fonts/` | Sora, Pretendard, JetBrains Mono 가변 폰트와 라이선스(SIL OFL 1.1) |
| `build_css.py` | `tokens.json` → `tokens.css` 생성 스크립트 |

### 사용법

```html
<link rel="stylesheet" href="/design-system/tokens.css">
<link rel="stylesheet" href="/design-system/components.css">

<body class="kd-root">
  <button class="kd-btn kd-btn--primary" type="button">쿼리 실행</button>
</body>
```

- 테마는 시스템 설정(라이트/다크)을 자동으로 따릅니다. 고정하려면 `<html data-theme="light">` 또는 `data-theme="dark"`를 지정합니다.
- 텍스트 스타일은 `kd-type-body`, `kd-type-heading-1`처럼 클래스로 적용합니다.
- 색은 `var(--text)`, `var(--surface)`, `var(--accent-strong)` 같은 시맨틱 토큰만 씁니다. `--brand-*`, `--ink-*` 원시 스케일은 직접 쓰지 않습니다.

### 토큰 수정

`tokens.json`을 고친 뒤 다음을 실행해 `tokens.css`를 다시 생성합니다.

```sh
python3 design-system/build_css.py
```
