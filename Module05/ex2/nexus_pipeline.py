from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass

class InputStage():
    def process(self, data: Any) -> Dict:
        if not isinstance(data, (list, dict)):
            raise TypeError("Error detected in Stage 1: data should be a dictionary")
        return {
            "data": data,
            "len": len(data),
            "value": None,
            "unit": None,
            "avg": None,
            "Input": None,
            "Transform": None,
            "Output": None,
            "error": False
            }


class TransformStage():
    def process(self, data: Any) -> Dict:
        if not isinstance(data, dict):
            raise TypeError("Error detected in Stage 2: data should be a dictionary")
        keys_to_update = ['Input', 'Transform', 'Output']
        new_dict = {}
        for key in keys_to_update:
            if key in data:
                new_dict[key] = data[key]
        return new_dict

class OutputStage():
    def process(self, data: Any) -> str:
        if not isinstance(data, dict):
            raise TypeError("Error detected in Stage 3: data should be a dictionary")
        custom_string = "\n".join(f"{key}:{value}" for key, value in data.items())

        print(custom_string, "\n\n\n\n")

class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage) -> ProcessingStage:
        self.stages.append(stage)
        return stage

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipeline_id = pipeline_id
        

    def __check_data(self, data):
        if not isinstance(data["sensor"], str) and \
            not isinstance(data["value"], (int, float)) and \
                not isinstance(data["unit"], str) and\
                    input["len"] != 3:
            raise ValueError("data Should contain no more or less than 3 element (sensor, value, unit)")
    

    def process(self, data) -> Any:
        try:
            processing = super().add_stage(InputStage())
            input = processing.process(data)
            self.__check_data(data)
            input["Input"] = data
            input["unit"] = data["unit"]
            input["value"] = data["value"]
            value_range  = "Normal range" 
            if 20 < input["value"] > 100:
                value_range  = "Danger range"
            input["Transform"] = " Enriched with metadata and validation"
            input["Output"] = f"Processed temperature reading: {input['value']}°{input['unit']} ({value_range})"
            processing = super().add_stage(TransformStage())
            transform = processing.process(input)
            processing = super().add_stage(OutputStage())
            output = processing.process(transform)
        except ValueError as e:
            print(e)
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
        except KeyError as e:
            print("KeyError")
            # it should return a message that say keyerror key not found
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            pass
        except Exception as e:
            print("==========>",e)
            pass

class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipeline_id = pipeline_id

    def __check_data(self, data):
        actions = ["login", "logout", "signed"]
        all_strings = all(isinstance(item, str) for item in data)
        if not all_strings:
            raise ValueError("all element should be strings")
        splited_data = []
        for s in data:
            split_list = s.split(',')
            splited_data.append(split_list)
        for element in splited_data:
            # print(element)
            if len(element) != 3:
                raise TypeError("element should contain 3 elemts (user, action, timestamp)")
            if int(element[0]) and \
                not isinstance(element[1], str) and \
                not isinstance(element[-1], str):
                raise ValueError("element should contain 3 elemts (user(int), action(str), timestamp(str))")
            if not element[1] in actions:
                raise ValueError("action should be either (login logout signed)")
            timestamp = element[-1] in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            if not timestamp:
                raise ValueError("timestamp should be a day of the week")
        return splited_data
       
    def process(self, data) -> Any:
        try:
            processing = super().add_stage(InputStage())
            input = processing.process(data)
            splited_data = self.__check_data(data)
            input["Input"] = "user,action,timestamp"
            input["Transform"] = "Parsed and structured data"
            input["Output"] = f"User activity logged: {input['len']} actions processed"
            processing = super().add_stage(TransformStage())
            transform = processing.process(input)
            processing = super().add_stage(OutputStage())
            output = processing.process(transform)
        except ValueError as e:
            print(e)
        except KeyError as e:
            print("KeyError")
            # it should return a message that say keyerror key not found
        except Exception as e:
            print("==========>",e)

