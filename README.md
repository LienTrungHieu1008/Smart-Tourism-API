# Smart Tourism API — Gợi ý Địa điểm Du lịch bằng Semantic Search

## Thông tin sinh viên

| Thông tin | Chi tiết |
|-----------|----------|
| **Họ và tên** | `Liên Trung Hiếu` |
| **MSSV** | `24120049` |
| **Lớp** | `24CTT3` |
| **Môn học** | Thiết kế và Triển khai API |
| **Giảng viên** | `Lê Đức Khoan` |

---

## Mô hình AI sử dụng

| Thông tin | Chi tiết |
|-----------|----------|
| **Tên mô hình** | `all-MiniLM-L6-v2` |
| **Hugging Face** | [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) |
| **Loại** | Sentence Transformer — mã hóa văn bản thành vector 384 chiều |
| **Ứng dụng** | Tính toán độ tương đồng ngữ nghĩa (Cosine Similarity) giữa câu truy vấn và mô tả địa điểm |

---

## Mô tả hệ thống

Hệ thống **Smart Tourism API** là một RESTful API được xây dựng bằng **FastAPI**, sử dụng thuật toán **Semantic Search** để gợi ý địa điểm du lịch Việt Nam phù hợp với yêu cầu của người dùng.

### Chức năng chính:
- **Tìm kiếm ngữ nghĩa**: Người dùng nhập mô tả (ví dụ: *"bãi biển đẹp"*, *"chùa cổ kính"*), hệ thống trả về các địa điểm phù hợp nhất dựa trên ý nghĩa ngữ nghĩa, không chỉ khớp từ khóa.
- **Kiểm tra sức khỏe server**: Endpoint `/health` cho biết trạng thái hoạt động, thông tin model và số lượng dữ liệu.
- **Sinh lại dữ liệu**: Endpoint `/generate` tạo mới 1000 địa điểm du lịch và cập nhật lại embeddings.
- **Giao diện web**: Trang HTML tĩnh để tương tác trực tiếp với API.

### Quy trình hoạt động:
```
Người dùng nhập query
        ↓
Mã hóa query thành vector (384 chiều) bằng Sentence Transformer
        ↓
Tính Cosine Similarity với 1000 vector địa điểm đã được mã hóa sẵn
        ↓
Trả về top_k địa điểm có điểm tương đồng cao nhất
```

---

## Hướng dẫn cài đặt

### 1. Yêu cầu hệ thống
- Python >= 3.10
- pip (trình quản lý thư viện Python)

### 2. Clone dự án
```bash
git clone <URL_REPO>
cd API
```

### 3. Tạo môi trường ảo (khuyến nghị)
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 4. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

Danh sách thư viện trong `requirements.txt`:
| Thư viện | Mục đích |
|----------|----------|
| `fastapi>=0.100.0` | Framework xây dựng API |
| `uvicorn[standard]>=0.22.0` | ASGI server chạy FastAPI |
| `pydantic>=2.0.0` | Validate dữ liệu đầu vào/đầu ra |
| `sentence-transformers>=2.2.2` | Mô hình AI mã hóa văn bản thành vector |
| `torch>=2.0.0` | Thư viện deep learning hỗ trợ tính toán tensor |
| `requests>=2.31.0` | Gọi HTTP API (dùng cho file kiểm thử) |

---

## Hướng dẫn chạy chương trình

### 1. Sinh dữ liệu (nếu chưa có file `data.py`)
```bash
python generate_data.py
```
> Tạo file `data.py` chứa 1000 địa điểm du lịch Việt Nam.

### 2. Khởi chạy server
```bash
uvicorn main:app --reload
```
> Server sẽ chạy tại: **http://127.0.0.1:8000**

### 3. Truy cập
- **Giao diện web**: http://127.0.0.1:8000
- **API Docs (Swagger)**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

### 4. Chạy kiểm thử
```bash
# Mở terminal khác (giữ server đang chạy)
python test_api.py
```

---

## Hướng dẫn gọi API

### 1. `GET /health` — Kiểm tra sức khỏe server

**Request:**
```bash
curl http://127.0.0.1:8000/health
```

**Response (200 OK):**
```json
{
    "status": "healthy",
    "model_name": "all-MiniLM-L6-v2",
    "total_destinations": 1000,
    "embedding_dimensions": 384,
    "message": "Server đang hoạt động bình thường."
}
```

---

### 2. `POST /suggest` — Tìm kiếm địa điểm du lịch

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/suggest \
  -H "Content-Type: application/json" \
  -d '{"query": "bãi biển đẹp", "top_k": 3}'
```

**Tham số:**
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---------|------|----------|-------|
| `query` | string | Có | Câu mô tả tìm kiếm (min 1 ký tự) |
| `top_k` | int | Không | Số kết quả trả về (mặc định: 3, tối đa: 10) |

**Response (200 OK):**
```json
[
    {
        "id": 14,
        "name": "Bãi biển Mỹ Khê",
        "description": "Một trong những bãi biển đẹp nhất hành tinh ở Đà Nẵng với cát trắng mịn, nước biển trong xanh và sóng nhẹ.",
        "score": 0.7845
    },
    {
        "id": 8,
        "name": "Mũi Né",
        "description": "Bãi biển nổi tiếng ở Bình Thuận với đồi cát bay, lướt ván diều và hoàng hôn tuyệt đẹp trên biển.",
        "score": 0.6912
    },
    {
        "id": 4,
        "name": "Đảo Phú Quốc",
        "description": "Hòn đảo ngọc ở Kiên Giang với cát trắng, bãi biển xanh, lặn ngắm san hô và hải sản tươi ngon tuyệt vời.",
        "score": 0.6503
    }
]
```

**Các lỗi có thể xảy ra:**

| Status Code | Nguyên nhân |
|-------------|-------------|
| `400` | Query chỉ chứa khoảng trắng |
| `404` | Không tìm thấy địa điểm phù hợp |
| `422` | Dữ liệu đầu vào không hợp lệ (thiếu query, top_k ngoài phạm vi) |
| `500` | Lỗi hệ thống |

---

### 3. `POST /generate` — Sinh lại dữ liệu

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/generate
```

**Response (200 OK):**
```json
{
    "status": "success",
    "total_generated": 1000,
    "time_seconds": 7.35,
    "message": "Đã tạo thành công 1000 địa điểm và cập nhật embeddings trong 7.35s."
}
```

---

### 4. Ví dụ gọi API bằng Python (thư viện `requests`)

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# 1. Kiểm tra health
resp = requests.get(f"{BASE_URL}/health")
print(resp.json())

# 2. Tìm kiếm địa điểm
resp = requests.post(f"{BASE_URL}/suggest", json={
    "query": "núi cao sương mù",
    "top_k": 5
})
for dest in resp.json():
    print(f"{dest['name']} — Score: {dest['score']}")

# 3. Sinh lại dữ liệu
resp = requests.post(f"{BASE_URL}/generate")
print(resp.json())
```

---

## Video Demo

> [Link video demo](<Điền link video demo tại đây>)

---

## Cấu trúc dự án

```
API/
├── main.py              # File chính — định nghĩa các endpoint FastAPI
├── data.py              # Dữ liệu 1000 địa điểm du lịch (auto-generated)
├── generate_data.py     # Script sinh dữ liệu địa điểm
├── test_api.py          # File kiểm thử API bằng thư viện requests
├── requirements.txt     # Danh sách thư viện cần cài đặt
├── README.md            # Tài liệu hướng dẫn (file này)
└── static/
    └── index.html       # Giao diện web tĩnh
```
