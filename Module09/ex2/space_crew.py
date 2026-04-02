from pydantic import BaseModel, ValidationError, Field, model_validator
from enum import Enum
from typing import Annotated
from datetime import datetime
from typing_extensions import Self


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


SPACE_MISSIONS = [
    {
        "mission_id": "M2024_TITAN",
        "mission_name": "Solar Observatory Research Mission",
        "destination": "Solar Observatory",
        "launch_date": "2024-03-30T00:00:00",
        "duration_days": 451,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Williams",
                "rank": Rank.CAPTAIN.value,
                "age": 43,
                "specialization": "Mission Command",
                "years_experience": 19,
                "is_active": True,
            },
            {
                "member_id": "CM002",
                "name": "James Hernandez",
                "rank": Rank.CAPTAIN.value,
                "age": 43,
                "specialization": "Pilot",
                "years_experience": 30,
                "is_active": True,
            },
            {
                "member_id": "CM003",
                "name": "Anna Jones",
                "rank": Rank.CADET.value,
                "age": 35,
                "specialization": "Communications",
                "years_experience": 15,
                "is_active": True,
            },
            {
                "member_id": "CM004",
                "name": "David Smith",
                "rank": Rank.COMMANDER.value,
                "age": 27,
                "specialization": "Security",
                "years_experience": 15,
                "is_active": True,
            },
            {
                "member_id": "CM005",
                "name": "Maria Jones",
                "rank": Rank.CADET.value,
                "age": 55,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True,
            },
        ],
        "mission_status": "planned",
        "budget_millions": 2208.1,
    },
    {
        "mission_id": "M2024_MARS",
        "mission_name": "Jupiter Orbit Colony Mission",
        "destination": "Jupiter Orbit",
        "launch_date": "2024-10-01T00:00:00",
        "duration_days": 1065,
        "crew": [
            {
                "member_id": "CM011",
                "name": "Emma Brown",
                "rank": Rank.COMMANDER.value,
                "age": 49,
                "specialization": "Mission Command",
                "years_experience": 27,
                "is_active": True,
            },
            {
                "member_id": "CM012",
                "name": "John Hernandez",
                "rank": Rank.LIEUTENANT.value,
                "age": 36,
                "specialization": "Science Officer",
                "years_experience": 22,
                "is_active": True,
            },
            {
                "member_id": "CM013",
                "name": "Sofia Rodriguez",
                "rank": Rank.COMMANDER.value,
                "age": 29,
                "specialization": "Life Support",
                "years_experience": 20,
                "is_active": True,
            },
            {
                "member_id": "CM014",
                "name": "Sofia Lopez",
                "rank": Rank.LIEUTENANT.value,
                "age": 44,
                "specialization": "Systems Analysis",
                "years_experience": 25,
                "is_active": True,
            },
        ],
        "mission_status": "planned",
        "budget_millions": 4626.0,
    },
    {
        "mission_id": "M2024_EUROPA",
        "mission_name": "Europa Colony Mission",
        "destination": "Europa",
        "launch_date": "2024-02-07T00:00:00",
        "duration_days": 666,
        "crew": [
            {
                "member_id": "CM021",
                "name": "Lisa Garcia",
                "rank": Rank.CAPTAIN.value,
                "age": 36,
                "specialization": "Medical Officer",
                "years_experience": 12,
                "is_active": True,
            },
            {
                "member_id": "CM022",
                "name": "John Garcia",
                "rank": Rank.CADET.value,
                "age": 46,
                "specialization": "Security",
                "years_experience": 25,
                "is_active": True,
            },
            {
                "member_id": "CM023",
                "name": "Michael Johnson",
                "rank": Rank.OFFICER.value,
                "age": 54,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True,
            },
            {
                "member_id": "CM024",
                "name": "Sarah Rodriguez",
                "rank": Rank.LIEUTENANT.value,
                "age": 54,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True,
            },
            {
                "member_id": "CM025",
                "name": "Maria Smith",
                "rank": Rank.CADET.value,
                "age": 38,
                "specialization": "Communications",
                "years_experience": 15,
                "is_active": True,
            },
        ],
        "mission_status": "planned",
        "budget_millions": 4976.0,
    },
    {
        "mission_id": "M2024_LUNA",
        "mission_name": "Mars Colony Mission",
        "destination": "Mars",
        "launch_date": "2024-06-13T00:00:00",
        "duration_days": 222,
        "crew": [
            {
                "member_id": "CM031",
                "name": "Anna Davis",
                "rank": Rank.COMMANDER.value,
                "age": 27,
                "specialization": "Communications",
                "years_experience": 14,
                "is_active": True,
            },
            {
                "member_id": "CM032",
                "name": "Elena Garcia",
                "rank": Rank.LIEUTENANT.value,
                "age": 42,
                "specialization": "Science Officer",
                "years_experience": 23,
                "is_active": True,
            },
            {
                "member_id": "CM033",
                "name": "Anna Brown",
                "rank": Rank.OFFICER.value,
                "age": 55,
                "specialization": "Engineering",
                "years_experience": 30,
                "is_active": True,
            },
            {
                "member_id": "CM034",
                "name": "Emma Smith",
                "rank": Rank.CAPTAIN.value,
                "age": 37,
                "specialization": "Research",
                "years_experience": 23,
                "is_active": True,
            },
            {
                "member_id": "CM035",
                "name": "Sofia Smith",
                "rank": Rank.LIEUTENANT.value,
                "age": 53,
                "specialization": "Security",
                "years_experience": 30,
                "is_active": True,
            },
            {
                "member_id": "CM036",
                "name": "Maria Hernandez",
                "rank": Rank.COMMANDER.value,
                "age": 41,
                "specialization": "Medical Officer",
                "years_experience": 30,
                "is_active": True,
            },
            {
                "member_id": "CM037",
                "name": "John Hernandez",
                "rank": Rank.OFFICER.value,
                "age": 42,
                "specialization": "Science Officer",
                "years_experience": 20,
                "is_active": True,
            },
        ],
        "mission_status": "planned",
        "budget_millions": 4984.6,
    },
    {
        "mission_id": "M2024_EUROPA",
        "mission_name": "Saturn Rings Research Mission",
        "destination": "Saturn Rings",
        "launch_date": "2024-09-18T00:00:00",
        "duration_days": 602,
        "crew": [
            {
                "member_id": "CM041",
                "name": "William Davis",
                "rank": Rank.CAPTAIN.value,
                "age": 35,
                "specialization": "Medical Officer",
                "years_experience": 14,
                "is_active": True,
            },
            {
                "member_id": "CM042",
                "name": "Sarah Smith",
                "rank": Rank.CAPTAIN.value,
                "age": 55,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True,
            },
            {
                "member_id": "CM043",
                "name": "Elena Garcia",
                "rank": Rank.COMMANDER.value,
                "age": 55,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True,
            },
            {
                "member_id": "CM044",
                "name": "Sofia Williams",
                "rank": Rank.OFFICER.value,
                "age": 30,
                "specialization": "Systems Analysis",
                "years_experience": 9,
                "is_active": True,
            },
            {
                "member_id": "CM045",
                "name": "Sarah Jones",
                "rank": Rank.LIEUTENANT.value,
                "age": 25,
                "specialization": "Maintenance",
                "years_experience": 11,
                "is_active": True,
            },
            {
                "member_id": "CM046",
                "name": "Lisa Rodriguez",
                "rank": Rank.OFFICER.value,
                "age": 30,
                "specialization": "Life Support",
                "years_experience": 12,
                "is_active": True,
            },
            {
                "member_id": "CM047",
                "name": "Sarah Smith",
                "rank": Rank.CADET.value,
                "age": 28,
                "specialization": "Pilot",
                "years_experience": 8,
                "is_active": False,
            },
        ],
        "mission_status": "planned",
        "budget_millions": 1092.6,
    },
]


