"""
Webapp demo cho lab CI/CD.
API máy tính đơn giản: trang chủ, health check, cộng, chia.
"""
from fastapi import FastAPI, HTTPException

# Khởi tạo ứng dụng
app = FastAPI(title="CI/CD Demo App", version="1.0.0")

@app.get("/")
def read_root():
    """Trang chủ — trả về lời chào."""
    return {"message": "Hello DevOps! App đang chạy."}

@app.get("/health")
def health_check():
    """
    Health check endpoint — QUAN TRỌNG trong DevOps:
    giúp hệ thống giám sát biết app còn sống hay không.
    """
    return {"status": "ok"}

@app.get("/add")
def add(a: float, b: float):
    """Cộng 2 số."""
    return {"a": a, "b": b, "result": a + b}

@app.get("/divide")
def divide(a: float, b: float):
    """Chia 2 số. Chia cho 0 trả lỗi 400."""
    if b == 0:
        raise HTTPException(status_code=400, detail="Không thể chia cho 0")
    return {"a": a, "b": b, "result": a / b}