import os
import requests

list_file = "fileditch_keepalive_list.txt"

if not os.path.exists(list_file):
    print(f"❌ 找不到續命清單檔案: {list_file}")
    exit(0)

with open(list_file, "r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

print(f"🔍 讀取到 {len(urls)} 個需要續命的 FileDitch 檔案網址...")

for idx, url in enumerate(urls, 1):
    try:
        # 發送請求模擬下載瀏覽，觸發伺服器更新存取時間
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) KeepAliveBot/1.0"}
        response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
        
        if response.status_code == 200:
            print(f"[{idx}/{len(urls)}] ✅ 成功續命: {url}")
        else:
            print(f"[{idx}/{len(urls)}] ⚠️ 狀態碼異常 ({response.status_code}): {url}")
    except Exception as e:
        print(f"[{idx}/{len(urls)}] ❌ 續命失敗 {url} | 錯誤: {e}")

print("🎉 所有檔案續命訪問作業執行完畢！")
