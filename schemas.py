from typing import Union, Optional  # Utilisez Optional pour plus de clarté
from pydantic import BaseModel, Field  # Importez Field pour les options de configuration
from pydantic import ConfigDict  # Utilisez ConfigDict pour la configuration V2

# --- Classes Item ---

class ItemBase(BaseModel):
    title: str = Field(...)  # Champ obligatoire avec Field(...)
    description: Optional[str] = Field(None)  # Utilisation de Optional et Field

class ItemCreate(ItemBase):
    pass  # Rien à ajouter ici

class Item(ItemBase):
    id: int = Field(...) 
    owner_id: int = Field(...)  # Utilisation de owner_id pour lier l'item à un utilisateur
    model_config = ConfigDict(from_attributes=True)  # Configuration V2 avec ConfigDict

# --- Classes User ---

class UserBase(BaseModel):
    email: str = Field(...)

class UserCreate(UserBase):
    password: str = Field(...)  # Champ obligatoire avec Field(...)

class User(UserBase):
    id: int = Field(...)
    is_active: bool = Field(True)  # Valeur par défaut True
    items: list[Item] = []
    
    model_config = ConfigDict(from_attributes=True)
