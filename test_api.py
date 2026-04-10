"""
File kiểm thử API bằng thư viện requests.
Chạy file này khi server đang hoạt động (uvicorn main:app --reload).

Sử dụng: python test_api.py
"""

import requests
import json
import sys

BASE_URL = "http://127.0.0.1:8000"

# Màu sắc cho terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

passed = 0
failed = 0


def print_header(text):
    print(f"\n{BOLD}{CYAN}{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}{RESET}")


def print_result(test_name, success, response=None, error=None):
    global passed, failed
    if success:
        passed += 1
        print(f"  {GREEN}✓ PASS{RESET} - {test_name}")
    else:
        failed += 1
        print(f"  {RED}✗ FAIL{RESET} - {test_name}")
    if error:
        print(f"    {RED}Lỗi: {error}{RESET}")
    if response is not None:
        print(f"    {YELLOW}Status: {response.status_code}{RESET}")
        try:
            body = response.json()
            print(f"    Response: {json.dumps(body, ensure_ascii=False, indent=4)}")
        except Exception:
            print(f"    Response: {response.text[:200]}")


# ============================================================
# TEST 1: GET /health - Kiểm tra sức khỏe server
# ============================================================
print_header("TEST 1: GET /health - Kiểm tra sức khỏe server")

try:
    resp = requests.get(f"{BASE_URL}/health")
    data = resp.json()
    success = (
        resp.status_code == 200
        and data.get("status") == "healthy"
        and "total_destinations" in data
        and "model_name" in data
    )
    print_result("Health check trả về status healthy", success, resp)
except Exception as e:
    print_result("Health check trả về status healthy", False, error=str(e))


# ============================================================
# TEST 2: GET / - Kiểm tra trang chủ
# ============================================================
print_header("TEST 2: GET / - Kiểm tra trang chủ (static HTML)")

try:
    resp = requests.get(f"{BASE_URL}/")
    success = resp.status_code == 200 and "text/html" in resp.headers.get("content-type", "")
    print_result("Trang chủ trả về HTML", success, resp)
except Exception as e:
    print_result("Trang chủ trả về HTML", False, error=str(e))


# ============================================================
# TEST 3: POST /suggest - Tìm kiếm thành công
# ============================================================
print_header("TEST 3: POST /suggest - Tìm kiếm địa điểm biển")

try:
    payload = {"query": "bãi biển đẹp", "top_k": 5}
    resp = requests.post(f"{BASE_URL}/suggest", json=payload)
    data = resp.json()
    success = (
        resp.status_code == 200
        and isinstance(data, list)
        and len(data) > 0
        and "name" in data[0]
        and "score" in data[0]
    )
    print_result("Tìm kiếm 'bãi biển đẹp' trả về kết quả", success, resp)
except Exception as e:
    print_result("Tìm kiếm 'bãi biển đẹp' trả về kết quả", False, error=str(e))


# ============================================================
# TEST 4: POST /suggest - Tìm kiếm với query khác
# ============================================================
print_header("TEST 4: POST /suggest - Tìm kiếm 'chùa cổ kính'")

try:
    payload = {"query": "chùa cổ kính linh thiêng", "top_k": 3}
    resp = requests.post(f"{BASE_URL}/suggest", json=payload)
    data = resp.json()
    success = (
        resp.status_code == 200
        and isinstance(data, list)
        and len(data) > 0
    )
    print_result("Tìm kiếm 'chùa cổ kính linh thiêng' thành công", success, resp)
except Exception as e:
    print_result("Tìm kiếm 'chùa cổ kính linh thiêng' thành công", False, error=str(e))


# ============================================================
# TEST 5: POST /suggest - Query rỗng (lỗi 422 validation)
# ============================================================
print_header("TEST 5: POST /suggest - Query rỗng (Validation Error)")

try:
    payload = {"query": "", "top_k": 3}
    resp = requests.post(f"{BASE_URL}/suggest", json=payload)
    # Pydantic sẽ validate min_length=1, trả về 422
    success = resp.status_code == 422
    print_result("Query rỗng trả về lỗi 422", success, resp)
