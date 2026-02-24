from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


class ProcessingPipeline(ABC):
    # stages: List[ProcessingStage] = []

    def add_stage(self):
        print("xxxxxxxxxxxxx")

    def process(self, data: Any) -> Union[str, Any]:
        pass

class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        self.pipeline_id = pipeline_id

    
    def process(slef, data) -> Any:
        pass

class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        self.pipeline_id = pipeline_id

    def process(slef, data) -> Any:
        pass

class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        self.pipeline_id = pipeline_id

    def process(slef, data) -> Any:
        pass


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass

class InputStage():
    def process(self, data: Any) -> Dict:
        pass

class TransformStage():
    def process(self, data: Any) -> Dict:
        pass

class OutputStage():
    def process(self, data: Any) -> str:
        pass




class NexusManager():
    def add_pipeline():
        pass

    def process_data():
        pass

if __name__ == "__main__":
    a = ProcessingPipeline()
    a.add_stage()