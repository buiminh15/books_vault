import os
import json
import re

BOOKS_DIR = './books'
OUTPUT_FILE = './books_data.js'

books = []

if not os.path.exists(BOOKS_DIR):
    os.makedirs(BOOKS_DIR)

for filename in os.listdir(BOOKS_DIR):
    if filename.endswith('.html'):
        filepath = os.path.join(BOOKS_DIR, filename)
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Trích xuất thông tin cơ bản
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = title_match.group(1).replace('Tóm Tắt Sách:', '').replace('Tóm Tắt Chuyên Sâu:', '').strip() if title_match else filename.replace('.html', '')

        # Tìm thể loại qua tag hoặc đoán theo từ khóa
        category = "Phát triển bản thân"
        if any(w in content.lower() for w in ['wyckoff', 'volume', 'chứng khoán', 'cổ phiếu', 'trading', 'đầu tư']):
            category = "Đầu tư & Trading"
        elif any(w in content.lower() for w in ['tư duy', 'mindset', 'thói quen', 'kỷ luật']):
            category = "Tâm lý & Tư duy"

        books.append({
            "title": title,
            "filename": f"books/{filename}",
            "category": category,
            "author": "Chuyên gia / Tác giả",
            "dateAdded": "Gần đây"
        })

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("const BOOKS_DATA = " + json.dumps(books, ensure_ascii=False, indent=2) + ";")

print(f"Đã cập nhật thành công {len(books)} cuốn sách vào thư viện!")