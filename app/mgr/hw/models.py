from redis_om import (EmbeddedJsonModel, Field, JsonModel)
from pydantic import PositiveInt
from typing import Optional, List


class Contact(EmbeddedJsonModel):
    street_number: PositiveInt = Field(index=True)

    unit: Optional[str] = Field(index=False)
    street_name: str = Field(index=True)
    city: str = Field(index=True)
    state: str = Field(index=True)
    postal_code: str = Field(index=True)

    # Provide a default value if none supplied...
    country: str = Field(index=True, default="United Kingdom")


class BioData(EmbeddedJsonModel):
    gender: str = Field(index=True)
    height: PositiveInt = Field(index=False)
    weight: PositiveInt = Field(index=False)

class Person(JsonModel):
    # Indexed for exact text matching
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    age: PositiveInt = Field(index=True)

    biodata: BioData
    contact: Contact

    skills: List[str] = Field(index=True)

    personal_statement: str = Field(index=True, full_text_search=True)


#eof