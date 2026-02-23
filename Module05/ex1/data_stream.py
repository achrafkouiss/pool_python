from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: Any) -> None:
        self.name: Any = stream_id
        self.processed: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        return ""

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"type": "Generic", "processed": self.processed}


class SensorStream(DataStream):
    def __init__(self, stream_id: Any) -> None:
        super().__init__(stream_id)
        self.critical: int = 0
        self.env_keys: set[str] = {
            "temp", "humidity", "pressure", "visibility", "wind", "Cloudiness"
        }
        self.required_keys: set[str] = {"max", "min"}

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            existing_keys: List[str] = [
                key for key in self.env_keys
                if any(key in d for d in data_batch)
            ]
            existing_env: bool = all(
                any(k in d for k in self.env_keys) for d in data_batch
            )
            if not existing_env:
                return (
                    "data should only contain temp, humidity, pressure, "
                    "visibility, wind, Cloudiness with each one containg "
                    "the maximum and minimum range (max, min)\n"
                )
            string: str = f"Stream ID: {self.name}, Type: Environmental Data\n"
            data: List[Union[int, float]] = self.filter_data(
                data_batch, existing_keys[0]
            )
            string += "Processing sensor batch: ["
            batch_len: int = len(data_batch)
            for index, dictionary in enumerate(data_batch):
                dict_set: set[str] = set(dictionary)
                k_present: str = list(self.env_keys.intersection(dict_set))[0]
                for key, value in dictionary.items():
                    if key == k_present:
                        string += f"{key}:{value}"
                if index != batch_len - 1:
                    string += ", "
                else:
                    string += "]\n"
            average: float = sum(data) / len(data)
            string += (
                f"Sensor analysis: {self.processed} readings processed, "
                f"avg {existing_keys[0]}: {average}\n"
            )
            return string
        except Exception as e:
            return f"SensorStream error: {e}\n"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Union[int, float]]:
        try:
            check_criteria: bool = any(criteria in d for d in data_batch)
            range_keys_present: bool = all(
                "min" in d and "max" in d for d in data_batch
            )
            one_env_keys: bool = all(
                any(k in d for k in self.env_keys) for d in data_batch
            )
            all_have_three: bool = all(len(d) == 3 for d in data_batch)
            if not range_keys_present or not one_env_keys \
                    or not check_criteria or not all_have_three:
                return []
            processing: int = len(data_batch)
            criteria_list: List[Union[int, float]] = [
                d.get(criteria) for d in data_batch if d.get(criteria)
            ]
            len_critical: int = 0
            for d in data_batch:
                dict_set: set[str] = set(d)
                keys_present: str = list(
                    self.env_keys.intersection(dict_set)
                )[0]
                if not d["min"] < d[keys_present] < d["max"]:
                    len_critical += 1
            self.critical = len_critical
            self.processed = processing
            return criteria_list
        except Exception:
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "type": "Sensor",
            "reading": self.processed,
            "critical": self.critical
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id: Any) -> None:
        super().__init__(stream_id)
        self.large: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            string: str = f"Stream ID: {self.name}, Type: Financial Data\n"
            data: List[Union[int, float]] = self.filter_data(data_batch)
            if not data:
                return "prolem filtering data\n"
            string += "Processing transaction batch: ["
            batch_len: int = len(data_batch)
            for index, number in enumerate(data_batch):
                if number < 0:
                    string += f"sell:{number * -1}"
                else:
                    string += f"buy:{number}"
                if index != batch_len - 1:
                    string += ", "
                else:
                    string += "]\n"
            total: Union[int, float] = sum(data_batch)
            if total < 0:
                s: str = f"{total}"
            else:
                s = f"+{total}"
            string += (
                f"Transaction analysis: {self.processed} operations, "
                f"net flow: {s} units\n"
            )
            return string
        except Exception as e:
            return f"TransactionStream error: {e}\n"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Union[int, float]]:
        try:
            check_list: bool = all(
                isinstance(item, (int, float)) for item in data_batch
            )
            if not check_list and isinstance(data_batch, list) \
                    or criteria not in ("buy", "sell", None):
                return []
            processing: int = len(data_batch)
            if criteria == "sell":
                criteria_list: List[Union[int, float]] = [
                    x for x in data_batch if x < 0
                ]
            elif criteria == "buy":
                criteria_list = [x for x in data_batch if x > 0]
            else:
                criteria_list = data_batch
            count_large: int = len([
                number for number in data_batch
                if number >= 150 or number <= -150
            ])
            self.processed = processing
            self.large = count_large
            return criteria_list
        except Exception:
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "type": "Transaction",
            "operations": self.processed,
            "large": self.large
        }


