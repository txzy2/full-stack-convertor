from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
import os

from docx2pdf import convert
from pdf2docx import Converter
from PIL import Image

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5000", "http://localhost:4433"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/docxtopdf")
async def read_item(file: UploadFile = File(...)):
    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    os.makedirs("converted", exist_ok=True)
    converted_file_location = os.path.join("converted", f"{file.filename}.pdf")

    convert(file_location, converted_file_location)
    return FileResponse(path=converted_file_location)


@app.post("/pdftodocx")
async def read_pdf(file: UploadFile = File(...)):
    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    os.makedirs("converted", exist_ok=True)
    converted_file_location = os.path.join(
        "converted", f"{file.filename}.docx")

    cn = Converter(file_location)
    cn.convert(converted_file_location, start=0, end=None)

    cn.close()
    return FileResponse(path=converted_file_location)

@app.post("/pngtojpg")
async def read_png(file: UploadFile = File(...)):
    file_location = f"uploads/imgs/{file.filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    im = Image.open(file_location)

    os.makedirs("converted", exist_ok=True)
    converted_file_location = os.path.join(
        "converted", f"{file.filename}.png")

    im.save(converted_file_location)

    return FileResponse(path=converted_file_location)

