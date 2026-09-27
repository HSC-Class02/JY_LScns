# LS전선 OpenDART 재무 분석 대시보드

<a href="https://hsc-class02.github.io/JY_LScns/"><img src="assets/ls-cable-logo.png" alt="🔗 LS전선 대시보드 바로가기" width="145"></a>

### [🔗 대시보드 바로가기](https://hsc-class02.github.io/JY_LScns/)

LS전선(LS Cable & System, DART 고유번호 `00683283`)의 사업보고서·반기보고서·분기보고서를 2010년부터 OpenDART에서 수집하고, 핵심 재무수치와 재무비율을 정리하는 자동화 프로젝트입니다.

## 대시보드

**🔗 [대시보드 바로가기](https://hsc-class02.github.io/JY_LScns/)**

상단은 핵심 KPI와 추세 그래프, 하단은 Annual / Half-year / Quarterly 재무 테이블과 국내 Peer firms 표로 구성됩니다. 오른쪽 플로팅 메뉴에서 대시보드 화면을 PDF로 출력하거나, 기간(연간·반기·분기)을 선택해 전체 재무데이터를 Excel(`.xlsx`)로 내려받을 수 있습니다. 데이터가 처음에는 비어 있을 수 있으며, API 키를 등록한 뒤 Actions에서 한 번 실행하면 채워집니다.

## 제공 범위

- 수집 기간: 2010년 1월 1일 이후
- 보고서: 사업보고서(`11011`), 반기보고서(`11012`), 1분기(`11013`), 3분기(`11014`)
- 주요 수치: 매출액, 매출원가, 매출총이익, 영업이익, 법인세차감전이익, 당기순이익, 자산·부채·자본, 현금, 매출채권, 재고자산, 영업현금흐름, CAPEX
- 재무비율: 성장률, 매출총/영업/순이익률, ROA, ROE, 유동·당좌비율, 부채비율, 재고회전율, DSO, CFO 전환율, FCF
- GitHub Actions: 매월 1일 09:00 KST 자동 갱신 및 GitHub Pages 재배포

## 국내 Peer firms

Peer는 **사업 중첩도**, **지배관계**, **상장 여부 및 재무자료 접근성**을 함께 고려해 분류했습니다. 아래 내용은 2026년 9월 기준이며, LS전선의 주요 사업인 초고압·해저·배전·통신·산업용 케이블과의 중첩도를 기준으로 합니다.

| 분류 | 기업 | LS전선과 겹치는 주요 사업 | 비교 시 유의사항 |
| --- | --- | --- | --- |
| **Core peer** | [대한전선](https://www.taihan.com/) | 초고압·전력·해저케이블 및 시공 솔루션 | 국내 독립 상장사 중 사업 중첩도가 가장 높아 핵심 비교기업으로 적합 |
| **Partial direct peer** | [일진전기](https://www.iljinelectric.co.kr/main?lang=ko) | 초고압·중저압 전력케이블, 접속재 및 전력 인프라 | 변압기·차단기 등 중전기 사업 비중이 있어 케이블 기업 간 마진 비교 시 사업부 구성을 고려해야 함 |
| **Secondary listed peer** | [대원전선](https://www.daewoncable.co.kr/) | 전력·통신·자동차용 전선 | 범용·중저압 제품 비중과 기업 규모 차이가 커 보조 비교기업으로 활용 |
| **Affiliate / operating benchmark** | [가온전선](https://www.gaoncable.com/) | 전력·통신·특수케이블 및 배전 솔루션 | LS전선(주) 외 1인이 81.63%를 보유한 계열사(2025년 말 기준)이므로 독립적인 가치평가 Peer에서는 제외하고 제품 믹스·운영지표 비교에 활용 |
| **Specialist benchmark** | [극동전선 (Lynxeo Korea)](https://www.lynxeogroup.com/ko/) | 선박·해양, 철도, 자동차 및 산업용 특수 케이블 | 비상장 해외계열 법인으로 공개 재무자료가 제한적이므로 특수 케이블 사업 비교에 한정 |

### Peer 활용 원칙

- **상장사 재무·가치평가 비교군:** 대한전선을 중심으로 일진전기와 대원전선을 보조적으로 사용합니다.
- **사업·제품 비교군:** 가온전선과 극동전선은 제품 포트폴리오 및 시장 노출도 비교에 활용합니다.
- 가온전선은 LS전선 연결 실적에 포함되는 계열사이므로 LS전선과 단순 병렬 비교하거나 평균 멀티플 계산에 함께 넣지 않습니다.
- 일진전기는 전선과 중전기 사업을 함께 영위하므로 가능하면 전체 회사 수치보다 사업부문별 매출과 이익을 확인합니다.
- 극동전선은 Lynxeo의 한국 특수 케이블 생산 거점이므로 초고압·해저 전력망 Peer보다는 산업용 특수 케이블 Peer에 가깝습니다.

분류 근거: [LS전선 사업영역](https://www.lscns.co.kr/kr/intro/overview.asp), [대한전선 해저케이블 사업](https://www.taihan.com/news/pr/releaseDetail?idx=424), [일진전기 사업영역](https://www.iljinelectric.co.kr/main?lang=ko), [가온전선 경영정보](https://www.gaoncable.com/company/business), [Lynxeo 사업영역](https://www.lynxeogroup.com/ko/company/what-we-do.html)

## API 키 설정

1. [OpenDART](https://opendart.fss.or.kr/)에서 인증키를 발급받습니다.
2. GitHub 저장소에서 **Settings → Secrets and variables → Actions → New repository secret**으로 이동합니다.
3. Name에 `DART_API_KEY`, Secret에 발급받은 키를 넣습니다.
4. **Settings → Pages → Build and deployment → Source**를 `GitHub Actions`로 선택합니다.
5. **Actions → Update OpenDART data and deploy dashboard → Run workflow**를 한 번 실행합니다.

키는 저장소나 ZIP에 넣지 않습니다. 자세한 내용은 [API_KEY_SETUP.txt](API_KEY_SETUP.txt)를 참고하세요.

## ZIP 배포본

`python scripts/build_zip.py`를 실행하면 `LS_Cable_OpenDART_Agent.zip`이 생성됩니다. ZIP은 `.env`, `.git`, `.github`, `__pycache__` 같은 숨김 파일/폴더를 포함하지 않습니다. ZIP을 푼 뒤 `install_github_workflow.ps1`을 실행하면 필요한 GitHub Actions 파일을 `.github/workflows`에 설치합니다.

## 로컬 실행

```powershell
Copy-Item env.example.txt .env
# .env의 DART_API_KEY= 뒤에 인증키 입력
python -m pip install -r requirements.txt
python scripts/fetch_opendart.py --start-year 2010
python scripts/analyze.py
python -m http.server 8000
```

브라우저에서 `http://localhost:8000`을 열면 대시보드를 확인할 수 있습니다. 이 프로젝트는 정보 제공 목적이며 투자 권유가 아닙니다.
