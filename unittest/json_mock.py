import mock
import prueba

with mock.patch("json.load") as mock:
    mock.return_value = {"a": 1, "b": 2, "c": 3}

    assert prueba.load() == {"a": 1, "b": 2, "c": 3}
