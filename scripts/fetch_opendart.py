"""Fetch LS Cable periodic filings and financial statements from OpenDART."""
from __future__ import annotations
import argparse, datetime as dt, json, os, pathlib, zipfile, io
import requests

ROOT = pathlib.Path(__file__).resolve().parents[1]
CORP_CODE = "00683283"  # LS Cable & System
REPORTS = {"11011": "annual", "11012": "half_year", "11013": "quarterly", "11014": "quarterly"}

def api_key():
    key = os.getenv("DART_API_KEY", "")
    if not key and (ROOT / ".env").exists():
        for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
            if line.startswith("DART_API_KEY="): key = line.split("=", 1)[1].strip()
    if not key: raise SystemExit("DART_API_KEY가 없습니다. API_KEY_SETUP.txt를 확인하세요.")
    return key

def get_json(path, params):
    response = requests.get("https://opendart.fss.or.kr/api/" + path, params=params, timeout=60)
    response.raise_for_status(); return response.json()

def main(start_year: int):
    key = api_key(); raw = ROOT / "data" / "raw"; raw.mkdir(parents=True, exist_ok=True)
    source = ROOT / "reports" / "source"; source.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().strftime("%Y%m%d"); disclosures = []
    for year in range(start_year, dt.date.today().year + 1):
        listing = get_json("list.json", {"crtfc_key":key,"corp_code":CORP_CODE,"bgn_de":f"{year}0101","end_de":today,"pblntf_ty":"A","page_count":100})
        for item in listing.get("list", []):
            name = item.get("report_nm", "")
            if any(x in name for x in ("사업보고서", "반기보고서", "분기보고서")) and "정정" not in name:
                disclosures.append(item)
                rcept = item["rcept_no"]; out = source / f"{rcept}.zip"
                if not out.exists():
                    blob = requests.get("https://opendart.fss.or.kr/api/document.xml", params={"crtfc_key":key,"rcept_no":rcept}, timeout=120).content
                    if blob.startswith(b"PK"): out.write_bytes(blob)
        for code, category in REPORTS.items():
            out = raw / f"lscns_{year}_{code}.json"
            if out.exists(): continue
            data = get_json("fnlttSinglAcntAll.json", {"crtfc_key":key,"corp_code":CORP_CODE,"bsns_year":str(year),"reprt_code":code,"fs_div":"CFS"})
            if data.get("status") != "000":
                data = get_json("fnlttSinglAcntAll.json", {"crtfc_key":key,"corp_code":CORP_CODE,"bsns_year":str(year),"reprt_code":code,"fs_div":"OFS"})
            data.update({"year":year,"reprt_code":code,"category":category,"corp_code":CORP_CODE})
            out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "reports" / "opendart_disclosures.json").write_text(json.dumps(disclosures, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--start-year", type=int, default=2010)
    main(parser.parse_args().start_year)
