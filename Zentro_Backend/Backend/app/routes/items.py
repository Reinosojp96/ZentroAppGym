# En tu archivo de rutas (por ejemplo, app/routes/items.py)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()

@router.get("/items/")
def read_items(db: Session = Depends(get_db)):
    # Ahora puedes usar 'db' para interactuar con la base de datos
    # por ejemplo: items = db.query(models.Item).all()
    return {"message": "Aquí se mostrarían los items."}