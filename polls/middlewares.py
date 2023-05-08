import time

from polls.models import Res


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.log_file = "log.txt"

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()

        result = Res(
            path=request.path,
            method=request.method,
            time=end_time - start_time,
        )

        result.save()

        with open(self.log_file, "a") as f:
            log_message = f"Path: {request.path}, Method: {request.method}, Execution time: {end_time - start_time}\n"
            f.write(log_message)

        return response
