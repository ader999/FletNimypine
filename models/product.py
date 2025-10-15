from dataclasses import dataclass
from typing import List, Optional
from decimal import Decimal

@dataclass
class Product:
    id: int
    nombre: str
    descripcion: str
    mipyme: int
    mipyme_name: str
    precio_venta: Decimal
    porcentaje_ganancia: Decimal
    stock_actual: int
    peso: Optional[Decimal]
    tamano_largo: Optional[Decimal]
    tamano_ancho: Optional[Decimal]
    tamano_alto: Optional[Decimal]
    presentacion: str
    costo_de_produccion: Decimal
    procesos: List[int]
    impuestos: List[int]
    formulacion: List[dict]
    procesos_detalles: List[dict]
    impuestos_detalles: List[dict]

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion', ''),
            mipyme=data.get('mipyme'),
            mipyme_name=data.get('mipyme_name'),
            precio_venta=Decimal(str(data.get('precio_venta', 0))),
            porcentaje_ganancia=Decimal(str(data.get('porcentaje_ganancia', 0))),
            stock_actual=data.get('stock_actual', 0),
            peso=Decimal(str(data.get('peso'))) if data.get('peso') else None,
            tamano_largo=Decimal(str(data.get('tamano_largo'))) if data.get('tamano_largo') else None,
            tamano_ancho=Decimal(str(data.get('tamano_ancho'))) if data.get('tamano_ancho') else None,
            tamano_alto=Decimal(str(data.get('tamano_alto'))) if data.get('tamano_alto') else None,
            presentacion=data.get('presentacion', ''),
            costo_de_produccion=Decimal(str(data.get('costo_de_produccion', 0))),
            procesos=data.get('procesos', []),
            impuestos=data.get('impuestos', []),
            formulacion=data.get('formulacion', []),
            procesos_detalles=data.get('procesos_detalles', []),
            impuestos_detalles=data.get('impuestos_detalles', [])
        )