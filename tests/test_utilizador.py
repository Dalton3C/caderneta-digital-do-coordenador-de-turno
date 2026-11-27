import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import app.models  # noqa: F401
from app.database import Base
from app.models import Utilizador
from app.security import hash_password, verify_password


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as sessao:
        yield sessao


def novo(email="a@caderneta.example", perfil="professor"):
    return Utilizador(nome="Teste", email=email, perfil=perfil,
                      password_hash=hash_password("Demo#2026"))


def test_criar_utilizador(db):
    db.add(novo())
    db.commit()
    assert db.query(Utilizador).count() == 1


def test_email_unico(db):
    db.add(novo())
    db.commit()
    db.add(novo())
    with pytest.raises(IntegrityError):
        db.commit()


def test_perfil_invalido(db):
    db.add(novo(perfil="intruso"))
    with pytest.raises(IntegrityError):
        db.commit()


def test_hash_da_palavra_passe():
    h = hash_password("Demo#2026")
    assert h != "Demo#2026"
    assert verify_password("Demo#2026", h)
    assert not verify_password("errada", h)