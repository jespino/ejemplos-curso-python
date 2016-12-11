from mock import patch
import urllib

with patch("urllib.urlopen") as mock:
    mock.return_value.read.return_value = "Test"
    response = urllib.urlopen("http://google.com")
    print(response.read())
