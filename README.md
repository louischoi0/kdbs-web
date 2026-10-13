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
| `assets/logo/kdbs-symbol.svg` | 심볼 단독, 밝은 배경용 |
| `assets/logo/kdbs-symbol-dark.svg` | 심볼 단독, 어두운 배경용 |

워드마크는 Sora Bold 기반이며, 서체 설치 없이 동일하게 표시되도록 외곽선(path)으로 변환되어 있습니다.

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
