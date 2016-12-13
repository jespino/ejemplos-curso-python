from flask import Response

class Ok(Response):
    def __init__(self, *args, **kwargs):
        super(Ok, self).__init__(*args, **kwargs)
        self.status_code = 200
