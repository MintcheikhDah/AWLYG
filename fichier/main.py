from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

import models, schemas, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/fichiers/", response_model=schemas.Fichier)
def create_fichier(fichier: schemas.FichierCreate, db: Session = Depends(get_db)):
    fichier_in_db = models.Fichier(
        name=fichier.name,
        description=fichier.description,
        niveau_id=fichier.niveau_id,
        filiere_id=fichier.filiere_id,
        groupe_id=fichier.groupe_id,
        annee_universitaire_id=fichier.annee_universitaire_id,
    )
    db.add(fichier_in_db)
    db.commit()
    db.refresh(fichier_in_db)
    return fichier_in_db

@app.get("/fichiers/", response_model=List[schemas.Fichier])
def read_fichiers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    fichiers = db.query(models.Fichier).offset(skip).limit(limit).all()
    return fichiers

@app.get("/fichiers/{fichier_id}", response_model=schemas.Fichier)
def read_fichier(fichier_id: int, db: Session = Depends(get_db)):
    fichier = db.query(models.Fichier).filter(models.Fichier.id == fichier_id).first()
    if not fichier:
        raise HTTPException(status_code=404, detail="Fichier not found")
    return fichier

@app.put("/fichiers/{fichier_id}", response_model=schemas.Fichier)
def update_fichier(fichier_id: int, fichier: schemas.FichierCreate, db: Session = Depends(get_db)):
    fichier_in_db = db.query(models.Fichier).filter(models.Fichier.id == fichier_id).first()
    if not fichier_in_db:
        raise HTTPException(status_code=404, detail="Fichier not found")

    fichier_in_db.name = fichier.name
    fichier_in_db.description = fichier.description
    fichier_in_db.niveau_id = fichier.niveau_id
    fichier_in_db.filiere_id = fichier.filiere_id
    fichier_in_db.groupe_id = fichier.groupe_id
    fichier_in_db.annee_universitaire_id = fichier.annee_universitaire_id

    db.commit()
    return fichier_in_db

@app.delete("/fichiers/{fichier_id}")
def delete_fichier(fichier_id: int, db: Session = Depends(get_db)):
    fichier = db.query(models.Fichier).filter(models.Fichier.id == fichier_id).first()
    if not fichier:
        raise HTTPException(status_code=404, detail="Fichier not found")

    db.delete(fichier)
    db.commit()
    return {"detail": "Fichier deleted"}