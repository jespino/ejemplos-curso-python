from mock import patch
import urllib


@patch("urllib.urlopen")
def loquesea(mock):
    mock.return_value.read.return_value = "Test"
    response = urllib.urlopen("http://google.com")
    print(response.read())

loquesea()