class EventStream(DataStream):
    def __init__(self, stream_id: Any) -> None:
        super().__init__(stream_id)
        self.error: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            string: str = f"Stream ID: {self.name}, Type: System Events\n"
            data: List[str] = self.filter_data(data_batch, "error")
            if not data:
                return "prolem filtering data\n"
            string += f"Processing event batch: [{', '.join(data_batch)}]\n"
            string += (
                f"Processing event batch: {self.processed} events, "
                f"net flow: {self.error} error detected\n"
            )
            return string
        except Exception as e:
            return f"EventStream error: {e}\n"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[str]:
        try:
            is_valid: bool = all(
                item in {"error", "login", "logout"} for item in data_batch
            )
            if not all(isinstance(item, str) for item in data_batch) \
                    and isinstance(data_batch, list) \
                    and not is_valid \
                    and criteria in ("error", "login", "logout", None):
                return []
            processing: int = len(data_batch)
            error_count: int = len([x for x in data_batch if x == "error"])
            criteria_list: List[str] = [x for x in data_batch if x != criteria]
            self.processed = processing
            self.error = error_count
            return criteria_list
        except Exception:
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "type": "Event",
            "events": self.processed,
            "error": self.error
        }


class StreamProcessor:
    def __init__(self) -> None:
        self.list_of_stream: List[DataStream] = []

    def append_steam(self, stream: DataStream) -> None:
        self.list_of_stream.append(stream)

    def process_data(self, data: List[Any]) -> str:
        try:
            stats: List[Dict[str, Union[str, int, float]]] = []
            string: str = ""
            priority: List[Dict[str, Union[str, int, float]]] = []
            for index, obj in enumerate(self.list_of_stream):
                obj.process_batch(data[index])
                stats.append(obj.get_stats())
            for dic in stats:
                last_key: str = list(dic)[-1]
                key: str = list(dic.keys())[1]
                string += f"- {dic['type']} data: {dic[key]} {key} processed\n"
                if dic[last_key] > 0:
                    priority.append(dic)
            string += "\nStream filtering active: High-priority data only\n"
            string += "Filtered results: "
            priority_len: int = len(priority)
            for index, dic in enumerate(priority):
                last_key = list(dic)[-1]
                string += f"{dic[last_key]} {last_key} {dic['type']}"
                if index != priority_len - 1:
                    string += ", "
                else:
                    string += "\n"
            return string
        except Exception as e:
            return f"StreamProcessor error: {e}\n"


if __name__ == "__main__":
    print("Initializing Sensor Stream...")
    SENSOR_001 = SensorStream("SENSOR_001")
    data = [
        {"temp": 22.5, "min": 0, "max": 100},
        {"humidity": 65, "min": 0, "max": 100},
        {"pressure": 1013, "min": 200, "max": 1000}
    ]
    print(SENSOR_001.process_batch(data))

    print("Initializing Sensor Stream...")
    TRANS_001 = TransactionStream("TRANS_001")
    data = [100, -150, 75]
    print(TRANS_001.process_batch(data))

    print("Initializing Event Stream...")
    EVENT_001 = EventStream("EVENT_001")
    data = ["login", "error", "logout"]
    print(EVENT_001.process_batch(data))

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    print("Batch 1 Results:")
    streams = [
        SensorStream("SENSOR_002"),
        TransactionStream("TRANS_002"),
        EventStream("EVENT_002"),
    ]
    data = [
            [
                {"temp": 150, "min": 0, "max": 100},
                {"humidity": 65.6, "min": 100, "max": 200}
            ],
            [
                100, -120, 75, 150
            ],
            [
                "login", "login", "logout"
            ]
        ]

    StreamPro = StreamProcessor()
    for object in streams:
        StreamPro.append_steam(object)

    print(StreamPro.process_data(data))
    print("All streams processed successfully. Nexus throughput optimal.")
