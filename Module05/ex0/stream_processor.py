from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        data: str
        validation: str
        output: str
        data, validation, output = result.split("|", maxsplit=2)
        string: List[str] = [
                f"Processing data: {data}\n",
                f"Validation: {validation}\n",
                f"Output: {output}",
        ]
        return "".join(string)


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        string: str = ""
        string += f"{data}|"
        if not self.validate(data):
            return "Cannot process data"
        if isinstance(data, (int, float)):
            data: List[Union[int, float]] = [data]
        else:
            data = list(data)
        string += "Numeric data is verified|"
        length: int = len(data)
        total: Union[int, float] = sum(data)
        average: Union[int, float] = total / length
        result1: str = f"Processed {length} numeric values, "
        result2: str = f"sum={total}, avg={average}"
        result: str = result1 + result2
        string += result
        return super().format_output(string)

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if not isinstance(data, (list, tuple, set)):
            return False
        return all(isinstance(x, (int, float)) for x in data)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        string: str = ""
        string += f"\"{data}\"|"
        if self.validate(data):
            string += "Text data verified|"
            leng: int = len(data)
            words: List[str] = data.split()
            count: int = len(words)
            result: str = f"Processed text: {leng} characters, {count} words"
            string += result
            return super().format_output(string)
        else:
            return ("Cannot process data")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        string: str = ""
        string += f"\"{data}\"|"
        if self.validate(data):
            string += "Log entry verified|"
            level: str
            message: str
            level, message = data.split(" ", maxsplit=1)
            if "ERROR:" == level:
                string += f"[ALERT] ERROR level detected: {message}"
            elif "INFO:" == level:
                string += f"[INFO] INFO level detected: {message}"
            return super().format_output(string)
        else:
            return ("Cannot process data")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        info: str = "INFO:"
        alert: str = "ERROR:"
        total_count: int = data.count(info) + data.count(alert)
        if (data.startswith(info) or data.startswith(alert)) \
                and total_count == 1:
            return True
        return False


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    objects = [NumericProcessor(), TextProcessor(), LogProcessor()]
    print("Initializing Numeric Processor...")
    print(objects[0].process([1, 2, 3, 4, 5]), "\n")

    print("Initializing Text Processor...")
    print(objects[1].process("Hello Nexus World"), "\n")

    print("Initializing Log Processor...")
    print(objects[2].process("ERROR: Connection timeout"), "\n")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    inputs: List[Any] = [[1, 2, 3], "achraf kouiss", "INFO: System ready"]
    for index, processor in enumerate(objects):
        res: str = processor.process(inputs[index]).splitlines()[-1]
        print(f"Result {index + 1}:", res[len("Output:"):].strip())

    print("\nFoundation systems online. Nexus ready for advanced streams.")
