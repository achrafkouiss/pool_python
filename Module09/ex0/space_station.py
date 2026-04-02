from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional, Annotated

SPACE_STATIONS = [
    {
        "station_id": "ISS001",
        "name": " International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2023-07-11T00:00:00",
        "is_operational": True,
        "notes": None,
    },
    {
        "station_id": "QCH189",
        "name": "Deep Space Observatory",
        "crew_size": 21,
        "power_level": 70.8,
        "oxygen_level": 88.1,
        "last_maintenance": "2023-08-24T00:00:00",
        "is_operational": False,
        "notes": "We are deep deep, Jhony Deep, deeper stop deeping, \
ping pang pong, ping pong, pingnata",
    },
]


class SpaceStation(BaseModel):
    station_id: Annotated[str, Field(..., min_length=3, max_length=10)]
    name: Annotated[str, Field(..., min_length=1, max_length=50)]
    crew_size: Annotated[int, Field(..., ge=0, le=20)]
    power_level: Annotated[float, Field(..., ge=0.0, le=100.0)]
    oxygen_level: Annotated[float, Field(..., ge=0.0, le=100.0)]
    last_maintenance: datetime
    is_operational: Annotated[bool, Field(default=True)]
    notes: Optional[Annotated[str, Field(..., max_length=200)]]


def display_info(station):
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    Operationel = "Operationel" if station.is_operational is True \
        else "Not Operational"
    print(f"Status: {Operationel}")


def main():
    print("Space Station Data Validation")
    print("============================================================")

    try:
        for station in SPACE_STATIONS:
            display_info(SpaceStation(**station))
            print()
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
