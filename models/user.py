from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    username: str
    email: str
    id: Optional[int] = None
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""
    mipyme: Optional[dict] = None
    es_admin_mipyme: bool = False
    es_creador_contenido: bool = False
    rol: Optional[str] = None
    avatar: Optional[str] = None
    email_confirmado: bool = False
    is_active: bool = True
    date_joined: Optional[str] = None
    token: Optional[str] = None

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            username=data.get('username'),
            email=data.get('email'),
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            mipyme=data.get('mipyme'),
            es_admin_mipyme=data.get('es_admin_mipyme', False),
            es_creador_contenido=data.get('es_creador_contenido', False),
            rol=data.get('rol'),
            avatar=data.get('avatar'),
            email_confirmado=data.get('email_confirmado', False),
            is_active=data.get('is_active', True),
            date_joined=data.get('date_joined')
        )