class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__()
        self.pipeline_id = pipeline_id

    def __check_data(self, data):
        for element in data:
            if not isinstance(element, (int, float)):
                raise ValueError("elements should be integer or float")

    def process(self, data) -> Any:
        try:
            processing = super().add_stage(InputStage())
            input = processing.process(data)
            splited_data = self.__check_data(data)
            input["Input"] = "Real-time sensor stream"
            input["avg"] = sum(data) / input["len"]
            input["Transform"] = " Enriched with metadata and validation"
            input["Output"] = f"Stream summary: {input['len']} readings, avg: {input['avg']:.2f}°C"
            processing = super().add_stage(TransformStage())
            transform = processing.process(input)
            processing = super().add_stage(OutputStage())
            output = processing.process(transform)
        except ValueError as e:
            print(e)
        except KeyError as e:
            print("KeyError")
            # it should return a message that say keyerror key not found
        except Exception as e:
            print("==========>",e)


class NexusManager():
    def add_pipeline():
        pass

    def process_data():
        pass

if __name__ == "__main__":
    a = JSONAdapter("cfdsv")
    a.process({"sensor": "temp", "value": 23.5, "unit": "C"})
    b = CSVAdapter("acsca")
    b.process(["1,login,Monday", "1,login,Monday"])
    # print(dir(CSVAdapter),"=" *40 , "\n")
    c = StreamAdapter("achraf")
    c.process([1,2,3.5])
    # {"sensor": "temp", "value": 23.5, "unit": "C"}

    # jsondata = {
    #     "data": {"sensor": "temp", "value": 23.5, "unit": "C"},
    #     "adapter": "json"
    # }

    # jsondata_before_transform = {
    #     "data": {"sensor": "temp", "value": 23.5, "unit": "C"},
    #     "adapter": "json",
    #     "Input": jsondata_before_transform["data"],
    #     "Transform": "Enriched with metadata and validation",
    #     "Output": "Processed temperature reading: ",
    #     "reading": f"{jsondata_before_transform["value"]} {jsondata_before_transform["unit"]}",
    #     "last":  "(Normal range)"
    # }

    # jsondata_after_transform = {
    #     "Input": jsondata_before_transform["data"],
    #     "Transform": "Enriched with metadata and validation",
    #     "Output": "Processed temperature reading: ",
    #     "reading": f"{jsondata_before_transform["value"]} {jsondata_before_transform["unit"]}",
    #     "last":  "(Normal range)"
    # }
    # # ###########################################################################
    # csvdata = {
    #     "data": ["achraf", "logged", "monday"],#each list should contain 3 element and each element should be string and the last element shoudl be a day of the week
    #     "adapter": "csv"
    # }

    # csvdata_before_transform = {
    #     "data": ["achraf", "logged", "monday"],#each list should contain 3 element and each element should be string and the last element shoudl be a day of the week
    #     "adapter": "csv",
    #     "Input": "user,action,timestamp",
    #     "Transform": "Parsed and structured data",
    #     "Output": "User activity logged: ",
    #     "actions": len(csvdata_before_transform["data"]),
    #     "last": "actions processed"  
    # }
    # csvdata_after_transform = {
    #     "Input": "user,action,timestamp",
    #     "Transform": "Parsed and structured data",
    #     "Output": "User activity logged: ",
    #     "actions": len(csvdata_before_transform["data"]),
    #     "last": "actions processed"
    # }
    # ###########################################################################
    # Streamdata = {
    #     "data": [20, 15,4, 30, 25,9, 24],
    #     "adapter": "Stream",
    # }
    # Streamdata_before_transform = {
    #     "data": [20, 15,4, 30, 25,9, 24],
    #     "adapter": "Stream",
    #     "Input": "Real-time sensor stream",
    #     "Transform": "Aggregated and filtered",
    #     "Output": "Stream summary: ",
    #     "reading": len(Streamdata_after_transform["data"]),
    #     "avg":  sum(Streamdata_after_transform["data"]) / len(Streamdata_after_transform["data"])
    # }
    # Streamdata_after_transform = {
    #     "Input": "Real-time sensor stream",
    #     "Transform": "Aggregated and filtered",
    #     "Output": "Stream summary: ",
    #     "reading": len(Streamdata_after_transform["data"]),
    #     "avg":  sum(Streamdata_after_transform["data"]) / len(Streamdata_after_transform["data"])
    # }