
if __name__ == "__main__":
    #  {"sensor": "temp", "value": 23.5, "unit": "C"}
    jsondata = {
        "data": {"sensor": "temp", "value": 23.5, "unit": "C"},
        "adapter": "json"
    }

    jsondata_before_transform = {
        "data": {"sensor": "temp", "value": 23.5, "unit": "C"},
        "adapter": "json",
        "Input": jsondata_before_transform["data"],
        "Transform": "Enriched with metadata and validation",
        "Output": "Processed temperature reading: ",
        "reading": f"{jsondata_before_transform["value"]} {jsondata_before_transform["unit"]}",
        "last":  "(Normal range)"
    }

    jsondata_after_transform = {
        "Input": jsondata_before_transform["data"],
        "Transform": "Enriched with metadata and validation",
        "Output": "Processed temperature reading: ",
        "reading": f"{jsondata_before_transform["value"]} {jsondata_before_transform["unit"]}",
        "last":  "(Normal range)"
    }
    ###########################################################################
    csvdata = {
        "data": ["achraf", "logged", "monday"],#each list should contain 3 element and each element should be string and the last element shoudl be a day of the week
        "adapter": "csv"
    }

    csvdata_before_transform = {
        "data": ["achraf", "logged", "monday"],#each list should contain 3 element and each element should be string and the last element shoudl be a day of the week
        "adapter": "csv",
        "Input": "user,action,timestamp",
        "Transform": "Parsed and structured data",
        "Output": "User activity logged: ",
        "actions": len(csvdata_before_transform["data"]),
        "last": "actions processed"  
    }
    csvdata_after_transform = {
        "Input": "user,action,timestamp",
        "Transform": "Parsed and structured data",
        "Output": "User activity logged: ",
        "actions": len(csvdata_before_transform["data"]),
        "last": "actions processed"
    }
    ###########################################################################
    Streamdata = {
        "data": [20, 15,4, 30, 25,9, 24],
        "adapter": "Stream",
    }
    Streamdata_before_transform = {
        "data": [20, 15,4, 30, 25,9, 24],
        "adapter": "Stream",
        "Input": "Real-time sensor stream",
        "Transform": "Aggregated and filtered",
        "Output": "Stream summary: ",
        "reading": len(Streamdata_after_transform["data"]),
        "avg":  sum(Streamdata_after_transform["data"]) / len(Streamdata_after_transform["data"])
    }
    Streamdata_after_transform = {
        "Input": "Real-time sensor stream",
        "Transform": "Aggregated and filtered",
        "Output": "Stream summary: ",
        "reading": len(Streamdata_after_transform["data"]),
        "avg":  sum(Streamdata_after_transform["data"]) / len(Streamdata_after_transform["data"])
    }