class CrewMember(BaseModel):
    member_id: Annotated[str, Field(..., min_length=3, max_length=10)]
    name: Annotated[str, Field(..., min_length=2, max_length=50)]
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: Annotated[int, Field(..., ge=18, le=80)]
    specialization: Annotated[str, Field(..., min_length=3, max_length=30)]
    years_experience: Annotated[int, Field(..., ge=0, le=50)]
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: Annotated[str, Field(..., min_length=5, max_length=15)]
    mission_name: Annotated[str, Field(..., min_length=3, max_length=100)]
    destination: Annotated[str, Field(..., min_length=3, max_length=50)]
    launch_date: datetime
    duration_days: Annotated[int, Field(..., ge=1, le=3650)]
    crew: Annotated[list[CrewMember], Field(..., min_length=1, max_length=12)]
    mission_status: Annotated[str, Field(default="planned")]
    budget_millions: Annotated[float, Field(..., ge=1.0, le=10000.0)]

    @model_validator(mode="after")
    def validatiton_rules(self) -> Self:
        necessary_rank = False
        experienced = 0
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
            if member.years_experience > 5:
                experienced += 1
            if (
                member.rank.value == Rank.COMMANDER.value
                or member.rank.value == Rank.CAPTAIN.value
            ):
                necessary_rank = True
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        elif not necessary_rank:
            raise ValueError("Must have at least one Commander or Captain")
        elif self.duration_days > 365 and experienced < len(self.crew) / 2:
            raise ValueError(
                "Long missions (> 365 days) need 50%% "
                "experienced crew (5+ years)"
            )
        return self


def display_info(mission):
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    for crew in mission.crew:
        print(f"- {crew.name} ({crew.rank.value}) - {crew.specialization}")
    print()


def main():
    print("Space Mission Crew Validation")
    print("=========================================")
    for space_mission in SPACE_MISSIONS:
        try:
            display_info(SpaceMission(**space_mission))
            print()
        except ValidationError as e:
            print("Expected validation error:")
            print(e.errors()[0]["msg"])
            print()


if __name__ == "__main__":
    main()
