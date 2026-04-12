# Smart Tourism API — Gợi ý Địa điểm Du lịch bằng Semantic Search

## Thông tin sinh viên

| Thông tin | Chi tiết |
|-----------|----------|
| **Họ và tên** | `Liên Trung Hiếu` |
| **MSSV** | `24120049` |
| **Lớp** | `24CTT3` |
| **Môn học** | Tư Duy Tính Toán |
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
- **Giao diện web**: Trang HTML tĩnh tại `/ui` để tương tác trực tiếp với API.

### Quy trình hoạt động:
```
Người dùng nhập query
        ↓
Mã hóa query thành vector (384 chiều) bằng Sentence Transformer
        ↓
Tính Cosine Similarity với 1000 vector địa điểm đã được mã hóa sẵn
        ↓
Trả về top_k địa điểm có điểm tương đồng cao nhất dưới dạng JSON
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
- **Thông tin API (JSON)**: http://127.0.0.1:8000
- **Giao diện web**: http://127.0.0.1:8000/ui
- **API Docs (Swagger)**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

### 4. Chạy kiểm thử
```bash
# Mở terminal khác (giữ server đang chạy)
python test_api.py
```

---

## Hướng dẫn gọi API

### Các endpoint

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| `GET` | `/` | Thông tin giới thiệu hệ thống |
| `GET` | `/health` | Kiểm tra trạng thái hoạt động |
| `POST` | `/predict` | Nhận dữ liệu đầu vào, gọi mô hình AI, trả kết quả JSON |
| `GET` | `/ui` | Giao diện web tương tác |

---

### 1. `GET /` — Thông tin giới thiệu hệ thống

**Request:**
```bash
curl http://127.0.0.1:8000/
```

**Response (200 OK):**
```json
{
    "system": "Smart Tourism API",
    "description": "Hệ thống gợi ý điểm đến du lịch Việt Nam sử dụng mô hình Sentence Transformer (all-MiniLM-L6-v2) từ Hugging Face để tìm kiếm ngữ nghĩa.",
    "model": "sentence-transformers/all-MiniLM-L6-v2",
    "huggingface_url": "https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2",
    "total_destinations": 1000,
    "endpoints": {
        "GET /": "Thông tin giới thiệu hệ thống",
        "GET /health": "Kiểm tra trạng thái hoạt động",
        "POST /predict": "Gợi ý điểm đến du lịch dựa trên câu truy vấn",
        "GET /ui": "Giao diện web tương tác"
    }
}
```

---

### 2. `GET /health` — Kiểm tra sức khỏe server

**Request:**
```bash
curl http://127.0.0.1:8000/health
```

**Response (200 OK):**
```json
{
    "status": "healthy",
    "model_name": "sentence-transformers/all-MiniLM-L6-v2",
    "model_source": "Hugging Face",
    "total_destinations": 1000,
    "embedding_dimensions": 384,
    "message": "Server đang hoạt động bình thường."
}
```

---

### 3. `POST /predict` — Gợi ý điểm đến du lịch

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"query": "bãi biển đẹp lặn san hô", "top_k": 3}'
```

**Tham số:**
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---------|------|----------|-------|
| `query` | string | Có | Câu mô tả nhu cầu du lịch (min 1 ký tự) |
| `top_k` | int | Không | Số kết quả trả về (mặc định: 5, tối đa: 20) |

**Response (200 OK):**
```json
[
    {
        "id": 4,
        "name": "Đảo Phú Quốc",
        "description": "Hòn đảo ngọc ở Kiên Giang với cát trắng, bãi biển xanh, lặn ngắm san hô và hải sản tươi ngon tuyệt vời.",
        "score": 0.7845
    },
    {
        "id": 14,
        "name": "Bãi biển Mỹ Khê",
        "description": "Một trong những bãi biển đẹp nhất hành tinh ở Đà Nẵng với cát trắng mịn, nước biển trong xanh và sóng nhẹ.",
        "score": 0.6912
    },
    {
        "id": 17,
        "name": "Cù Lao Chàm",
        "description": "Khu dự trữ sinh quyển thế giới ở Quảng Nam với rạn san hô đa dạng, lặn biển và làng chài yên bình.",
        "score": 0.6503
    }
]
```

**Các lỗi có thể xảy ra:**

| Status Code | Nguyên nhân |
|-------------|-------------|
| `400` | Query chỉ chứa khoảng trắng |
| `404` | Không tìm thấy địa điểm phù hợp |
| `422` | Dữ liệu đầu vào không hợp lệ (thiếu query, top_k ngoài phạm vi, sai định dạng) |
| `500` | Lỗi hệ thống trong quá trình suy luận |

---

### 4. Ví dụ gọi API bằng Python (thư viện `requests`)

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# 1. Xem thông tin hệ thống
resp = requests.get(f"{BASE_URL}/")
print(resp.json())

# 2. Kiểm tra health
resp = requests.get(f"{BASE_URL}/health")
print(resp.json())

# 3. Gọi /predict - Tìm kiếm địa điểm du lịch
resp = requests.post(f"{BASE_URL}/predict", json={
    "query": "núi cao sương mù ruộng bậc thang",
    "top_k": 5
})
for dest in resp.json():
    print(f"{dest['name']} — Score: {dest['score']}")
```

---

## Video Demo

[![Demo API Smart Tourism](https://img.youtube.com/vi/QmbwUO5al_4/hqdefault.jpg)](https://youtu.be/QmbwUO5al_4)
> 💡 *Nhấn vào ảnh trên để xem video Demo trên YouTube.*

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
    ├── index.html       # Giao diện web
    ├── style.css        # CSS giao diện
    └── app.js           # JavaScript xử lý tương tác
```
