from sqlalchemy import select

from app.database import SessionLocal
from app.models import Utilizador
from app.security import hash_password

# Dados FICTÍCIOS, só para desenvolvimento e demonstração local.
SENHA_DEMO = "Demo#2026"
UTILIZADORES = [
    ("Administrador Demo", "admin@caderneta.example", "admin"),
    ("Coordenador Demo", "coordenador@caderneta.example", "coordenador"),
    ("Professor Demo", "professor@caderneta.example", "professor"),
]


def main() -> None:
    with SessionLocal() as db:
        for nome, email, perfil in UTILIZADORES:
            if db.scalar(select(Utilizador).where(Utilizador.email == email)):
                continue
            db.add(Utilizador(nome=nome, email=email, perfil=perfil,
                              password_hash=hash_password(SENHA_DEMO)))
        db.commit()
        print(f"Utilizadores na base de dados: {len(db.scalars(select(Utilizador)).all())}")


if __name__ == "__main__":
    main()