except Exception as e:
    print_result("Query rỗng trả về lỗi 422", False, error=str(e))


# ============================================================
# TEST 6: POST /suggest - Query chỉ có khoảng trắng (lỗi 400)
# ============================================================
print_header("TEST 6: POST /suggest - Query chỉ có khoảng trắng (lỗi 400)")

try:
    payload = {"query": "   ", "top_k": 3}
    resp = requests.post(f"{BASE_URL}/suggest", json=payload)
    # Server kiểm tra .strip() và raise 400
    success = resp.status_code == 400
    print_result("Query khoảng trắng trả về lỗi 400", success, resp)
except Exception as e:
    print_result("Query khoảng trắng trả về lỗi 400", False, error=str(e))


# ============================================================
# TEST 7: POST /suggest - top_k không hợp lệ (lỗi 422)
# ============================================================
print_header("TEST 7: POST /suggest - top_k = 0 (Validation Error)")

try:
    payload = {"query": "núi", "top_k": 0}
    resp = requests.post(f"{BASE_URL}/suggest", json=payload)
    # Pydantic validate gt=0, trả về 422
    success = resp.status_code == 422
    print_result("top_k=0 trả về lỗi 422", success, resp)
except Exception as e:
    print_result("top_k=0 trả về lỗi 422", False, error=str(e))


# ============================================================
# TEST 8: POST /suggest - top_k vượt giới hạn (lỗi 422)
# ============================================================
print_header("TEST 8: POST /suggest - top_k = 100 (vượt le=10)")

try:
    payload = {"query": "thác nước", "top_k": 100}
    resp = requests.post(f"{BASE_URL}/suggest", json=payload)
    # Pydantic validate le=10, trả về 422
    success = resp.status_code == 422
    print_result("top_k=100 trả về lỗi 422", success, resp)
except Exception as e:
    print_result("top_k=100 trả về lỗi 422", False, error=str(e))


# ============================================================
# TEST 9: POST /suggest - Thiếu body (lỗi 422)
# ============================================================
print_header("TEST 9: POST /suggest - Thiếu request body")

try:
    resp = requests.post(f"{BASE_URL}/suggest")
    success = resp.status_code == 422
    print_result("Thiếu body trả về lỗi 422", success, resp)
except Exception as e:
    print_result("Thiếu body trả về lỗi 422", False, error=str(e))


# ============================================================
# TEST 10: POST /generate - Sinh lại dữ liệu
# ============================================================
print_header("TEST 10: POST /generate - Sinh lại dữ liệu")

try:
    resp = requests.post(f"{BASE_URL}/generate")
    data = resp.json()
    success = (
        resp.status_code == 200
        and data.get("status") == "success"
        and data.get("total_generated", 0) == 1000
    )
    print_result("Generate trả về 1000 địa điểm", success, resp)
except Exception as e:
    print_result("Generate trả về 1000 địa điểm", False, error=str(e))


# ============================================================
# TEST 11: GET /health sau khi generate - Kiểm tra dữ liệu mới
# ============================================================
print_header("TEST 11: GET /health sau generate - Xác nhận 1000 địa điểm")

try:
    resp = requests.get(f"{BASE_URL}/health")
    data = resp.json()
    success = (
        resp.status_code == 200
        and data.get("total_destinations") == 1000
    )
    print_result("Health check xác nhận 1000 địa điểm", success, resp)
except Exception as e:
    print_result("Health check xác nhận 1000 địa điểm", False, error=str(e))


# ============================================================
# TỔNG KẾT
# ============================================================
print(f"\n{BOLD}{CYAN}{'='*60}")
print(f"  TỔNG KẾT KẾT QUẢ KIỂM THỬ")
print(f"{'='*60}{RESET}")
print(f"  {GREEN}✓ Passed: {passed}{RESET}")
print(f"  {RED}✗ Failed: {failed}{RESET}")
print(f"  Tổng cộng: {passed + failed} test cases")
print(f"{CYAN}{'='*60}{RESET}\n")

if failed > 0:
    sys.exit(1)
else:
    print(f"  {GREEN}{BOLD}🎉 Tất cả test cases đều PASS!{RESET}\n")
    sys.exit(0)
