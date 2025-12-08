class Day:
    render_data: list[list[str] | str] = []
    render_interval_ms: int = 100

    def __init__(self, input_data: str, test: bool):
        self.input = input_data
        self.lines = input_data.splitlines()
        self.is_test = test

    def p1(self):
        pass

    def p2(self):
        pass