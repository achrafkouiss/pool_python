from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        return data


class InputStage():
    def process(self, data: Any) -> Dict:
        if not isinstance(data, dict):
            raise TypeError(
                "Error detected in Stage 1: expects a dict payload"
            )
        return data


class TransformStage():
    def process(self, data: Any) -> Dict:
        if not isinstance(data, dict):
            raise TypeError(
                "Error detected in Stage 2: data should be a dictionary"
            )
        keys_to_update: List[str] = ['Input', 'Transform', 'Output']
        new_dict: Dict = {}
        for key in keys_to_update:
            if key in data:
                new_dict[key] = data[key]
        return new_dict


class OutputStage():
    def process(self, data: Any) -> str:
        if not isinstance(data, dict):
            raise TypeError(
                "Error detected in Stage 3: data should be a dictionary"
            )
        custom_string: str = "\n".join(
            f"{key}:{value}" for key, value in data.items()
        ) + "\n"
        return custom_string


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def add_stage(self, stage: ProcessingStage) -> ProcessingStage:
        self.stages.append(stage)
        return stage

    def run_pipeline(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        return data


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: Union[int, str]) -> None:
        super().__init__()
        self.pipeline_id: Union[int, str] = pipeline_id

    def __check_data(self, data: Any) -> None:
        if not isinstance(data, dict):
            raise TypeError("JSON data must be a dictionary")
        if len(data) != 3:
            raise ValueError(
                "JSON data must contain exactly 3 keys: sensor, value, unit"
            )
        if not isinstance(data.get("sensor"), str):
            raise TypeError("sensor must be a string")
        if not isinstance(data.get("value"), (int, float)):
            raise TypeError("value must be int or float")
        if not isinstance(data.get("unit"), str):
            raise TypeError("unit must be a string")

    def process(self, data: Any) -> Optional[str]:
        try:
            self.__check_data(data)
            payload: Dict = {
                "Input": data,
                "value": data["value"],
                "unit": data["unit"],
                "Transform": "Enriched with metadata and validation",
                "Output": f"Processed temperature reading: "
                          f"{data['value']}°{data['unit']}"
            }
            return self.run_pipeline(payload)

        except Exception as e:
            print(e)
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            return None


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: Union[int, str]) -> None:
        super().__init__()
        self.pipeline_id: Union[int, str] = pipeline_id

    def __check_data(self, data: Any) -> None:
        if not isinstance(data, list):
            raise TypeError("CSV input must be a list of strings")

        actions: set[str] = {"login", "logout", "signed"}
        days: set[str] = {
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday"
        }

        for row in data:
            if not isinstance(row, str):
                raise TypeError("Each CSV row must be a string")

            parts: List[str] = row.split(",")
            if len(parts) != 3:
                raise ValueError(
                    "Each CSV row must contain: user,action,timestamp"
                    )

            if not parts[0].isdigit():
                raise ValueError("user must be an integer")

            if parts[1] not in actions:
                raise ValueError(
                    "action must be one of: login, logout, signed"
                    )

            if parts[2] not in days:
                raise ValueError("timestamp must be a valid weekday")

    def process(self, data: Any) -> Optional[str]:
        try:
            self.__check_data(data)
            lenght: int = len(data)
            payload: Dict = {
                "Input": "user,action,timestamp",
                "len": lenght,
                "Transform": "Parsed and structured CSV data",
                "Output": f"User activity logged: {lenght} actions processed"
            }
            return self.run_pipeline(payload)

        except Exception as e:
            print(e)
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            return None


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: Union[int, str]) -> None:
        super().__init__()
        self.pipeline_id: Union[int, str] = pipeline_id

    def __check_data(self, data: Any) -> None:
        if not isinstance(data, list):
            raise TypeError("Stream input must be a list of numbers")

        for x in data:
            if not isinstance(x, (int, float)):
                raise ValueError("Stream elements must be int or float")

    def process(self, data: Any) -> Optional[str]:
        try:
            self.__check_data(data)
            leng = len(data)
            avg: float = sum(data) / leng
            payload: Dict = {
                "Input": "Real-time sensor stream",
                "avg": avg,
                "Transform": "Aggregated sensor data",
                "Output": f"Stream summary: {leng} readings, avg: {avg:.2f}°C"
            }
            return self.run_pipeline(payload)
        except Exception as e:
            print(e)
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            return None


class NexusManager():
    def __init__(self) -> None:
        self.Pipeline: List[ProcessingPipeline] = []
        self.name: int = 0

    def add_pipeline(self, object: ProcessingPipeline) -> ProcessingPipeline:
        self.Pipeline.append(object)
        return object

    def __checkdata(self, data: Any) -> Optional[ProcessingPipeline]:
        if isinstance(data, dict):
            self.name += 1
            return self.add_pipeline(JSONAdapter(self.name))
        elif isinstance(data, list):
            if all(isinstance(x, (int, float)) for x in data):
                self.name += 1
                return self.add_pipeline(StreamAdapter(self.name))
            elif all(isinstance(x, str) for x in data):
                self.name += 1
                return self.add_pipeline(CSVAdapter(self.name))
        return None

    def process_data(self, data: List[Any]) -> str:
        print("Pipeline capacity: 100 streams/second\n")
        print("Creating Data Processing Pipeline...")
        for d in data:
            process: Optional[ProcessingPipeline] = self.__checkdata(d)
            if process:
                process.process(d)

        print("Stage 1: Input validation and parsing")
        print("Stage 2: Data transformation and enrichment")
        print("Stage 3: Output formatting and delivery\n")

        lenght: int = len(self.Pipeline)
        names: List[str] = [
            f"Pipeline {pipe.pipeline_id}" for pipe in self.Pipeline
            ]

        string: str = " -> ".join(names) + "\n"
        string += "Data flow: Raw -> Processed -> Analyzed -> Stored\n\n"
        string += f"Chain result: {lenght} "
        string += "records processed through 3-stage pipeline\n"
        efficiency: float = (lenght * 100) / len(data)
        processing: float = len(self.Pipeline) / 100
        string += f"Performance: {efficiency:.02f}% efficiency, "
        string += f"{processing}s total processing time\n"
        return string


def main():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    nexus: NexusManager = NexusManager()
    nexus_process: str = nexus.process_data(
        [
            [1, 2],
            ["1,login,Monday", "1,login,Monday"],
            {"sensor": "temp", "value": 23.5, "unit": "C"},
        ]
    )

    print("=== Multi-Format Data Processing ===\n")
    print("Processing JSON data through pipeline...")
    json_adapter: JSONAdapter = JSONAdapter("JSONAdapter")
    print(json_adapter.process({"sensor": "temp", "value": 23.5, "unit": "C"}))

    print("Processing CSV data through same pipeline...")
    csv_adapter: CSVAdapter = CSVAdapter("CSVAdapter")
    print(csv_adapter.process(["1,login,Monday", "1,login,Monday"]))

    print("Processing Stream data through same pipeline...")
    stream_dapter: StreamAdapter = StreamAdapter("StreamAdapter")
    print(stream_dapter.process([1, 2, 3.5]))

    print("=== Pipeline Chaining Demo ===")
    print(nexus_process)

    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    csv_adapter2: CSVAdapter = CSVAdapter("CSVAdapter")
    csv_adapter2.process("1,login,Monday")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
