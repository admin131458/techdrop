import json
import random
import os
from datetime import datetime, timezone

def run():
    file_path = "data.json"
    if not os.path.exists(file_path):
        print("未找到 data.json，跳过更新")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 模拟真实市场动态微调波动（实际可在这里调用 requests 爬取真实商品价格）
    for p in data.get("products", []):
        fluctuation = random.choice([-50, 0, 50, 100])
        p["marketPrice"] = max(p["officialMsrp"] - 600, p["marketPrice"] + fluctuation)

    # 记录最新更新时间
    data["updated_at"] = datetime.now(timezone.utc).isoformat()

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"数据更新完成，时间: {data['updated_at']}")

if __name__ == "__main__":
    run()