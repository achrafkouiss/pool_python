from pydantic import BaseModel, Field, ValidationError, field_validator
from datetime import datetime
from typing import Optional, Annotated

SPACE_STATIONS1= {
        'station_id': 'LGW125',
        'name': 'Titan Mining Outpost',
        'crew_size': 6,
        'power_level': 76.4,
        'oxygen_level': 95.5,
        'last_maintenance': '2023-07-11T00:00:00',
        'is_operational': True,
        'notes': None
    }

SPACE_STATIONS2= {
        'station_id': 'QCH189',
        'name': 'Deep Space Observatory',
        'crew_size': 50,
        'power_level': 70.8,
        'oxygen_level': 88.1,
        'last_maintenance': '2023-08-24T00:00:00',
        'is_operational': False,
        'notes': 'We are deep deep, Jhony Deep, deeper stop deeping, \
ping pang pong, ping pong, pingnata'
    }

class SpaceStation(BaseModel):
    station_id: Annotated[str, Field(..., min_length=3, max_length=10)]
    name: Annotated[str, Field(..., min_length=1, max_length=50)]
    crew_size: Annotated[int, Field(..., ge=0, le=20)]
    power_level: Annotated[float, Field(..., ge=0.0, le=100.0)]
    oxygen_level: Annotated[float, Field(..., ge=0.0, le=100.0)]
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[Annotated[str, Field(..., max_length=200)]]


def main():
    print("============================================================")
    try:
        station1 = SpaceStation(**SPACE_STATIONS1)
        print("Valid station created:")
        print(f"ID: {station1.station_id}")
        print(f"Name: {station1.name}")
        print(f"Crew: {station1.crew_size} people")
        print(f"Power: {station1.power_level}%")
        print(f"Oxygen: {station1.oxygen_level}%")
        Operationel = 'Operationel' if station1.is_operational is True else 'Not Operational'
        print(f"Status: {Operationel}")
        print()
        station2 = SpaceStation(**SPACE_STATIONS2)
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors())


if __name__ == "__main__":
    main()

