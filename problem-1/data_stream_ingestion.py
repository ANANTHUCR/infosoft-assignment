
class DataStream:
    
    def __init__(self):
        
        self.last_printed_strings: dict[str, int] = {}
        
    def should_output_data_str(self, timestamp: int, data_string: str) -> bool:
        
        if data_string in self.last_printed_strings:
            
            last_printed_timestamp = self.last_printed_strings[data_string]
            
            if timestamp - last_printed_timestamp >= 5:
                self.last_printed_strings[data_string] = timestamp
                
                return True
            else:
                return False
        else:
            self.last_printed_strings[data_string] = timestamp
            
            return True
    
data_stream = DataStream()

data_stream_result = [
    data_stream.should_output_data_str(timestamp=0, data_string="hello"),
    data_stream.should_output_data_str(timestamp=1, data_string="world"),
    data_stream.should_output_data_str(timestamp=6, data_string="hello"),
    data_stream.should_output_data_str(timestamp=7, data_string="hello"),
    data_stream.should_output_data_str(timestamp=8, data_string="world")
]

print(data_stream_result) # [True, True, True, False, True]
