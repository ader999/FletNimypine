from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    mipyme: Optional[dict]
    es_admin_mipyme: bool
    es_creador_contenido: bool
    rol: str
    avatar: Optional[str]
    email_confirmado: bool
    is_active: bool
    date_joined: str

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