from pydantic import model_validator, ValidationError, BaseModel, Field
from typing import Annotated, Optional
from datetime import datetime
from enum import Enum
from typing_extensions import Self


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


contacts = [
    {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-01-20T00:00:00",
        "location": "Area 51, Nevada",
        "contact_type": ContactType.RADIO.value,
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False,
    },
    {
        "contact_id": "AC_2024_002",
        "timestamp": "2024-01-16T09:15:00",
        "location": "Roswell",
        "contact_type": ContactType.TELEPATHIC.value,
        "signal_strength": 6.2,
        "duration_minutes": 30,
        "witness_count": 1,
        "message_received": None,
        "is_verified": False,
    },
]


class AlienContact(BaseModel):
    contact_id: Annotated[str, Field(..., min_length=5, max_length=15)]
    timestamp: datetime
    location: Annotated[str, Field(..., min_length=3, max_length=15)]
    contact_type: ContactType
    signal_strength: Annotated[float, Field(..., ge=0.0, le=10.0)]
    duration_minutes: Annotated[int, Field(..., ge=1, le=1440)]
    witness_count: Annotated[int, Field(..., ge=1, le=100)]
    message_received: Annotated[Optional[str], Field(..., max_length=500)]
    is_verified: bool = True

    @model_validator(mode="after")
    def validatiton_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        elif (
            self.contact_type.value == ContactType.PHYSICAL.value
            and self.is_verified is False
        ):
            raise ValueError("physical contact must be verified")
        elif (
            self.contact_type.value == ContactType.TELEPATHIC.value
            and self.witness_count < 3
        ):
            raise ValueError("telepathic contact"
                             "requires at least 3 witnesses")
        elif self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("strong signals should include received messages")
        return self


def display_info(contact):
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received is not None:
        print(f"Message '{contact.message_received}'")
    print()


def main():
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")

    for contact in contacts:
        try:
            display_info(AlienContact(**contact))
        except ValidationError as e:
            print("Expected validation error:")
            print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
