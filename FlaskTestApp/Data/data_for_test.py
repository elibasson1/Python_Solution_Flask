def data_for_reversed_strings():
    data = [
        {"input_string": "The quick brown fox jumps over the lazy dog",
         "expected_result": "dog lazy the over jumps fox brown quick The"
         },
        {"input_string": "Eli Basson",
         "expected_result": "Basson Eli"
         }
    ]
    return data


def data_for_invalid_inputs():
    return [
        {"input": "/invalid-endpoint"}
    ]
